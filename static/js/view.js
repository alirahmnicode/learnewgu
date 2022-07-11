var host = window.location.host

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$(document).ready(function () {
    $(".viewed").click(function () {
        console.log('ali')
        // get this vocab pk
        thisBtn = this
        pk = getPk(thisBtn)
        view_url = `http://${host}/vocab/review/${pk}/`
        // send ajax request
        url = view_url
        $.ajax(url, {
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            success: function (response) {
                // update html
                if ($(".random-review").data().review === 'random') {
                    // request sended from random page 
                    getNewVocab()
                } else {
                    getCountBox(thisBtn).textContent = response['count']
                }
            }
        })
    });
});


var nextBtn = $("#next")

nextBtn.click(function (){
    getNewVocab()
})

function getNewVocab() {
    var view_url = `http://${host}/vocab/random-review/`
    var url = view_url
    $.ajax(url, {
        type: 'GET',
        success: function (response) {
            // update html
            $("#text")[0].textContent = response.object['text']
            $("#translation")[0].textContent = response.object['translation']
            $("#type")[0].textContent = response.object['type']
            $("#date")[0].textContent = response.object['date']
            $("#r-count")[0].textContent = response.object['review_count']
            $("input[name=pk]")[0].value = response.object['pk']
        }
    })
}


function getPk(obj) {
    return obj.parentElement.firstElementChild.value
}

function getCountBox(obj) {
    return obj.parentElement.parentElement.parentElement.children[0].children[1].lastElementChild
}