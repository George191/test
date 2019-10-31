$(".pricing-column").hover(function () {
    $(this).siblings('div').removeClass('green-pr feature-package');
    $(this).siblings('div').find('a.green').removeClass('green').addClass('gray');
    $(this).addClass("green-pr feature-package");
    $(this).find('a').addClass('green');
});