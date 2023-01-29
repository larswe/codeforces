# GamingForces
# Tags: greedy, sortings

t = int(input())

for _ in range(t):
    n = int(input())
    
    h = list(map(int, input().split()))

    h_sorted = sorted(h)

    min_spells = n

    spells_needed_to_kill_z = [0] * (n + 1)

    for i in range(n):
        spells_needed_to_kill_z[i + 1] = spells_needed_to_kill_z[i] + h_sorted[i]
        if i + 1 < n:
            h_sorted[i + 1] -= h_sorted[i]

    spells_if_z_killed = [n] * (n + 1)

    for i in range(n):
        spells_if_z_killed[i + 1] = spells_needed_to_kill_z[i + 1] + n - i - 1

    print(min(spells_if_z_killed))