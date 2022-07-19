// open filter box
var filterBox = $('.s-f')
var accordion = $('.accordion')
var box;

accordion.click(function () {
    var boxMode = this.getAttribute('data-box')
    if (boxMode == 'filter') {
        box = filterBox[0]
    } else {
        box = this.parentElement.parentElement.nextElementSibling
    }
    box.classList.toggle("active");

})