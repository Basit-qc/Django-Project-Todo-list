$(document).ready(function(){
	
	$('#todotable').on('click', '.sendemail', function() {
		var tr = $(this).closest('tr');
        var summary = tr.find('td:eq(0)').text();
        var description = tr.find('td:eq(1)').text();
        var url = tr.find('td:eq(2)').text();
		//alert(summary +''+ description+ ' ' +url);
        $.get('/emailing/',{'summary':summary,'description':description,'url':url},function(data) {
    		//alert("successfully deleted");
    		alert("Email has been sent successfully");
        })
	});
	
	
	$('#todotable').on('click', '.deletetodo', function() {
		var tr = $(this).closest('tr');
        var summary = tr.find('td:eq(0)').text();
        var description = tr.find('td:eq(1)').text();
        var url = tr.find('td:eq(2)').text();
		//alert(summary +''+ description+ ' ' +url);
        $.get('/deletetodo/',{'summary':summary,'description':description,'url':url},function(data) {
        		//alert("successfully deleted");
        		location.reload();
        })
	});
	
	
	
});