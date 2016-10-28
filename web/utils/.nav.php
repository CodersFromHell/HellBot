<?php
if(empty($active)){
    $active = -1;
}
?>

<nav id="navigation">
        <div class="background"></div>
        <ul class="nav">
            <li class="no-link"><a class="heading">Hell Bot</a></li>
            <li class=" <?php if($active == -1) echo 'active' ?>"><a href="">Home</a></li>
            <li><a href="levels.php">Levels</a></li>
            <li><a href="">FAQ</a></li>
            <li><a href="">Contact</a></li>
        </ul>
        <link rel="stylesheet" type="text/css" href="/css/.nav.css">
    </nav>