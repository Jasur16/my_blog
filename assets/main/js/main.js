var nav = document.querySelector('nav');

window.addEventListener('scroll', function () {
	if (window.pageYOffset > 100) {
		nav.classList.add('bg-light', 'shadow');
	} else {
		nav.classList.remove('bg-light', 'shadow');
	}
});