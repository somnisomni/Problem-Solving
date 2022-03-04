-- https://programmers.co.kr/learn/courses/30/lessons/59408
-- DISTINCT 문법 문제

-- COUNT 함수는 행의 지정된 열의 값이 NULL인 경우는 세지 않음
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
