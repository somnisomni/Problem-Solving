def solve(x1, y1, r1, x2, y2, r2):
    # Calculate center-to-center distance using Pythagorian Theorem
    #   SQRT((X1 - X2) ^ 2 + (Y1 - Y2) ^ 2)
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)

    if distance == 0:   # CASE: center point of circle is in exactly same position
        if r1 == r2:    # ... and radius is same
            return -1   # ...... then infinity point found
        else:           # ... and radius is different
            return 0    # ...... then no points found
    elif abs(r1 - r2) == distance:      # CASE: inner circle inscribed to outer circle
        return 1                        # ... then one point found
    elif abs(r1 - r2) > distance:       # CASE: inner circle NOT inscribed to outer circle
        return 0                        # ... then no points found
    elif r1 + r2 == distance:           # CASE: two circles circumscribed
        return 1                        # ... then one point found
    elif r1 + r2 < distance:            # CASE: two circles NOT circumscribed
        return 0                        # ... then no points found
    else:                               # OTHER CASES: two circles overlapped
        return 2                        # ... then two points found

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solve(x1, y1, r1, x2, y2, r2))
