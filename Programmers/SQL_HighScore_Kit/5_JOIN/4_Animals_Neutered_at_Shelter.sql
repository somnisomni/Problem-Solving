-- https://programmers.co.kr/learn/courses/30/lessons/59045
-- RIGHT (OUTER) JOIN 문법 문제

-- 본 문제의 집합 수식 => ANIMAL_INS ∩ ANIMAL_OUTS ＋ ANIMAL_OUTS

SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME
  FROM ANIMAL_INS
  RIGHT OUTER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
  WHERE ANIMAL_INS.SEX_UPON_INTAKE != ANIMAL_OUTS.SEX_UPON_OUTCOME
  ORDER BY ANIMAL_OUTS.ANIMAL_ID
-- 중성화 여부는 SEX_UPON_INCOME -> SEX_UPON_OUTCOME 비교 시 값 자체가 달라지는 경우 중성화라고 판단합니다.
--   자연(Intact) 상태에서 중성화(Neutered/Spayed) 상태로 바뀔 수는 있어도, 중성화 상태에서 자연 상태로 바뀌는 경우는 없다고 가정하고,
--   성별이 바뀌는 경우 또한 없다고 가정한다면, 단순히 값 비교만으로 중성화 판단이 가능합니다.
