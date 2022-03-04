-- https://programmers.co.kr/learn/courses/30/lessons/59410
-- IFNULL 함수 문제

-- MySQL 계열에선 IFNULL(), MSSQL에선 ISNULL(), Oracle에선 NVL() / 파라미터 순서는 동일 (칼럼명, NULL일 때 대체값)
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
  ORDER BY ANIMAL_ID
