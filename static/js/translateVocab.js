var host = window.location.origin
var textField = $('#id_text')
var translationField = $('#id_translation')
var formBtn = $('.form-btn')[0]

textField.keyup(function () {
    const text = textField[0].value
    const target = 'fa'
    if (text != '') {
        // check if the word exits in db
        if (text.split(' ').length < 3) {
            check(text)
        }
        // get words translation
        btnIsPending(true, formBtn)
        const url = `${host}/translate/text/?text=${text}`
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                translationField[0].value = response
                btnIsPending(false, formBtn)
            }
        })
    } else {
        translationField[0].value = ''
    }
    // set choose field
    if (text.split(' ').length > 2) {
        $('#id_type')[0].value = 'phrase'
    }
    else {
        $('#id_type')[0].value = 'word'
    }
})

translationField.keyup(function () {
    btnIsPending(false, formBtn)
})

function check(word) {
    const checkUrl = `${host}/vocab/check/?word=${word}`
    $.ajax({
        type: 'GET',
        url: checkUrl,
        success: function (response) {
            if(!response) {
                // word exist
                $('#word-check')[0].textContent = 'ali'
            } else {
                $('#word-check')[0].textContent = ''
            }
        }
    })
}