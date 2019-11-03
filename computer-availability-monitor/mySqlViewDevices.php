<html>

<!DOCTYPE html>
<html>
<head>
<title>Table with database</title>
<style>
/* TABLE FORMATTING */
table {
border-collapse: collapse;
width: 100%;
color: #588c7e;
font-family: monospace;
font-size: 25px;
text-align: left;
}
th {
background-color: #588c7e;
color: white;
}
tr:nth-child(even) {background-color: #f2f2f2}
</style>
</head>
<body>
<table>

<tr>
<!--  RECORDS BEING DISPLAYED -->
<td>Device Name</td>
<td>State</td>
<td>Current User</td>

</tr>
<?php

// Enter username and password - this must be populated with the information from the Database
$username = '';
$password = '';


// Create database connection using PHP Data Object (PDO)
$db = new PDO("mysql:host=localhost;dbname=devices", $username, $password);

// Identify name of table within database
$table = 'computers';

// Create the query - take everything from the table
$stmt = $db->query('SELECT * from '.$table);

// Close connection to database
$db = NULL;

// Specifiy which records you are displaying
while($rows = $stmt->fetch()){
echo "<tr><td>". $rows['name'] . "</td><td>" . $rows['state'] . "</td><td>" . $rows['currentuser'] . "</td></tr>";
};
?>
</table>
</body>
</html>
</html>