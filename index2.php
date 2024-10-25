/<?php
function GetFile($host,$port,$link) {
    $fp = fsockopen($host, intval($port), $errno, $errstr, 30);
    if(!$fp) {
        echo "$errstr (error number $errno} \n";
    }
    else{
        $out = "GET $link HTTP/1.1\r\n";
        $out .= "Host: $host\r\n";
        $out .= "Connection:Close\r\n\r\n";
        $out .= "\r\n";
        fwrite($fp, $out);
        echo($out);
        $contents='';
        while(!feof($fp)) {
            $contents .=fgets($fp, 1024);
        }
        fclose($fp);
        return $contents;
    }
}
echo GetFile($_GET["host"], $_GET["port"], $_GET["link"]);
?>