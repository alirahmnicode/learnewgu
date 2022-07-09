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

var host = window.location.host


$(document).ready(function () {
    $(".viewed").click(function () {
        // get this vocab pk
        thisBtn = this
        pk = getPk(thisBtn)
        view_url = `http://${host}/vocab/review/${pk}/`
        
        // send ajax request
        url = view_url
        $.ajax(url, {
            type:'POST',
            headers: {'X-CSRFToken': csrftoken},
            success:function(response){
                // update html
                getCountBox(thisBtn).textContent = response['count']
            }
        })
        
    });
});


function getPk(obj) {
    return obj.parentElement.firstElementChild.value
}

function getCountBox(obj) {
    return obj.parentElement.parentElement.parentElement.children[0].children[1].lastElementChild
}