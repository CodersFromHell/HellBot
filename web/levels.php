<!DOCTYPE html>
<html lang=en>
<head>
    <link rel="stylesheet" type="text/css" href="/css/root.css">
    <link rel="icon" href="/img/favicon.ico">
    <link rel="apple-touch-icon" href="/img/favicon.jpg">
    <link rel="apple-touch-icon-precomposed" href="/img/favicon.jpg">
    <link rel="apple-touch-startup-image" href="/img/load.jpg">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</head>
<header>
    <?php
    $active = 1;
    include '/utils/.nav.php'
    ?>
</header>
<body>
<div id="level-list">
    <table>
        <tbody>
        <?php
        $json = json_decode(file_get_contents("conf/levels.json"), true);
        foreach($json as $user){
        $username = $user['name'];
        $xp = $user['xp'];
        $reXp = 50 + 5 * ($user['lvl'] - 1);
        $rank = 1;
        echo "
        <tr class='card'>
            <td>$username</td>
            <td>$xp XP</td>
            <td>-</td>
            <td>$reXp XP</td>
            <td>$rank</td>
        </tr>";
        }
        ?>
        </tbody>
    </table>
</div>
<script type="text/javascript">
    users = {};
    $.getJSON("conf/levels.json", function(json){
        keys = Object.keys(json)
        for(i = 0; i < keys.length; i++){
            users[i] = {};
            users[i]['id'] = keys[i];
            users[i]['xp'] = json[keys[i]]['xp'];
            users[i]['of'] = 50 + 5 * (json[keys[i]]['lvl'] - 1);
            users[i]['lvl'] = json[keys[i]]['lvl'];
            users[i]['name'] = json[keys[i]]['name'];
        }
        console.log(users)
    });

</script>
</body>
</html>