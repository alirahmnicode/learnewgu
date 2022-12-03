// pronunciation
const pronunciationBtn = $('.pronunciation')
pronunciationBtn.click(function () {
    // find word
    const word = $(this.parentElement.parentElement).find('.word')[0].textContent
    // get pronunciation
    getPronunciation(word)
})

function getPronunciation(_word){
    const url = `https://api.dictionaryapi.dev/api/v2/entries/en/${_word}`
    $.ajax({
        type: 'GET',
        url: url,
        success: function (response) {
            const audioUrl = response[0].phonetics[0].audio
            var audioElement = document.createElement('audio');
            audioElement.setAttribute('src', audioUrl);
            audioElement.play();
        }
    })
}