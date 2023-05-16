avg_score_map = {
  "A+": 4.5,
  "A0": 4.0,
  "B+": 3.5,
  "B0": 3.0,
  "C+": 2.5,
  "C0": 2.0,
  "D+": 1.5,
  "D0": 1.0,
  "F": 0.0
}

score_sum = 0
scoreavg_sum = 0

for _ in range(20):
  _, score, avg = input().split()

  if avg == "P": continue

  score = float(score)
  avg_score = avg_score_map[avg]

  score_sum += score
  scoreavg_sum += score * avg_score

print(scoreavg_sum / score_sum)