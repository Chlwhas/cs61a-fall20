CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
    SELECT name, size
    FROM dogs
    INNER JOIN sizes
	    ON height > min AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
    SELECT d1.name
    FROM dogs AS d1
    INNER JOIN parents AS p
	    ON p.child = d1.name
    INNER JOIN dogs AS d2
	    ON p.parent = d2.name
    ORDER BY d2.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
    SELECT d.name AS first, p2.child AS second
    FROM dogs AS d
    INNER JOIN parents AS p1
        ON p1.child = d.name
    INNER JOIN parents AS p2
        ON p2.parent = p1.parent
        AND p2.child != d.name
    WHERE d.name < p2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
    SELECT "The two siblings, " || s.first || " plus " || s.second || " have the same size: " || sod1.size AS result
    FROM siblings AS s
    INNER JOIN size_of_dogs AS sod1
        ON s.first = sod1.name
    INNER JOIN size_of_dogs AS sod2
        ON s.second = sod2.name
        WHERE sod1.size = sod2.size;

