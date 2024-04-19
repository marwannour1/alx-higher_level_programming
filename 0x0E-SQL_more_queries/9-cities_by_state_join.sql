-- qurey all cities

SELECT c.id, c.name, s.name
FROM cities AS c, states AS s
ORDER BY c.id ASC;
