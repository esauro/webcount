
$("#main_form").submit(function(e) {
    e.preventDefault();  // Avoid page reloading
    $.post("/api/", {"site": $("#site").val()}, function(data) {
        var obj = jQuery.parseJSON(data);
        var wordcloud_div = $("#wordcloud");
        for (word in obj) {
            var span = $('<span />').attr('data-weight', obj[word][1]).html(obj[word][0]);
            wordcloud_div.append(span);
        }
        wordcloud_div.awesomeCloud({
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
