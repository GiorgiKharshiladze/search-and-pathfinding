<html>
<head>
	<title>Giorgi</title>
</head>
<body>

	<div id="maze"></div>
	
<script>
	var map = [];
	var map = {{ !list }};

	for(i = 0; i < map.length; i++)
	{
		var row = document.createElement("div");
		document.getElementById("maze").appendChild(row);
		row = row.setAttribute("id", "row-"+i);
		document.getElementById("row-"+i).className = "row-class";

		for(j = 0; j < map[i].length; j++)
		{
			var col = document.createElement("div");
			document.getElementById("row-"+i).appendChild(col);
			col.setAttribute("id", "col-"+j);
			box = document.getElementById("col-"+j);
			box.className = "col-class";
			box.appendChild(document.createTextNode(map[i][j]));
		}
	}
	
</script>
</body>
</html>