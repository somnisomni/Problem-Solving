-- https://programmers.co.kr/learn/courses/30/lessons/59038
-- MIN 함수 문제

-- 아래는 MIN 함수를 쓰지 않고 정렬(ORDER BY)+한정(LIMIT)만으로 비슷한 효과를 내는 쿼리 예시
--   SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1

-- 아래는 문제에서 의도했을 답
SELECT MIN(DATETIME) FROM ANIMAL_INS
