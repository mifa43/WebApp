function hashTag(){
    function tagError(){
        console.log("Tag is in wrong format. Add whatever logic is needed here, whether toggling of a field validation element, or an alert, etc.");
    };
      
      function generateHiddenInput(){
        var tags = "";
        var tagCount = 0, tagMax = 5; //MODIFY MAX COUNT TO YOUR LIKING
        $("#tagList li").each(function(i){
          tags += $(this).attr("data-htag") + " ";
          tagCount++;
        });
        $("#tags").val(tags.trim());
        console.log("Current val of tags is '" + $("#tags").val() + "'");
        return tagCount <= tagMax;
      };
      
    function addToHashtagList(tag){
        $("#tagList").append("<li data-htag='" + tag + "'><a href='#' title='Remove Tag' id='tagValue1'>#" + tag + "</a></li>");
        if (!generateHiddenInput()){
          alert("Too many. Add whatever logic is needed here, whether toggling of a field validation element, or an alert, etc.");
          $("#tagList").children().last().remove();
          generateHiddenInput();
        }
      };
      
    $("#tagInput").keypress(function(e) {
        var key = (e.keyCode || e.which);
        if(key != 32 && key != 13)
          return;
        var rgxHashtag = /^#?([a-zA-Z\d]{3,12})$/;
        var inString = $("#tagInput").val().trim();
        if(!rgxHashtag.test(inString)){
          tagError();
          return;
        }
        var tagToAdd = rgxHashtag.exec(inString)[1];
        if($("#tagList li[data-htag='" + tagToAdd + "']").length > 0){
          return false; //Tag already existed.
        }
        addToHashtagList(tagToAdd);
        $("#tagInput").val("");
        return false;
      });
      
    $("#tagList").on("click", "li", function(){
        var tagName = $(this).attr("data-htag");
        $(this).remove();
        generateHiddenInput();
    });
}

