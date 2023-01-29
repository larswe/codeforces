# Stand-up Comedian
# Tags: greedy, math
# Verdict: Accepted, 202 ms, 0 KB

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    mood = [0, 0]
    
    # first tell all good jokes
    mood[0] += a[0]
    mood[1] += a[0]
    total = a[0]

    if a[0] > 0:
        # alternate jokes that A/B likes, until one category is exhausted.
        safe_semi = min(a[1], a[2])
        a[1] -= safe_semi
        a[2] -= safe_semi
        total += 2 * safe_semi

        # then tell the remaining semi-good jokes if possible
        rem_semi_A = min(mood[0], a[2])
        mood[0] -= rem_semi_A
        mood[1] += rem_semi_A
        a[2] -= rem_semi_A
        total += rem_semi_A

        rem_semi_B = min(mood[1], a[1])
        mood[1] -= rem_semi_B
        mood[0] += rem_semi_B
        a[1] -= rem_semi_B
        total += rem_semi_B

        # then tell as many bad jokes as possible
        rem_bad = min(mood[0], mood[1], a[3])
        mood[0] -= rem_bad
        mood[1] -= rem_bad
        a[3] -= rem_bad
        total += rem_bad

    # if you have any jokes left, just tell one more to end the show
    if a[1] > 0 or a[2] > 0 or a[3] > 0:
        total += 1

    print(total)



    
    
