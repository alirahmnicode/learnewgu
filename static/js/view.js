var host = window.location.origin
var fullPath = window.location.href

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

var viewBtn = $(".viewed")
$(document).ready(function () {
    viewBtn.click(function () {
        // get this vocab pk
        var thisBtn = this
        pk = getPk(thisBtn)
        view_url = `${host}/vocab/review/${pk}/`
        // send ajax request
        url = view_url
        btnIsPending(true, thisBtn)
        $.ajax(url, {
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            success: function (response) {
                // update html
                if ($(".random-review").data().review === 'random') {
                    // request sended from random page 
                    getNewVocab(thisBtn)
                } else {
                    getCountBox(thisBtn).textContent = response['count']
                }
                btnIsPending(false, thisBtn)
            }
        })
    });
});


var nextBtn = $("#next")

nextBtn.click(function () {
    getNewVocab(this)
})

function getNewVocab(thisBtn) {
    var view_url = `${host}/vocab/random-review/`
    var url = view_url
    btnIsPending(true, thisBtn)
    $.ajax(url, {
        type: 'GET',
        success: function (response) {
            // update html
            if (fullPath.split('ln=').length > 1) {
                $("#text")[0].textContent = response.object['translation']
                $("#translation")[0].textContent = response.object['text']
            } else {
                $("#text")[0].textContent = response.object['text']
                $("#translation")[0].textContent = response.object['translation']
            }
            $("#type")[0].textContent = response.object['type']
            $("#date")[0].textContent = response.object['date']
            $("#r-count")[0].textContent = response.object['review_count']
            $("input[name=pk]")[0].value = response.object['pk']
            btnIsPending(false, thisBtn)
        }
    })
}


function getPk(obj) {
    return obj.parentElement.firstElementChild.value
}

function getCountBox(obj) {
    return obj.parentElement.parentElement.parentElement.children[0].children[1].lastElementChild
}