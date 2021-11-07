emps = [list(map(int, input().split())) for _ in range(3)]

for emp in emps:
  workSec = (emp[3] * 3600 + emp[4] * 60 + emp[5]) - (emp[0] * 3600 + emp[1] * 60 + emp[2])

  h = workSec // 3600
  workSec -= h * 3600
  m = workSec // 60
  workSec -= m * 60

  print("{} {} {}".format(h, m, workSec))
