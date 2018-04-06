$(document).ready(function() {

    console.log("tesat");

    $("#hooliButton").click(function() {
        $.post( "/verify",
        {
            test: "123"
        },
        function( data ) {
            $( ".result" ).html( data );
        });
    });
});