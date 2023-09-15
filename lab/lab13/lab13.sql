.read data.sql


CREATE TABLE average_prices AS
    SELECT category, AVG(MSRP) AS average_price
    FROM products
    GROUP BY category;


CREATE TABLE lowest_prices AS
    SELECT i1.store, i1.item, i2.min_price
    FROM inventory AS i1
    INNER JOIN (
        SELECT item, MIN(price) AS min_price
        FROM inventory
        GROUP BY item
    ) AS i2
        ON i1.item = i2.item AND i1.price = i2.min_price;


CREATE TABLE shopping_list AS
    SELECT lp.item, lp.store
    FROM lowest_prices AS lp
    INNER JOIN (
        SELECT p1.category, p1.name, p1.value AS value
        FROM (
            SELECT category, name, ROUND(MSRP/rating, 6) AS value
            FROM products
        ) AS p1
        INNER JOIN (
            SELECT category, ROUND(MIN(MSRP/rating), 6) AS min_value
            FROM products
            GROUP BY category
        ) AS p2
            ON p1.category = p2.category AND p1.value = p2.min_value
    ) AS mr
        ON lp.item = mr.name;


CREATE TABLE total_bandwidth AS
    SELECT SUM(s.Mbs)
    FROM shopping_list AS sl
    INNER JOIN stores AS s
        ON sl.store = s.store;

