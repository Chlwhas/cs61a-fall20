.read data.sql


CREATE TABLE bluedog AS
  		SELECT color, pet
		FROM students
		WHERE pet = "dog" AND color = "blue";

CREATE TABLE bluedog_songs AS
  		SELECT color, pet, song
		FROM students
		WHERE pet = "dog" AND color = "blue";


CREATE TABLE smallest_int AS
        SELECT time, smallest
        FROM students
        WHERE smallest > 2
        ORDER BY smallest
        LIMIT 20;


CREATE TABLE matchmaker AS
        SELECT s1.pet, s1.song, s1.color AS color1, s2.color AS color2
        FROM students AS s1
        INNER JOIN students AS s2
            ON s1.pet = s2.pet
            AND s1.song = s2.song
            AND s1.time < s2.time;


CREATE TABLE sevens AS
        SELECT s.seven
        FROM students AS s
        INNER JOIN numbers AS n
            ON s.time = n.time
        WHERE s.number = 7
            AND n.`7` = "True";

