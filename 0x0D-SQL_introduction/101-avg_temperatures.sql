-- average tempreture

SELECT city, AVG(value) as avg_temp
FROM tempretures
GROUP BY city
ORDER BY value DESC;
