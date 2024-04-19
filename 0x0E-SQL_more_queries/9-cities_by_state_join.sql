-- qurey all cities

SELECT c.id, c.name, s.name
FROM cities as c, states as s
ORDER BY c.id ASC;
