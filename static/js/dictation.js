var html = ''
var numbers = []

function htmlCreator(word) {
    numbers = generateRandomNumber()
    for (let i = 0; i < word.length; i++) {
        if (numbers.includes(i)) {
            html += `<input type="text" maxlength="1" style="width:10px" name="${i + 1}">`
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
    check()
})


function check() {
    var word = $(".data")[0].getAttribute('data-word')
    if (word === clientText) {
        var url = window.location.href
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                // $('.dictation')[0].innerHTML = ''
                html = ''
                $(".data")[0].setAttribute('data-word', response.text)
                htmlCreator($(".data")[0].getAttribute('data-word'))
            }
        })
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