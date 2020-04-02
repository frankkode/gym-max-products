$(document).ready(function () {

    var productForm = $(".form-product-ajax");

    productForm.submit(function (event) {
        event.preventDefault();

        var thisForm = $(this);
        var actionEndpoint = thisForm.attr("action");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();
        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {

                var submitSpan = thisForm.find(".submit-span");
                if (data.added) {
                    submitSpan.html("In cart <button type='submit' class='btn remove'>Remove?</button>");
                } else {
                    submitSpan.html("<button type='submit'  class='btn btn-success add-to-cart'>Add to cart</button>");
                }
                var navbarCount = $(".navbar-cart-count");
                navbarCount.text(data.cartItemCount);
            },
            error: function (errorData) {
                console.log("error");
                console.log(errorData);
            }
        });
    });

});

/*nav and header*/
// Sticky Header
$(window).scroll(function () {

    if ($(window).scrollTop() > 100) {
        $('.main_h').addClass('sticky');
    } else {
        $('.main_h').removeClass('sticky');
    }
});

// Mobile Navigation
$('.mobile-toggle').click(function () {
    if ($('.main_h').hasClass('open-nav')) {
        $('.main_h').removeClass('open-nav');
    } else {
        $('.main_h').addClass('open-nav');
    }
});

$('.main_h li a').click(function () {
    if ($('.main_h').hasClass('open-nav')) {
        $('.navigation').removeClass('open-nav');
        $('.main_h').removeClass('open-nav');
    }
});

// navigation scroll lijepo radi materem
$('nav a').click(function (event) {
    var id = $(this).attr("href");
    var offset = 70;
    var target = $(id).offset().top - offset;
    $('html, body').animate({
        scrollTop: target
    }, 500);
    event.preventDefault();
});