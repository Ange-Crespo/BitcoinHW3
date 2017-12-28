//REQUIRE JQUERY !
function getCSRFTokenValue() {
    var key= jQuery("[name=csrfmiddlewaretoken]").val();
    console.log( "CSRF COOKIE from buyAndSell/main.js :" +key);
    return key;
};

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};
    function create_post(comd) {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
            console.log(!csrfSafeMethod(settings.type) && !this.crossDomain);
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCSRFTokenValue());
                    console.log("we are in");
                }
            }
        });
    console.log("create post is working!") // sanity check
    console.log(window.location.origin+"/buyAndSell/create_post/");
    $.ajax({
        url : window.location.origin+"/buyAndSell/create_post/", // the endpoint
        type : "POST", // http method
        data : { limit: $('#Limit').val(), price : $('#price').val(), amount :$('#amount').val(),cmd : comd}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#Limit').val(''); // remove the value from the input
            $('#price').val('');
            $('#amount').val('');
            
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            
            console.log('http://{domain}'+$('#URL_buyAndSellForm').val());
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            console.log(getCSRFTokenValue());
        }
        });
        };
        var comd="bid";       
        $('#bid').mouseover(function(event){

            comd="ask";
            console.log("cmd : "+comd);
        });

        $('#ask').mouseover(function(event){
            
            comd="bid";
            console.log("cmd : "+comd);
        });
        $('#form1').on('submit', function(event){
            event.preventDefault();
            console.log("form submitted!")  // sanity check
            console.log(comd);
            create_post(comd);
        });