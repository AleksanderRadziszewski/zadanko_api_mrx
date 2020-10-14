document.addEventListener("DOMContentLoaded",function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie("csrftoken");
    var $fund_article = $("#article");

    $fund_article.one("keyup", function (event) {
        event.preventDefault();
        var typingTimer;    //timer identifier
        var doneTypingInterval = 1000;
        clearTimeout(typingTimer);
        if ($('#article').val()) {
            typingTimer = setTimeout(input_send, doneTypingInterval);
        }

        function input_send() {

            var article_search = $fund_article.val();
            console.log(article_search);
            $.post({
                url: "/articles/_search",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    article_search: article_search
                }
            }).done(function (repsonse) {
                var $result_list = $("#search_list");
                console.log($result_list);
                $result_list.html(repsonse)

            })
                .fail(function (e) {
                    alert("nie poszlo");
                    console.log(e)

                });
        }
    });

    $(".add").one("click", function add_product(event) {
        event.preventDefault();
        var csrftoken = getCookie('csrftoken');
        console.log(this.dataset.id);
        $.post({
            url: "/add_product_to_cart/",
            data: {
                csrfmiddlewaretoken: csrftoken,
                id_product: this.dataset.id
            },
            function(data, status) {
                alert(status);
            }
        });

    });

    function increase_quantity() {
        var csrftoken = getCookie('csrftoken');
        $.post({
            url: "/changequantity/",
            data: {
                csrfmiddlewaretoken: csrftoken,
                id_product: this.dataset.id,
            },
            function(data, status) {
                alert(status);
            }
        });

    }

    $(document).ready(function (event) {
        event.preventDefault;
        $("#increase").click(increase_quantity);

    });


});






