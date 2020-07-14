-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- database used was https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT city, AVG(value) AS average FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;