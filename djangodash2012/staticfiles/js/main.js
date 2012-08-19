$(function(){
	output='today';

    /*
	$('#imagesLoad .img').live("mouseenter", function(){
		$(this).html('<div class="eye"></div>')
	}).live("mouseleave", function(){
		$(this).empty()
	})*/

    $('#mainBody .img').click(function(){
        window.location = $(this).attr('url');
    });

	var $container = $('#imagesLoad');

	$container.masonry({
		itemSelector: '.box',
		columnWidth: 100,
		isAnimated: !Modernizr.csstransitions
	});

    // fixed
    $('a.vote_link').live('click', function(event){
        event.preventDefault(); //stop default browser behaviour
        var this_vote = $(this);
        type = $(this).attr('type');
        url = '/vote/' + $(this).attr('alt') + '/' + type;
        var json = $.ajax({
            dataType: 'json',
            url:url,
            beforeSend: function () {

            },
            success: function(data) {
                this_vote.parent().find('span').text(data['rating'])
            }
        });
    })

    // lightbox
	$('#imagesLoad .img').live('click',function(){
		var img = $(this).css('background-image').split('url(').join('').split(')').join('').split('"').join('')

		$('#lightbox img').attr('src',img)
		var images_height = $('#lightbox img').attr('src',img)
		$('.blackBackground').fadeIn()
		$('#lightbox').css('margin-top',-$('#lightbox img').height()/2)
	});

	$('.blackBackground').click(function(){
		$(this).fadeOut();
	})

    // load images
	function box() {
        var url = '/i/'+$('#imagesLoad').attr('slug')+'/'+output;
		var json = $.ajax({
			dataType: 'json',
			url: url,
			beforeSend: function () {
				loader_set();
			},
            complete: function(){
                loader_unset();
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
					items.push('<div class="'+size+' box masonry-brick float-left"><div class="img" style="background-image:url('+val['url']+')"></div><div class="imagesPanel black-50"><h3>'+title+'</h3><div class="vote"><span>'+val['rating']+'</span><a href="javascript:void(null);" alt="'+val['id']+'" class="vote_link up" type="up"></a><a href="javascript:void(null);" alt="'+val['id']+'" class="vote_link down" type="down"></a></div></div></div>');
				});

				$container.prepend(items.join('')).masonry( 'reload' );
			}
		});
		//return i;
	}

    if($('#imagesLoad').length > 0){
        box();
    }

	function interval(){
		box()
		while (i) {
			$('#imagesLoad div.box').last().remove()
			i--;
		}
	}

    function loader_set(){
        $('#slider-result').html('<img src="/static/images/loading.gif">');
    }

    function loader_unset(){
        $('#slider-result').html(output);
    }

	var inter = setInterval(interval, 60000)

	$( ".slider" ).slider({
		animate: true,
		range: "min",
		value: 0,
		min: 0,
		max: 80,
		step: 10,

		slide: function( event, ui ) {
			//var output;
			if(ui.value==0){output='today'}
			else output=2000 - ui.value+10
			loader_unset();
			$container.empty()
			box()
		}
	});
});