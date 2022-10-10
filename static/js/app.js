// filter box
const filterBtn = $("#filter-btn")
const filterBox = $('.s-f')[0]
filterBtn.click(function () {
    console.log('ali')
    filterBox.classList.toggle('active')
})

// translation
const accordion = $('.accordion')
accordion.click(function () {
    var box = $(this.offsetParent).find('.translation')[0]
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
    var box = $(this.offsetParent)[0];
    box.classList.toggle("active");
})


// var voiceBtn = $('.pronunciation')
// voiceBtn.click(function () {
//     btnIsPending(true, this)
//     var text_per = this.parentElement.parentElement.children[0].children[1].textContent
//     responsiveVoice.speak(text_per)
//     btnIsPending(false, this)
// })


$(".close-message").click(function () {
    $(this)
        .parent(".alert")
        .fadeOut();
});

// set side bars height
const windowHeight = $( window ).height()
if( windowHeight > $('.container').height()) {
    $('.side').css('height', `${windowHeight}px`)
}