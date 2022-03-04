-- https://programmers.co.kr/learn/courses/30/lessons/59037
-- WHERE에서 값 비교시 NOT EQUAL(!=) 사용하는 문제

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != "Aged" ORDER BY ANIMAL_ID
