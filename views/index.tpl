<html>
<head>
	<title>Giorgi</title>
	<link rel="stylesheet" href="static/tether.min.css">
	<link rel="stylesheet" href="static/bootstrap.min.css">

<style>
.holder {
	/*border: 1px #000 dashed;*/
}
.my-col {
	float:left;
}
</style>
</head>
<body>

	<center>
		<button id="start" class="btn btn-success">Start</button><br><br>
	<div class="holder">
	  <div id="maze" class="maze"></div>
	</div>
	<center>
	

<script src="static/jquery.min.js"></script>
<script src="static/tether.min.js"></script>
<script src="static/bootstrap.min.js"></script>
<script src="static/jquery.color.min.js"></script>
<script>

	var map = {{ !start_list }};
	var path = {{ !path_list }};

	var mouse = [];
	var cheese = [];

	for(i = 0; i < map.length; i++)
	{
		$("#maze").append('<div id="row-'+i+'"></div>');

		$("#row-"+i).addClass("my-row");

		for(j = 0; j < map[i].length; j++)
		{

			$("#row-"+i).append("<div id='col-"+i+"-"+j+"' class='my-col'></div>");

			if(map[i][j] == "%"){
				map[i][j] = "#2c3e50";
			}
			else if (map[i][j] == "P"){
				map[i][j] = "#2980b9";
				mouse = [i, j];
			}
			else if (map[i][j] == "."){
				map[i][j] = "#e74c3c";
				cheese = [i, j];
			}
			else {
				map[i][j] = "#ecf0f1"
			}
			$("#col-"+i+"-"+j).css("background",map[i][j]);
		}
	}


	var col = map[0].length;
	var row = map.length;
	var ratio = col/row;

	// This might need some changes after template
	var scale = 0.7;
	var holder_width = $(document).width();
	var holder_height = $(document).height();

	if(col >= row){
		$(".holder").css("width", holder_width * scale);
		$(".holder").css("height", holder_width * scale / ratio);
	}
	else {
		$(".holder").css("width", holder_height * scale * ratio);
		$(".holder").css("height", holder_height * scale);
	}

	$(".my-col").css("width", $(".holder").width()/col);
	$(".my-col").css("height", $(".holder").height()/row);
	

	// draw mouse
	var mouse_height = $("#col-0-0").height();
	var cheese_height = mouse_height;
	var my_mouse = "<img src='static/img/mouse.png' class='mouse' height='"+mouse_height+"'>";
	var my_cheese = "<img src='static/img/cheese.png' height='"+cheese_height+"'>";

	$("#col-"+mouse[0]+"-"+mouse[1]).append(my_mouse);
	$("#col-"+cheese[0]+"-"+cheese[1]).append(my_cheese);

	$("#start").click(function(){
		for(i = 0; i < path.length; i++)
		{
			var x = path[i][0],y = path[i][1];

			$("#col-"+x+"-"+y).animate({ 
				backgroundColor: "#7f8c8d",
				},i*200, function () {
				// After Animation 
			  	$(this).append(my_mouse);
			});
		}
	});


</script>
</body>
</html>