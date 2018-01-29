<html>
<head>
	<title>Giorgi</title>
	<link rel="stylesheet" href="static/tether.min.css">
	<link rel="stylesheet" href="static/bootstrap.min.css">

<style>
.holder {
	border: 1px #000 dashed;
}
.maze {
	text-align: center;
	/*width:30%;*/
}
.my-col {
	float:left;
}
</style>
</head>
<body>
	<center>
	<div class="holder">
	  <div id="maze" class="maze"></div>
	</div>
	<center>
	

<script src="static/jquery.min.js"></script>
<script src="static/tether.min.js"></script>
<script src="static/bootstrap.min.js"></script>
<script>

	var map = {{ !list }};

	for(i = 0; i < map.length; i++)
	{
		$("#maze").append('<div id="row-'+i+'"></div>');

		$("#row-"+i).addClass("my-row");

		for(j = 0; j < map[i].length; j++)
		{

			$("#row-"+i).append("<div id='col-"+i+"-"+j+"' class='my-col'></div>")

			// make every box same height
			// $("#col-"+i+"-"+j).css("height",$(".row").width()/map[i].length);


			if(map[i][j] == "%"){
				map[i][j] = "#2c3e50";
			}
			else if (map[i][j] == "P"){
				map[i][j] = "#2980b9";
			}
			else if (map[i][j] == "."){
				map[i][j] = "#f1c40f";
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
	
</script>
</body>
</html>