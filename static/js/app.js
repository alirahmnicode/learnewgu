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

var navBtn = $('.nav-btn')
var itemsBox = $('.side')

navBtn.click(function () {
    if (itemsBox.width() == 0) {
        itemsBox.css('width', '200px')
    } else {
        itemsBox.css('width', '0px')
    }
})


var closeBtn = $('.close')
closeBtn.click(function () {
    box.classList.toggle("active");
})


var voiceBtn = $('.pronunciation')
voiceBtn.click(function () {
    var text_per = this.parentElement.parentElement.children[0].children[1].textContent
    responsiveVoice.speak(text_per)
})