Tag = function(name,value){
	this.name = name;
	this.value = value;
}

$(document).ready(function() {
	$("#create_post_form").submit(function(e){
		e.preventDefault(); 
		
	    var formData = $(this).serializeArray();
	    var formURL = $(this).attr("action");
	    var postData = new FormData();
		for(var i = 0; i < formData.length;i++){ 
			//console.log("i:"+i+" data:"+formData[i].name);
			if(formData[i].name == 'tag'){
				var tags = formData[i].value.split(',');
				for(var j =0; j < tags.length; j++){
					postData.append(formData[i].name,tags[j]);
				}
				
			}else{
				postData.append(formData[i].name,formData[i].value);	
			}
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
	        	console.log('success');
	            //data: return data from server
	        },
	        error: function(jqXHR, textStatus, errorThrown) 
	        {
	        	console.log('failure');
	            //if fails      
	        }
	    });
	    
	    
	});

	$("#login_form").submit(function(e){
		e.preventDefault(); 
	});
});