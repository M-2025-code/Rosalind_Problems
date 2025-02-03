string = 'ATATTCCCGCACACTATCTGCGCCAGGAGAGCCGTGATTACATTGACAAACTTGGGCGGATTATTGATCCCTTAAATTCGTGCGTGGACTGGAAGAGTTAAGCTTTATCAAACCTTCCGCACTGCGATGATGCCGGCGCGTAATGAATTATGGTGTTAACCATTCCGGCGTCAAACGTTCCCCATGAAAGGAAATAACATCCCCAGACGACTAGGCCTGTTTTAGTTCTAGACAGACTAACTTCCGTTTTCAACTGGAGGGAGGTCTCGGTTTATTTGCCCTGCCCAACAGACCTAAATACGAGCATTGAATACTATGCATAATGTTTGACCCTACAGGCCACACGTAACGGGATTTCATACTGGTGCAAGATTGGAACCGCAGTCTCGCCCAGGTAATAATCAGTTAGGAACGTTAGAGTGCACTAATGGTAACGGCACAGTGGGGGATACCAATCCTTCCTAATATGCACTGGGCTTGCCGACCGGTGGGAAAGAGCTCTTTAAGGGGCCCTATCATCTTGTCTATAATAAGCATGTGTGCGGTCTAGAGCTCCAAGTTTTTGATCAGGTTCACGGCCAAATCCGCAGAGTGGAGTAGCCCCGTTACGGTCCGGTCTATTTTTGTGGTCCATATTGCGAGTTTCTGGCAGTTTGGGCTCAGTCAGCAGGTGCCCTCTGGAATATAGGAAATCTAATCATGTGTACCCGCCGTTTTAAGCAGATGTTATCCTTATAGGTGAGTAACGATTCACGAGGGTATTCGCTGAACCCCAATCGTCAAGGTTATATCCTATAGCAGTTTTGCTTCGGCATACAGACTGCAAGGTTGGTGTCAAACGCTGCCATACTGGGCTTAGTACACGGTCTCACGGAGTTGAAGTTTGGCTCAGCATGGACAAGCCGAGTCAGAGCCCAGCAAAACTTCCGGCACTTGAGTATCGATGTATGTTCAAGCGTCACGCCGCCGGCCCATGATCGTTTGACCAGCCAGCGC'
i = 0
dict = {}

for j in range(4, (len(string) - 3)): #moving the end of the initial frame - creates initial length frame such as 4 before being indexed in next loop then once thats finished this starts the next frame with length 5
    i = 0
    for x in range(0, (len(string) - 3)): #moving the start of the frame

        if x == (len(string) - 4) and j + i > len(string): #not sure if these if statements are unnecessary or not but they are the last substring for each length before there would be an index error or it becomes an incorrect length
            break
        elif x == (len(string) - 5) and j + i > len(string):
            break
        elif x == (len(string) - 6) and j + i > len(string):
            break
        elif x == (len(string) - 7) and j + i > len(string):
            break
        elif x == (len(string) - 8) and j + i > len(string):
            break
        elif x == (len(string) - 9) and j + i > len(string):
           break
        elif x == (len(string) - 10) and j + i > len(string):
            break
        elif x == (len(string) - 11) and j + i > len(string):
            break
        elif x == (len(string) - 12) and j + i > len(string):
            break
        sub = string[x : j + i] #the start of the splice changes at the same rate as i
        if len(sub) > 12:
            break
        #print(sub)
        comp = ''
        for y in sub:
            if y == 'A':
                comp += 'T'
            elif y == 'T':
                comp += 'A'
            elif y == 'C':
                comp += 'G'
            elif y == 'G':
                comp += 'C'
        if sub == comp[::-1]:
            dict[x + 1] = len(sub) #have to add one to x as x is running on 0 indexing
        i += 1

for x, y in dict.items():
    print(x, y)


