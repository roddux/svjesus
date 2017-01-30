#!/usr/bin/env bash

# Globals
FUZZGROUP="NEWFUZZ"
# USER=`whoami`
USER="roddux"
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
which sudo &>/dev/null
USESUDO=$?
echo "Creating memory-limited cgroup '$FUZZGROUP'... "
if [ $USESUDO != 0 ]
	then
		echo "sudo not found! Using su-- please enter root password"
		su -c "$CGCREATE -a $USER:$USER -t $USER:$USER -g memory:$FUZZGROUP"
	else
		sudo $CGCREATE -a $USER:$USER -t $USER:$USER -g memory:$FUZZGROUP
fi
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
if [ $USESUDO != 0 ]
	then
		echo -e "\t$ su -c \"$CGDELETE -g memory:$FUZZGROUP\""
	else
		echo -e "\t$ sudo $CGDELETE -g memory:$FUZZGROUP"
fi