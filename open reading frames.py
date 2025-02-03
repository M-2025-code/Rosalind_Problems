def translation(dna, protein, start):
    for i in range(start, len(dna), 3):
        if i + 2 == (len(dna) - 1): #these following if statements are checking if its at the end of the string or not because if it is then that reading frame wouldnt be valid as there may be no stop codon present
            protein = ''
            return protein, i
        if i >= (len(dna) - 4):
            protein = ''
            return protein, i
        aa = dna[i] + dna[i + 1] + dna[i + 2]
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

    return protein, i

def transcription(dna):
    x = 0
    for i in dna:
        if i == 'T':
            dna = dna[:x] + 'U' + dna[x + 1:]  # technically the dna is rna
        x += 1

    return dna


rf = []

dna1 = 'GGCCTTTAAGCGAGAAGCGGAGCTACACCGGGCGTGCCCCGTAGGCCGCCTGAAATCGTCTAATGAATCTACAGCGTTGACACTAGGATTCGGTTGCGAGCCCCAGGATCTGCGCTCACCTGCAGTCCAGCCTCGGGGTATTCGGTAAGGGAGACTTGTCCATAGACATGACGAGTCCGCAACTCCACATATACAAAGAGAGGCTTTGAGTTTGTTTGTTCGCACGTAGCGGGAATAAAGCATAGATGCTCCTCTAGGAATATGCGGCGACTAGCGCAGACTGTAGCGTGGCGATGCCCCGTGATACAGAAAGGGCGAGCCGTACGGCCGGCGCTTTCTCGCACACAAGAATAGCAATTAAATGCCTCTAGGGCTATTCGGCGCCGGGTAACCCTAATAAGACGAATTCCTACATTACAATCGTCTGCCCCGAGTCACACAATCGTAACAGGCTGGACGAGCATGATCCCAAACATTGCGCGACGTTAGCTAACGTCGCGCAATGTTTGGGATCATATTAGTAAAAATGGCCTTGTTACAAAGTAGTCAAGCGGAGAATATTCCTCTCCTCATCGCATGAGGGCTGGAATCTCCTATGCGAACCGACTTTGGGTGTTTGTGGAGAATCGGACCTACGTGCCGCTGTGGGTGCGACAGCTCGTCGACCTCAGGAAGCGTCTGTTACTTATGGGTTTGAGTCGAGGACAGACTCGTGCCCTAGGATATGCTAAGTTGGAGGGATACTTTAACCGGTGTTAACTACCTCGATCGGTAAAAAGTCTGCCGAGTGCTATCCCGCAATCGGCCAAAAGCCAAGATAGATTCCGGTTGCAGTGCGATGATATTCCTTGGGGTGATTTTTAATTTACGCGAGCTTAAGTCAAAGGCGTTGAACGAGACATAGCGCTTTAGAACCACAACTTAGCCATGTTCTTTGCAATCGAGCCTGCGCTCCTTTAATGGTAACTACTTACGAGA'
rna1 = transcription(dna1)
protein0 = ''

proteins1 = []
x = 0
for i in range(0,3): #determining reading frames
    while x == 0: #following is getting all sequences along the whole reading frame
        protein1 = translation(rna1, protein0, i) #will return tuple (string, i being the pos)
        proteins1.append(protein1[0]) #just adding all sequences to the same array
        if protein1[1] >= (len(rna1) - 4):
            break
        i = protein1[1] + 3 #the new starting position as the i returned is the start of the stop codon


for w in proteins1:  #going through array
    x = 0
    for y in w:
        if y == 'M':
            w = w[x:] #want to keep from M to the end
            if w not in rf: #didnt know you can do this assuming you can
                rf.append(w)
            x = 0
        x += 1

#creating complementary strand - then need to reverse so that it is being read in the correct direction due to directionality

dna2 = '' #creating complementary strand
for i in dna1:
    if i == 'A':
        dna2 += 'T'
    elif i == 'T':
        dna2 += 'A'
    elif i == 'C':
        dna2 += 'G'
    elif i == 'G':
        dna2 += 'C'


dnarev = dna2[::-1]
rna2 = transcription(dnarev) #reversing so its in correct direction

proteins2 = [] #repetitive code so could make it into a function
x = 0
for i in range(0,3):
    while x == 0:
        protein2 = translation(rna2, protein0, i)
        proteins2.append(protein2[0])
        if protein2[1] >= (len(rna2) - 4):
            break
        i = protein2[1] + 3

for w in proteins2:
    x = 0
    for y in w:
        if y == 'M':
            w = w[x:]
            if w not in rf:
                rf.append(w)
            x = 0
        x += 1


for frame in rf:
    print(frame)



