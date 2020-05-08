<!DOCTYPE html>

<head>
    <link rel = "stylesheet" type = "text/css" href ="style.css"> 
    <link rel = "stylesheet" type = "text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title> Task Manager </title>
</head>
<html>
<body>
<center>
    <h4>
    This is data
    </h4>
    <form method = "post">
        <input type = "text" value = "ID"placeholder = "Enter id"><br/><br/>
        <input type = "text" value = "Name"placeholder = "Task Name"><br/><br/>
        <input type = "text" value = "descript"placeholder = "Description"><br/><br/>
        <input type = "text" value = "due_date"placeholder = "Dude Date"><br/><br/>
        <button type = "submit" class = "btn btn-outline-light" name ='submit1'> Add </button>
        <button type = "submit" class = "btn btn-outline-light" name ='submit2'> View </button>
    </form>
</center>
</body>
</html>

<?php
function database(){
    $mysqli -> query("INSERT INTO Task (Enter id, Task_Name, descript, due_date) VALUES ($_POST['ID'], $_POST["Name"], $_POST['descript'], $_POST['due_date'])");

// Print auto-generated id
echo "New record has id: " . $mysqli -> insert_id;
}

function reload(){

    if ($result = $mysqli -> query("SELECT * FROM Task")) {
        echo "Returned rows are: " . $result -> num_rows;
        // Free result set
        $result -> free_result();
      }
      
      $mysqli -> close();
}

$mysqli = new mysqli("localhost","hezz","1234567","task_db");

// Check connection
        if ($mysqli -> connect_errno) {
        echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
        exit();
    }
if(isset($_POST['submit1']))
{
    database();
}
else
{
    reload();
}

?>
