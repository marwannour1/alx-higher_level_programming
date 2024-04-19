-- qurey all cities

SELECT c.id, c.name, s.name
FROM cities AS c JOIN states as s ON c.state_id = s.id
ORDER BY c.id ASC;
