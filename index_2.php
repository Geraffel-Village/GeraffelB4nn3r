
<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Geraffelindex</title>

</head><body style="color: rgb(51, 51, 51); background-color: black; height: 331px;" alink="#000099" link="#000099" vlink="#460046">

<div style="text-align: center;"><span style="text-decoration: underline;">LED-Garaffelbanner V2-Webinterface</span><br></div>
<br>
<hr style="width: 100%; height: 2px;"><br><div style="text-align: center;"><img style="width: 571px; height: 66px;" alt="www.geraffel-village.de" title="www.geraffel-village.de" src="Geraffel.png">



<p>
<form action="index.php" method ="post">
<input type="Submit" name="set_led1" value="Led 1">
<input type="Submit" name="set_led2" value="Led 2">
<input type="Submit" name="set_led3" value="Led 3">
<input type="Submit" name="set_led4" value="Led 4">
<input type="Submit" name="set_led5" value="Led 5">
<input type="Submit" name="set_led6" value="Led 6">
<input type="Submit" name="set_led7" value="Led 7">
<input type="Submit" name="set_led8" value="Led 8">
</form>

<?php
if (isset($_REQUEST['set_led1']))
	{
	shell_exec("/var/www/pattern/ledmuster_1.sh");
	}
if (isset($_REQUEST['set_led2']))
	{
	shell_exec("/var/www/pattern/ledmuster_2.sh");
	}
if (isset($_REQUEST['set_led3']))
	{
	shell_exec("/var/www/pattern/ledmuster_3.sh");
	}
if (isset($_REQUEST['set_led4']))
	{
	shell_exec("/var/www/pattern/ledmuster_4.sh");
	}
if (isset($_REQUEST['set_led5']))
	{
	shell_exec("/var/www/pattern/ledmuster_5.sh");
	}
if (isset($_REQUEST['set_led6']))
	{
	exec('sudo python /var/www/pattern/./pattern1.py');
	}
if (isset($_REQUEST['set_led7']))
	{
	exec('sudo python /var/www/pattern/./Soft-PWM.py');
	}
if (isset($_REQUEST['set_led8']))
	{
	shell_exec("/var/www/lpattern/edmuster_8.sh");
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
