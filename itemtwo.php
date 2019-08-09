<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="utf-8">
    <title></title>
</head>
<body>
<?php
$conn = new mysqli("localhost", "root", "", "storedb");
if ($conn->connect_errno) {
    echo "Database connection failed (" . $conn->connect_errno . ") " . $conn->connect_error;
}
if (!$conn->query("UPDATE items SET avail=avail-1 where id='2'")) {
    echo "Table creation failed: (" . $conn->errno . ") " . $conn->error;
}
?>
</body>
</html>
