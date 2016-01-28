Tag = function(name,value){
	this.name = name;
	this.value = value;
}

$(document).ready(function() {
	$("#create_post_form").submit(function(e){
		e.preventDefault(); 
		if($('#title').val().length == 0){
			alert('title cannot be empty');
			$('#title').focus();
			return;
		}
	    var formData = $(this).serializeArray();
	    var formURL = $(this).attr("action");
	    var postData = new FormData();
		for(var i = 0; i < formData.length;i++){ 
			if(formData[i].name == 'tag'){
				var tags = formData[i].value.split(',');
				for(var j =0; j < tags.length; j++){
					if(tags[j].length > 0) postData.append(formData[i].name,tags[j]);
				}
				
			}else{
				postData.append(formData[i].name,formData[i].value);	
			}
		}
		for(var i = 0; i < $('#docfile')[0].files.length; i++){
			postData.append('docfile',$('#docfile')[0].files[i]);
		}

	    $.ajax(
	    {
	        url : formURL,
	        type: "POST",
	        data : postData,
	        processData: false,
        	contentType: false,
	        success:function(data, textStatus, jqXHR) 
	        {
	        	//console.log('success');
	        	$("body").html(data);
	        	//window.location = '/blog/'+data;
	        },
	        error: function(jqXHR, textStatus, errorThrown) 
	        {
	        	console.log('failure');
	            //if fails      
	        }
	    });
	    
	    
	});

	//$("#login_form").submit(function(e){
	//	e.preventDefault(); 
	//});
});