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
    $("#confirm").one("click",function(event) {
        event.preventDefault();
        console.log("bla");

     var csrftoken = getCookie('csrftoken');
     console.log("dupa");
     var total_price=$("#total_price").text();
     console.log(total_price);
       $.post({
        url: "/confirm_order/",
        data: {
            csrfmiddlewaretoken: csrftoken,
            totalprice:total_price,
        },
        }).done(function (response) {
             var $result = $("#confirmation");
            $result.text("Check your email!")

        })
            .fail(function (e) {
                alert("nie poszlo");
                console.log(e)

                });
        })

});

