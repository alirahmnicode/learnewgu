var textField = $('#id_text')
var translationField = $('#id_translation')

textField.keyup(function () {
    const text = textField[0].value
    const target = 'fa'
    if (text != '') {
        // send ajax
        const url = `http://localhost:8000/translate/text/?text=${text}`
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                translationField[0].value = response
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