// jQuery
$(document).ready( function () {
    $( function() {
        $( "#datepicker" ).datepicker({
          dateFormat: "yy-mm-dd"

        });
    });

});

jQuery(document).ready(function(){
  jQuery(function() {
        jQuery(this).bind("contextmenu", function(event) {
            event.preventDefault();
            alert('Right click disable in this site!!')
        });
    });
});









