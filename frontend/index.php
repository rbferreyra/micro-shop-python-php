<html>
    <head>
        <title>Micro Shop</title>
    </head>

    <body>
        <h1>Micro shop</h1>
        <ul>
            <?php
                $json = file_get_contents('http://backend');
                $obj = json_decode($json);
                $products = $obj->products;

                foreach ($products as $product) {
                    echo "<li>" . $product . "</li>";
                }
            ?>
        </ul>
    </body>
</html>