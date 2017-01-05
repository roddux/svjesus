#!/usr/bin/env bash

# Globals
FUZZGROUP="NEWFUZZ"
USER=`whoami`
LIMIT="650M"
CGCREATE=""
CGEXEC=""
CGDELETE=""

# Check that the cgroup tools are installed
which cgcreate &>/dev/null
INSTALLED=$?
which cgexec &>/dev/null
let INSTALLED=$INSTALLED+$?
which cgdelete &>/dev/null
let INSTALLED=$INSTALLED+$?

if [ $INSTALLED != 0 ]
	then
		echo "Error: cgroup tools (cgcreate/cgexec/cgdelete) are required"
		exit 1
	else
		CGCREATE=`which cgcreate`
		CGEXEC=`which cgexec`
		CGDELETE=`which cgdelete`
fi

# Create the cgroup
echo "Creating memory-limited cgroup '$FUZZGROUP'... "
sudo $CGCREATE -a $USER:$USER -t $USER:$USER -g memory:$FUZZGROUP
if [ ! -w /sys/fs/cgroup/memory/$FUZZGROUP/memory.limit_in_bytes ]
	then
		echo "Error creating cgroup"
		exit 1
fi
echo -e "Done\n"

# Set a memory limit to catch leaks without bringing down the whole box
echo "Setting memory limit of $LIMIT for '$FUZZGROUP'... "
echo $LIMIT > /sys/fs/cgroup/memory/$FUZZGROUP/memory.limit_in_bytes
echo -e "Done\n"

# Tell the user to start a browser inside the group
# NOTE: This will probably be moved into the handler, to automatically catch crashes
echo "Now run one of the following:"
echo -e "\t$ $CGEXEC -g memory:$FUZZGROUP chromium"
echo -e "\t$ $CGEXEC -g memory:$FUZZGROUP firefox --no-remote --new-instance --profile /tmp/\n"
echo "Remove the group (after fuzzing) with:"
echo -e "\t$ sudo $CGDELETE -g memory:$FUZZGROUP"