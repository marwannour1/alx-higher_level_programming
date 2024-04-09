-- average tempreture

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
HAVING month = 7 OR month = 8
ORDER BY avg_temp DESC
LIMIT 3;
