s = ''
protein = ''

for i in range(0, len(s), 3):
    aa = s[i] + s[i+1] + s[i+2]
    if aa == 'UUU' or aa == 'UUC':
        protein += 'F'
    elif aa == 'UUA' or aa == 'UUG' or aa == 'CUU' or aa == 'CUC' or aa == 'CUA' or aa == 'CUG':
        protein += 'L'
    elif aa == 'UCU' or aa == 'UCC' or aa == 'UCA' or aa == 'UCG' or aa == 'AGU' or aa == 'AGC':
        protein += 'S'
    elif aa == 'UAU' or aa == 'UAC':
        protein += 'Y'
    elif aa == 'UAA' or aa == 'UAG' or aa == 'UGA':
        break
    elif aa == 'UGU' or aa == 'UGC':
        protein += 'C'
    elif aa == 'UGG':
        protein += 'W'
    elif aa == 'CCU' or aa == 'CCC' or aa == 'CCA' or aa == 'CCG':
        protein += 'P'
    elif aa == 'CAU' or aa == 'CAC':
        protein += 'H'
    elif aa == 'CAA' or aa == 'CAG':
        protein += 'Q'
    elif aa == 'CGU' or aa == 'CGC' or aa == 'CGA' or aa == 'CGG' or aa == 'AGA' or aa == 'AGG':
        protein += 'R'
    elif aa == 'AUU' or aa == 'AUC' or aa == 'AUA':
        protein += 'I'
    elif aa == 'AUG':
        protein += 'M'
    elif aa == 'ACU' or aa == 'ACC' or aa == 'ACA' or aa == 'ACG':
        protein += 'T'
    elif aa == 'AAU' or aa == 'AAC':
        protein += 'N'
    elif aa == 'AAA' or aa == 'AAG':
        protein += 'K'
    elif aa == 'GUU' or aa == 'GUC' or aa == 'GUA' or aa == 'GUG':
        protein += 'V'
    elif aa == 'GCU' or aa == 'GCC' or aa == 'GCA' or aa == 'GCG':
        protein += 'A'
    elif aa == 'GAU' or aa == 'GAC':
        protein += 'D'
    elif aa == 'GAA' or aa == 'GAG':
        protein += 'E'
    elif aa == 'GGU' or aa == 'GGC' or aa == 'GGA' or aa == 'GGG':
        protein += 'G'

print(protein)
