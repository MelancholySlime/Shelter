var _ua=(function(d){var c={0:(d.indexOf('windows')!=-1&&d.indexOf('phone')!=-1)||d.indexOf('iphone')!=-1||d.indexOf('ipod')!=-1||(d.indexOf('android')!=-1&&d.indexOf('mobile')!=-1)||(d.indexOf('firefox')!=-1&&d.indexOf('mobile')!=-1)||d.indexOf('blackberry')!=-1,iPhone:(d.indexOf('iphone')!=-1),Android:(d.indexOf('android')!=-1&&d.indexOf('mobile')!=-1)};var b=(d.indexOf('windows')!=-1&&d.indexOf('touch')!=-1)||d.indexOf('ipad')!=-1||(d.indexOf('android')!=-1&&d.indexOf('mobile')==-1)||(d.indexOf('firefox')!=-1&&d.indexOf('tablet')!=-1)||d.indexOf('kindle')!=-1||d.indexOf('silk')!=-1||d.indexOf('playbook')!=-1;var a=!c[0]&&!b;return{Mobile:c,Tablet:b,PC:a}})(window.navigator.userAgent.toLowerCase());function addBrowserClass(){var c=function(e,d){if(document.documentElement.className){document.documentElement.className+=' '}document.documentElement.className+=e+(d!==''?' '+e+(d*1).toString().replace('.','_'):'')};var b=window.navigator.userAgent.toLowerCase();var a=window.navigator.appVersion.toLowerCase();if(get=b.match(/msie (\d+(\.\d+)?)/i)){c('ie',get[1])}else{if(get=b.match(/Trident.+rv\:(\d+(\.\d+)?)/i)){c('ie',get[1])}else{if(get=b.match(/chrome\/(\d+(\.\d+)?)/i)){c('chrome',get[1])}else{if(get=b.match(/firefox\/(\d+(\.\d+)?)/i)){c('firefox',get[1])}else{if(get=b.match(/opera\/(\d+(\.\d+)?)/i)){c('opera',get[1])}else{if(get=b.match(/safari\/(\d+(\.\d+)?)/i)){c('safari',get[1])}}}}}}if(get=b.match(/iPhone OS (\d+(\.\d+)?)/i)){c('ios',get[1])}if(get=b.match(/iPhone;/i)){c('iphone','')}else{if(get=b.match(/iPod;/i)){c('ipod','')}else{if(get=b.match(/iPad;/i)){c('ipad','')}else{if(get=b.match(/Android (\d+(\.\d+)?)/i)){c('android',get[1])}}}}}addBrowserClass();
// example
// if(_ua.PC)
// if(_ua.Tablet)
// if(_ua.Mobile[0])
// if(_ua.Mobile.iPhone)
// if(_ua.Mobile.Android)

$(function() {
	var ww;
	var wh;
	var scTop;
	var box = [];
	var mainvisualHeight = $('.mainvisual').height();
	var loadScroll;
	var body = $('body');
	var header = $('header');
	var bgIntroductionNumber;
	var bgIntroductionPosition;
	var loadingCheck = $('html').hasClass('loading');

	if(_ua.PC){
		$('html').addClass('pc');
	}
	if(_ua.Tablet){
		$('html').addClass('tablet');
	}

	$(window).on('load',function(){
		ww = $(window).width();
		wh = $(window).height();
		loadScroll = mainvisualHeight - wh;
		scTop = $(window).scrollTop();
		$('.box').each(function(){
			boxPosition = $(this).offset().top-70;
			box.push(boxPosition);
		});
		boxLength = box.length;
		setTimeout(function(){
			$('.load').addClass('off');
		},1000);
		setTimeout(function(){
			$('html,body').animate({
				scrollTop: loadScroll
			},1000,'swing');
			setTimeout(function(){
				$('html').removeClass('loading');
				$('.load').addClass('remove');
			},1000);
		},2000);

	});
	$(window).on('resize',function(){
		$('.box').each(function(){
			boxPosition = $(this).offset().top;
			box.push(boxPosition);
		});
	});
	var scCount = 0;
	var scNow;
	$(window).on('scroll',function(){
		scTop = $(window).scrollTop();
		scNow = scCount;
		if(scTop < box[0]){
			scCount = 0;
		}
		if(scTop >= box[0]) {
			scCount = 1;
		}
		if(scTop >= box[1]) {
			scCount = 2;
		}
		if(scTop >= box[2]) {
			scCount = 3;
		}
		if(scTop >= box[3]) {
			scCount = 4;
		}
		if(scTop >= box[4]) {
			scCount = 5;
		}
		if(scTop >= box[5]) {
			scCount = 6;
		}
		if(scTop >= box[6]) {
			scCount = 7;
		}

		if(scNow != scCount){
			if(scCount>0) {
				$('.totop').addClass('on');
			}else {
				$('.totop').removeClass('on');
			}
			body.removeClass();
			body.addClass('sec'+scCount);
		}

		$('.modal_movie').colorbox({
			iframe:true,
			innerWidth:960,
			innerHeight:540,
			opacity:.75
		});

		bgIntroductionNumber = scTop*.08;
		$('.introduction').css('background-position','center '+ -bgIntroductionNumber +'px');
		header.css("left", -$(window).scrollLeft());
	});

	$('.gnav').find('li').on('click',function(){
		$('.gnav').find('li').removeClass('on');
		$(this).addClass('on');
        var link = $(this).data('link');
        if(link === 'top') {
            $('html,body').animate({scrollTop:0},800);
        }else {
            var $linkEle = $('#'+link);
            $('html,body').animate({scrollTop:$linkEle.offset().top - 70},800);
        }
		return false;
    });
	$('.totop').on('click',function(){
		$('html,body').animate({scrollTop:loadScroll},800);
	});
});
