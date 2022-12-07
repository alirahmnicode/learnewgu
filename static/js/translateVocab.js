var host = window.location.origin
var textField = $('.text-trns')
var translationField = $('#id_translation')
var formBtn = $('.form-btn')[0]

textField.keyup(function () {
    const thisInput = $(this)
    const text = this.value
    const inputName = thisInput[0].name
    const target = 'fa'
    if (text != '') {
        // check if the word exits in db
        if (text.split(' ').length < 3) {
            check(text)
        }
        // get words translation
        const url = `${host}/translate/text/?text=${text}`
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                if (inputName == 'word') {
                    put_word_translation(response)
                } else {
                    put_sentence_translation(thisInput, response)
                }
            }
        })
    } else {
        translationField[0].value = ''
    }
})


function check(word) {
    const checkUrl = `${host}/vocab/check/?word=${word}`
    $.ajax({
        type: 'GET',
        url: checkUrl,
        success: function (response) {
            if(!response) {
                // the word exists
                $('#word-check')[0].textContent = 'This word exists.'
            } else {
                $('#word-check')[0].textContent = ''
            }
        }
    })
}

function put_word_translation(response){
    $('.word-translation')[0].value = response.tr_text
}

function put_sentence_translation(input, response){
   const trnField = input[0].parentElement.nextElementSibling.firstElementChild
   trnField.value = response.tr_text
}