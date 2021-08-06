
window.onload = function()
{
	console.log("Document Loaded")
	var url = "http://127.0.0.1:5000/get_location";
	$.get(url, function(data, status){
		if(data){
			var location = data.location;
			
			var uilocation = document.getElementById("uilocation")
			$('#uilocation').empty();
			for(var i in location){
				var opt = new Option(location[i]);
				$('#uilocation').append(opt);
			}
		}
	});
}

function getEstimatedPrice(){
	var bath = getBathroom();
	var bhk = getBHK();
	var balcony = getBalcony();
	var location = document.getElementById("uilocation").value;
	var sqft = getSqft();
	url = "http://127.0.0.1:5000/predict_price";
	
	$.post(url, {
		location : location,
		total_sqft: parseFloat(sqft),
		bath: bath,
		balcony: balcony,
		BHK: bhk
	}, function(data, status){
		var price = data.price;
		document.getElementById("EstimatedPrice").innerHTML = price + " Lac.";
		document.getElementById("desc").innerHTML = "This is just an estimated price. Original price may br higher or lower.";
	});
}

function getBathroom(){
	var bath = document.getElementById("bathroom").value;
	
	return bath;
}

function getBHK(){
	var bhk = document.getElementById("bhk").value;
	
	return bhk;
}

function getBalcony(){
	var balcony = document.getElementById("balcony").value;
	
	return balcony;
}


function getSqft(){
	var Sqft = document.getElementById("sqft").value;
	
	return Sqft;
}

