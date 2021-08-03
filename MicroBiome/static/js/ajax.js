function delay(callback, ms) {
    var timer = 0;
    return function() {
        var context = this,
            args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function() {
            callback.apply(context, args);
        }, ms || 0);
    };
}

// https://stackoverflow.com/questions/1909441/how-to-delay-the-keyup-handler-until-the-user-stops-typing

$(function() {
    $("#search").keyup(
        delay(function() {
            $.ajax({
                type: "POST",
                url: "/results/",
                data: {
                    tags: $("#search").val(),
                    oldsearch: $("#tags").val(),
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken").val(),
                },
                success: searchSuccess,
                dataType: "html",
            });
        }, 2000)
    ); // 2 seconds delay after after typing
});

function searchSuccess(data, textStatus, jqXHR) {
    $("#dynamic").html(data);
}
