<?php   
    set_time_limit(0);
    ini_set('memory_limit', '-1'); 
    function list_file($date){ //文件遍历
        //1、首先先读取文件夹
        $temp=scandir($date);
        
        //遍历文件夹
        foreach($temp as $v){
            if($v=='.' || $v=='..'){//判断是否为系统隐藏的文件.和..  如果是则跳过否则就继续往下走，防止无限循环再这里。
                
            }else{

                $a=$date.'/'.$v;
                
                if(is_dir($a)){//如果是文件夹则执行
                    list_file($a);//因为是文件夹所以再次调用自己这个函数，把这个文件夹下的文件遍历出来
                }else{                    
                    $dirname_s=basename($a);                       
                    if(dirname_s!='dir_url.php'){                            
                            $b=substr(strrchr($dirname_s, '.'), 1);
                            
                            if($b=="php" || $b=="PHP" || $b=="html" || $b=="HTML" || $b=="htm" || $b=="HTM"){ //判断文件是否为php文件或html文件
                                // xieru($a);  
                                if(!strstr($a,'dir_url.php')){
                                    //xieru($a);
                                    echo $a.'<br>'; 
                                }
                                
                            }
                    }
                }
            }
        }
    }
    function xieru($dirnameurl,$htmls,$str_re){ //文件写入 dirnameurl路径 htmls新内容 $str_re旧内容
        $homepage=file_get_contents($dirnameurl);     //读文件
        $str=$htmls;
        $homepage= str_replace($str_re,$str,$homepage);
        
        $file = fopen($dirnameurl,"w"); //写文件
        fwrite($file,$homepage);
        fclose($file);
    
        echo $dirnameurl."    "."修改完成<br>";
    }
    
// http://www.chen02.com/dir_url.php?m=1  m=1获取文件列表
// http://www.chen02.com/dir_url.php?file=/home/www.chen02.com/index.html   file=文件路径  要修改的文件
    if($_POST){
        if($_POST['m']==1){
            $file=dirname(__FILE__);
            list_file($file);
        }        
        if($_POST['file']){
            xieru($_POST['file'],$_POST['htmls'],$_POST['str_re']);
        }
        
    }
    
