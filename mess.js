// // Seeded random, for reproducability
// function Rnd () {
//     var x = Math.sin(seed++) * 10000;
//     return x - Math.floor(x);
// }

// // Mess around with the loaded SVG
// function jsMess(_cont=null) {
//     var target = document.getElementById("target");
//     try {
//         target.append("ASDF");
//         target.childNodes[Math.floor(Rnd()*target.childNodes.length)].innerHTML = "bluh";
//         x = target.animate({});
//         x.play(); x.dispatchEvent(new Event({}));
//         y = x.currentTime;
//         target.appendChild(
//             target.childNodes[Math.floor(Rnd()*target.childNodes.length)]
//         );
//         target.childNodes[Math.floor(Rnd()*target.childNodes.length)].innerHTML = "bluh";
//         x = target.childNodes[Math.floor(Rnd()*target.childNodes.length)].animate({});
//         x.play(); x.dispatchEvent(new Event({}));
//         y = x.currentTime;
//         target.removeChild(
//             target.childNodes[Math.floor(Rnd()*target.childNodes.length)]
//         );
//     } catch(e) {}
//     if (_cont) return _cont();
// }

// // Reload with hash
// function outputReload() {
// 	document.location.hash = seed;
//     if (seed < 1000) document.location.reload();
// }
function dumpPage() {
	var df;
	if (typeof dump === "undefined") df = console.log;
	else df = dump;
	df('\n---\n'+btoa(document.getElementsByTagName('html')[0].outerHTML)+'\n---\n');
}