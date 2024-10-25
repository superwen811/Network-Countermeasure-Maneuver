<?php
if(isset($_POST['url'])) {
    $content = filr_get_contents($_POST['url']);
    $filename = "./images/".rand().".jpg";
    file_put_contents($filename, $content);
    echo $_POST['url'];
    $img = "<img src=\"".$filename."\"/>";
}
echo $img;
?>