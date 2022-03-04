-- https://programmers.co.kr/learn/courses/30/lessons/59040
-- GROUP BY 문법 기초 문제

SELECT ANIMAL_TYPE, COUNT(*)
  FROM ANIMAL_INS
  GROUP BY ANIMAL_TYPE
  ORDER BY ANIMAL_TYPE
