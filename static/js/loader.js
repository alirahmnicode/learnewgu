var myDiv = document.getElementsByClassName('all-article')[0]
var number = 0
$(window).scroll(function (event) {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        number += 15
        console.log('ali')
        $.ajax({
            type: "GET",
            url: `http://localhost:8000/vocab/list/?n=${number}`,
            success: function (response) {
                for (let i = 0; i < response.objects.length; i++) {
                    var box = `<div>
                                    <div>${response.objects[i].counter}</div>
                                    <div>${response.objects[i].text}</div>
                                    <div>${response.objects[i].translation}</div>
                                    <div class="view-count">${response.objects[i].review_count}</div>
                                    <div>${response.objects[i].type}</div>
                                    <div>${response.objects[i].created}</div>
                                    <div>
                                        <input type="hidden" name="pk" value="${response.objects[i].pk}">
                                        <button class="viewed">Viewed</button>
                                    </div>
                                </div>`
                    $('.vocabs').append(box)
                }
                console.log(response)
            }
        })
    }
})