var myDiv = document.getElementsByClassName('all-article')[0]
var number = 0
var host = window.location.origin

$(window).scroll(function (event) {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        number += 15
        view_url = `${host}/vocab/list/?n=${number}`
        $.ajax({
            type: "GET",
            url: view_url,
            success: function (response) {
                for (let i = 0; i < response.objects.length; i++) {
                    var box = `<div class="box">
                    <div>
                        <div class="text mr">
                            <div class="mr">${response.objects[i].counter}</div>
                            <div class="mr"><span>${response.objects[i].text}</span></div>
                            <div class="mr">
                                <button class="btn">see trns</button>
                            </div>
                        </div>
                        <div class="translation mr">
                            <span>${response.objects[i].translation}</span>
                        </div>
                    </div>
                    <div>
                        <div class="info">
                            <div class="mr">
                                <span>type : ${response.objects[i].type}</span>
                            </div>
                            <div class="mr">
                                <span>review count :</span> <span class="review-count"> ${response.objects[i].review_count}</span>
                            </div>
                        </div>
                        <div class="manage">
                            <div class="mr">
                                <a href="${host}/vocab/${response.objects[i].pk}/edit/">Edit</a>
                            </div>
                            <div class="mr">
                                <a href="${host}/vocab/${response.objects[i].pk}/delete/">Delete</a>
                            </div>
                            <div class="h">
                                <input type="hidden" name="pk" value="${response.objects[i].pk}">
                                <button class="btn viewed random-review" data-review="list">Viewed</button>
                            </div>
                        </div>
                        <div class="date">
                            <span>${response.objects[i].created}</span>
                        </div>
                    </div>
                </div>`
                    $('.vocabs').append(box)
                }
            }
        })
    }
})