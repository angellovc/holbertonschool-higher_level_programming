-- displays the top 3 of cities temperature during July and August
-- database used was https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month
BETWEEN 7 AND 8
GROUP BY city
ORDER BY AVG(value) DESC LIMIT 3;
