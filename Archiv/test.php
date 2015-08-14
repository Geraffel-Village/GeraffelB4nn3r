<?php
echo ("Dies ist ein Test");
$output = shell_exec('ls -larc');
echo "<pre>$output</pre>";
shell_exec('sh led.sh'); 
?>
