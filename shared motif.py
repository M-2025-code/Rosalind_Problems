strands = []
s = open('rosalind_lcsm_4.txt', 'r')
strand = ''
for line in s:
    if '>' not in line:
        l = line.strip()
        strand += l
    else:
        strands.append(strand)
        strand = ''

def order(a):
    return len(a)

#go through and create potential substrings
#sort by doing strand.sort(reverse=True, key=order)
#go through and compare to each string - when first one is found break the loop and this is the longest motif

motifs = []
sub = ''
for i in range(0, len(strands[1])):
    if len(sub) > 2:
        sub = strands[1][i:]
        motifs.append(sub)

sub = ''
for x in strands[1]:
    if len(sub) > 2:
        sub += x
        motifs.append(sub)

for y in range(3, len(strands[1])):
    for k in range(0, len(strands[1])):
        sub = strands[1][k:k+y]
        motifs.append(sub)
        if (k+y) == len(strands[1]):
            break

motifs.sort(reverse=True, key=order)

for x in motifs:
    check = []
    for i in range(2, len(strands)):
        if x in strands[i]: #think if the letters are in there at all not sure if it means in this order
            check.append(1)
        else:
            check.append(0)
    if 0 not in check:
        print(x)
        break



