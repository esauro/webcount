
$("#main_form").submit(function(e) {
    e.preventDefault();
    $.post("/api/", {"site": $("#site").val()}, function(data) {
        var obj = jQuery.parseJSON(data);
        var wordcloud = $("#wordcloud");
        for (word in obj) {
            var span = $('<span />').attr('data-weight', obj[word][1]).html(obj[word][0]);
            wordcloud.append(span);
        }
        wordcloud.awesomeCloud({
            "size" : {
                "grid" : 1,
                "normalize" : true,
                "factor": 0
            },
            "options" : {
                "color" : "random-dark",
                "rotationRatio" : 0.35,
                "printMultiplier" : 1,
                "sort" : "random"
            },
            "font" : "'Times New Roman', Times, serif",
            "shape" : "circle"
        });


    });
});
