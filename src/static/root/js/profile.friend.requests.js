$(document).ready(function(){
	$("#addfriend").click(function(event){
		event.preventDefault();
		var request = $.ajax({
			method: "POST",
			url: "{{ profile.get_absolute_url }}",
			data: {
				csrfmiddlewaretoken: "{{ csrf_token }}",
			}
		})
		$('#addfriend').hide();
		$("#cancelrequest").removeClass("hidden");
		request.done(function(data){
			console.log("working")
		})
	})

})