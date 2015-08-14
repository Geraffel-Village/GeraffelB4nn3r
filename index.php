<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>Geraffel-Banner</title>
<meta content="Mic" name="author"><meta content="Geraffelbanner-Homepage" name="description"></head>


<body style="color: rgb(204, 204, 204); background-color: rgb(51, 51, 51); background-image: url(wallpaper-cf2-1680x1050.png);" alink="#000099" link="#000099" vlink="#990099">

<div style="text-align: center;"><big><span style="text-decoration: underline;">LED-Garaffelbanner
V2-Webinterface</span></big><br>

<div style="text-align: left;"></div>

<hr style="width: 100%; height: 2px;"><br><div style="text-align: center;">

<img style="width: 671px; height: 86px;" alt="www.geraffel-village.de" title="www.geraffel-village.de" src="Geraffel.png">
<a href="mailto:RasPirates@beernary-counter.de"><img style="width: 185px; height: 191px; float: right;" alt="Geraffel-Raspirates" src="Raspirates_transparent.png"></a>


<p>
<form action="index.php" method ="post">
<input type="Submit" name="pattern1" value="Old-School" style="width: 130px">
<input type="Submit" name="pattern2" value="Quad-Walk" style="width: 130px">
<input type="Submit" name="pattern3" value="Meet Me" style="width: 130px">
<input type="Submit" name="pattern4" value="Meet & Follow" style="width: 130px">
<input type="Submit" name="pattern5" value="Fill it up" style="width: 130px">
<input type="Submit" name="pattern6" value="Dimm-Bar" style="width: 130px">
<input type="Submit" name="pattern7" value="Led  7" style="width: 130px">
<input type="Submit" name="pattern8" value="Quicky" style="width: 130px">
</form>
<p>
<form action="index.php" method ="post">
<input type="Submit" name="pattern9" value="Random" style="width: 130px">
<input type="Submit" name="pattern10" value="Led 10" style="width: 130px">
<input type="Submit" name="pattern11" value="Led 11" style="width: 130px">
<input type="Submit" name="pattern12" value="Led 12" style="width: 130px">
<input type="Submit" name="pattern13" value="Led 13" style="width: 130px">
<input type="Submit" name="pattern14" value="Led 14" style="width: 130px">
<input type="Submit" name="pattern15" value="Led 15" style="width: 130px">
<input type="Submit" name="pattern16" value="Led 16" style="width: 130px">
</form>

<?php
if (isset($_REQUEST['pattern1']))
	{
	shell_exec("/var/www/pattern/ledmuster_1.sh");
	}
if (isset($_REQUEST['pattern2']))
	{
	shell_exec("/var/www/pattern/ledmuster_2.sh");
	}
if (isset($_REQUEST['pattern3']))
	{
	shell_exec("/var/www/pattern/ledmuster_3.sh");
	}
if (isset($_REQUEST['pattern4']))
	{
	shell_exec("/var/www/pattern/ledmuster_4.sh");
	}
if (isset($_REQUEST['pattern5']))
	{
	shell_exec("/var/www/pattern/Fillemup.sh");
	}
if (isset($_REQUEST['pattern6']))
	{
	exec('sudo python /var/www/./pattern1.py');
	}
if (isset($_REQUEST['pattern7']))
	{
	exec('sudo python /var/www/pattern/./Soft-PWM.py');
	}
if (isset($_REQUEST['pattern8']))
	{
	exec('sudo python /var/www/./quicky.py');
	}
if (isset($_REQUEST['pattern9']))
	{
	exec('sudo python /var/www/./randompattern.py');
	}
?>






<!-- 
So schaut der Aufruf des LED-Test-Musters aus php aus

#<?php
#shell_exec("/var/www/led.sh");
#?>

-->

</body>
</html>
