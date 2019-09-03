$(document).ready(function(){
//Banner Slider
    $('.banner-sec .owl-carousel').owlCarousel({
        loop:true,
        nav:false,
        items:1,
        autoplay:true,
        animateOut: 'fadeOut', 
        autoWidth:false,
        dots:false,
    });
    
//Testimonial Slider
    $('.testi-sec .owl-carousel').owlCarousel({
        loop:true,
        nav:true,
        items:1,
        autoplay:true,
        autoWidth:false,
        dots:false,
    });
    $( ".test-sec .owl-carousel .owl-prev" ).html('<i class="fa fa-angle-left" aria-hidden="true"></i>'); 
    $( ".test-sec .owl-carousel .owl-next" ).html('<i class="fa fa-angle-right" aria-hidden="true"></i>');
    

    
    $(".nav-icon").click(function(){
        $(".mob-nav").toggleClass("show-nav")
    });
    
});