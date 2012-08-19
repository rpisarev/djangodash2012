$(function(){



	$('#imagesLoad').masonry({
		itemSelector: '.box',
		isAnimated: true,
		isFitWidth: true,
	});
	
	$('#imagesLoad .img').hover(
	function(){
		$(this).html('<div class="eye"></div>')
	},
	function(){
		$(this).empty()
	}).click(function(){
            window.location = $(this).attr('url');
    })
	
	
	
	
	$('#imagesLoad .img').click(function(){
		var img = $(this).css('background-image').split('url(').join('').split(')').join('').split('"').join('')

		$('#lightbox img').attr('src',img)
		var images_height = $('#lightbox img').attr('src',img)
		
		
		$('.blackBackground').fadeIn()
		$('#lightbox').css('margin-top',-$('#lightbox img').height()/2)
		
	})
	
	$('.blackBackground').click(function(){
		$(this).fadeOut();
	})
	
	

});