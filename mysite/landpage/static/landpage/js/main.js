$(document).ready(function(){


	$("#portfolio-contant-active").mixItUp();


	$("#testimonial-slider").owlCarousel({
	    paginationSpeed : 500,      
	    singleItem:true,
	    autoPlay: 3000,
	});




	$("#clients-logo").owlCarousel({
		autoPlay: 3000,
		items : 5,
		itemsDesktop : [1199,5],
		itemsDesktopSmall : [979,5],
	});

	$("#works-logo").owlCarousel({
		autoPlay: 3000,
		items : 5,
		itemsDesktop : [1199,5],
		itemsDesktopSmall : [979,5],
	});


	// google map
		var map;
		function initMap() {
		  map = new google.maps.Map(document.getElementById('map'), {
		    center: {lat: -34.397, lng: 150.644},
		    zoom: 8
		  });
		}


	// Counter

	$('.counter').counterUp({
        delay: 10,
        time: 1000
    });


	// Tag Line
	var $tagLine = $('#tag-line');
	var currentIndex = 0
	var listOfTagLines = [
		'NTU Students',
		'the best developers in Taiwan',
		'the Hundi'
	];
	function setTagLine () {
		$tagLine[0].style.webkitAnimation = 'none';
    setTimeout(function() {
		  $tagLine.text(listOfTagLines[currentIndex % listOfTagLines.length]);
      $tagLine[0].style.webkitAnimation = '';
    }, 100);
		currentIndex += 1;
	}
	setInterval(setTagLine, 1000 * 3);
	setTagLine();

});




