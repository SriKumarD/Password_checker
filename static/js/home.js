$(document).on('click','#on',(e) =>
{
    $("#myForm").submit((e) => {
        e.preventDefault(); // prevent actual form submit
        var form = $(this);
    
        var url = form.attr('action'); //get submit url [replace url here if desired]
        $.ajax({
             type: "POST",
             url: url,
             data: form.serialize(),
             success: function (resData) {
         				
                console.log(resData)
            } 
        });      
    });
});
