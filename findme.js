
// Get the H1 heading
var h1 = document.querySelector('h1');

// Get it's position in the viewport
var bounding = h1.getBoundingClientRect();

// Log the results
console.log(bounding);
// {
// 	height: 118,
// 	width: 591.359375,
// 	top: 137,
// 	bottom: 255,
// 	left: 40.3125,
// 	right: 631.671875
// }

if (
	bounding.top >= 0 &&
	bounding.left >= 0 &&
	bounding.right <= (window.innerWidth || document.documentElement.clientWidth) &&
	bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)
) {
	console.log('In the viewport!');
} else {
	console.log('Not in the viewport... whomp whomp');
}

var isInViewport = function (elem) {
	var distance = elem.getBoundingClientRect();
	return (
		distance.top >= 0 &&
		distance.left >= 0 &&
		distance.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
		distance.right <= (window.innerWidth || document.documentElement.clientWidth)
	);
};

// var findMe = document.querySelector('#find-me');

// window.addEventListener('scroll', function (event) {
// 	if (isInViewport(findMe)) {
// 		console.log('In viewport!');
// 	} else {
//     console.log('Nope...');
//   }
// }, false);


https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect



