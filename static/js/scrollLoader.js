var myDiv = document.getElementsByClassName('all-article')[0]
var number = 0
$(window).scroll(function (event) {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        number += 5
        console.log(number)
        $.ajax({
            type: "GET",
            url: `http://localhost:5000/articles/all/?n=${number}`,
            success: function (response) {
                for (let i = 0; i < response.articles.length; i++) {
                    var box = `<div class="article box">
                                <div>
                                    <a href="/articles/detail/${response.articles[i].slug}/${response.articles[i].pk}/">
                                        <img src="${response.articles[i].image}" alt="">
                                        <h2>
                                            ${response.articles[i].title}
                                        </h2>
                                    </a>
                                </div>
                            </div>`
                    $('.all-article').append(box)
                }
            }
        })
    }
})