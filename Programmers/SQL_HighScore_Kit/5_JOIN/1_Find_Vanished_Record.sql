-- https://programmers.co.kr/learn/courses/30/lessons/59042
-- LEFT (OUTER) JOIN 문법 문제

-- 본 문제의 집합 수식 => ANIMAL_OUTS － ANIMAL_INS (ANIMAL_OUTS에 대한 ANIMAL_INS의 차집합)

SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
  FROM ANIMAL_OUTS
  LEFT OUTER JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
  WHERE ANIMAL_INS.ANIMAL_ID IS NULL
  ORDER BY ANIMAL_ID
