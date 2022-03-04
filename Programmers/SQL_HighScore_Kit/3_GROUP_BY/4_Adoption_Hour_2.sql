-- https://programmers.co.kr/learn/courses/30/lessons/59413
-- GROUP BY 카테고리에 속하는 문제이긴 한데, GROUP BY 잘 쓴다고 풀어지는 문제가 아닌 듯.
-- 다양한 풀이가 있지만 변수(SET)를 만들고 재귀하는 방식을 찾음

-- "HOUR_ITER"라는 변수를 만들고 -1 값 대입
-- 변수는 변수명 앞에 앳마크(@)를 붙여서 사용
SET @HOUR_ITER := -1;

-- 아래 SELECT에서 HOUR 칼럼은 WHERE의 조건에 의해 0 ~ 23의 값을 가지는 열을 만들어 낼 것임
-- 재귀가 돌 때마다, COUNT 칼럼에서 현재 HOUR_ITER 변수값과 HOUR(DATETIME)이 일치하는 열의 개수를 세어 남김
SELECT (@HOUR_ITER := @HOUR_ITER + 1) AS HOUR,
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR_ITER) AS COUNT
    FROM ANIMAL_OUTS
    WHERE @HOUR_ITER < 23
