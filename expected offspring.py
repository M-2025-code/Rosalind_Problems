prob = [1, 1, 1, 0.75, 0.5, 0]
pairs = [19756, 16249, 19711, 17419, 19041, 16309]
x = 0
total = 0
for i in pairs:
    if i != 0:
        total += (i * 2) * prob[x]
    x += 1

print(total)