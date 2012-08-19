$(function(){
	output='today';

	$('#imagesLoad .img').live("mouseenter",
	function(){
		$(this).html('<div class="eye"></div>')
	}).live("mouseleave",
	function(){
		$(this).empty()
	})

	var $container = $('#imagesLoad');

	$container.masonry({
		itemSelector: '.box',
		columnWidth: 100,
		isAnimated: !Modernizr.csstransitions
	});

    //
	$('.vote a.up').live('click',function(event){
		event.preventDefault(); //stop default browser behaviour
		var this_vote = $(this);

		var json = $.ajax({
			dataType: 'json',
			url:$('#imagesLoad').attr('slug')+'/vote/'+$(this).attr('alt')+'/up',
			beforeSend: function () {
				$('#slider-result').html('<img src="/static/images/loading.gif">')
			},
			success: function(data) {

				i++;
				this_vote.parent().find('span').text(data['rating'])
				this_vote.parent().parent().parent().removeClass('box-1').removeClass('box-2').addClass(data['size'])
				$container.masonry('reload')
				$('#slider-result').html(output)
			}
		});
	})

	$('.vote a.down').live('click',function(event){
		event.preventDefault(); //stop default browser behaviour
		var this_vote = $(this);
		//alert($(this).attr('alt'))

		var json = $.ajax({
			dataType: 'json',
			url:$('#imagesLoad').attr('slug')+'vote/'+$(this).attr('alt')+'/down',
			beforeSend: function () {
				$('#slider-result').html('<img src="/images/loading.gif">')
			},
			success: function(data) {
				$container.masonry('reload');
				$('#slider-result').html(output)
			}
		});
		this_vote.parent().parent().parent().remove()
	})

	$('#imagesLoad .img').live('click',function(){
		var img = $(this).css('background-image').split('url(').join('').split(')').join('').split('"').join('')

		$('#lightbox img').attr('src',img)
		var images_height = $('#lightbox img').attr('src',img)
		$('.blackBackground').fadeIn()
		$('#lightbox').css('margin-top',-$('#lightbox img').height()/2)
	}).click(function(){
            window.location = $(this).attr('url');
    });

	$('.blackBackground').click(function(){
		$(this).fadeOut();
	})

	function box() {
		var json = $.ajax({
			dataType: 'json',
			url:'/i/'+$('#imagesLoad').attr('slug')+'/'+output,
			beforeSend: function () {
				$('#slider-result').html('<img src="/images/loading.gif">')
			},
			success: function(data) {
				var items = [];
				i = 0;

				$.each(data, function(key, val) {
					i++;

					var size;
					if(Math.floor( Math.random( ) * (1+1))  == 0){
						size ='box-1'
					}
					else{
						size ='box-2'
					}

					var title='';
					if(val['title']) title = val['title'];
					items.push('<div class="'+size+' box masonry-brick float-left"><div class="img" style="background-image:url('+val['url']+')"></div><div class="imagesPanel black-50"><h3>'+title+'</h3><div class="vote"><span>'+val['rating']+'</span><a href="" alt="'+val['id']+'" class="up"></a><a href="" alt="'+val['id']+'" class="down"></a></div></div></div>');
				});


				$container.prepend(items.join('')).masonry( 'reload' );
				$('#slider-result').html(output)
			}
		});
		//return i;
	}


	box()
	box()

	function interval(){

		box()
		while (i) {
			$('#imagesLoad div.box').last().remove()
			i--;
		}
	}

	var inter = setInterval(interval, 15000)

	$( ".slider" ).slider({
		animate: true,
		range: "min",
		value: 0,
		min: 0,
		max: 100,
		step: 10,

		slide: function( event, ui ) {
			//var output;
			if(ui.value==0){output='today'}
			else output=2000 - ui.value+10
			$( "#slider-result" ).html(output);
			$container.empty()
			box()
		}
	});

});