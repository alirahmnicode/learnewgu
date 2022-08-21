var html = ''
var numbers = []

function htmlCreator(word) {
    numbers = generateRandomNumber()
    for (let i = 0; i < word.length; i++) {
        if (numbers.includes(i)) {
            html += `<input type="text" maxlength="1" 
                        style="width:20px;text-align: center;outline: none;border: none;border-radius: 4px;" 
                        name="${i + 1}">`
        } else {
            html += `<span>${word[i]}</span>`
        }

    }
    $('.dictation')[0].innerHTML = html
}

function generateRandomNumber() {
    var x = 0
    if (word.length > 3) {
        x = parseInt(word.length / 2) - 1
    } else {
        x = 1
    }
    for (let i = 0; i < x; i++) {
        number = Math.floor(Math.random() * word.length)
        if (!numbers.includes(number)) {
            numbers[i] = number
        }
    }
    return numbers
}
var word = $(".data")[0].getAttribute('data-word')
htmlCreator(word)

var clientText = ''

const checkBtn = $('.check-btn')
const nextBtn = $('.next-btn')

checkBtn.click(function () {
    var nodes = document.getElementsByClassName('dictation')[0].childNodes
    clientText = ''
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].tagName == "INPUT") {
            clientText += nodes[i].value
        } else {
            clientText += nodes[i].textContent
        }
    }
    check(this)
})


nextBtn.click(function () {
    // get next word
    getWord()
    check(this)
})


function check(btn) {
    var word = $(".data")[0].getAttribute('data-word')
    if (word === clientText) {
        btnIsPending(true, btn)
        getWord()
        btnIsPending(false, btn)
    } else {
        verify()
    }
}

function verify() {
    var nodes = document.getElementsByClassName('dictation')[0].childNodes
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].tagName == "INPUT") {
            if (nodes[i].value != word[i]) {
                $(`INPUT[name="${i + 1}"]`).css('background', 'red')
                $(`INPUT[name="${i + 1}"]`).css('color', '#fff')
            } else {
                $(`INPUT[name="${i + 1}"]`).css('background', 'green')
            }
        }
    }
}

function getWord() {
    var url = window.location.href
    $.ajax({
        type: 'GET',
        url: url,
        success: function (response) {
            // close orignal word box if open
            $('.or-word').css('display', 'none')
            // create new html
            html = ''
            $(".data")[0].setAttribute('data-word', response.text)
            // set translation
            $('#translation')[0].textContent = response.translation
            htmlCreator($(".data")[0].getAttribute('data-word'))
        }
    })
}