-- https://programmers.co.kr/learn/courses/30/lessons/59412
-- 다중 조건 HAVING 문법 문제

SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
  FROM ANIMAL_OUTS
  GROUP BY HOUR
  HAVING HOUR > 8 AND HOUR < 20 
  ORDER BY HOUR
