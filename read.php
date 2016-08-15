<?php
$fp = fopen("rates.txt", "r");
if ($fp) {
    while (!feof($fp)) {
        $str = fgets($fp, 100);
        $data[] = str_replace("\r\n", "", $str);
    }
    fclose($fp);

    echo json_encode($data);
}
?>