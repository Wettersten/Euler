def name_score(name):
    score = 0
    alph_dict = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
        'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26
                 }

    for letter in name:
        score += alph_dict[letter]

    return score


file = "data/p022_names.txt"
name_list = []

with open(file, 'r') as f:
    names = (f.readlines()[0].replace("\"", "").split(","))
    name_list = sorted(names)

name_sum = 0
index = 1
for name in name_list:
    name_sum += index * name_score(name)
    index += 1

print(name_sum)

#: answer is 871198282
