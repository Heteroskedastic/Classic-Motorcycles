function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $("[name='btn-send-feedback']").click(function(){
        var feedback_text = $.trim($("#feedback").val());
        if(!feedback_text){
            //If feedback text area is empty, show error message
            $("#feedback-error").show();
            $("#feedback-status").html("Enter feedback text");
            $("#feedback").val("");
        }
        else{
            $.post("/search/feedback",{
                    feedback:$("#feedback").val()
                }).done(function(){
                    $('#collapseOne').collapse('hide');    
                    $('#collapseTwo').collapse('show');   
                }).fail(function(){
                    $("#feedback-error").show();
                    $("#feedback-status").html("Error while sending the feedback");
                });
        }
    });
});    