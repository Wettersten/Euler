from itertools import permutations

permrange = list(range(10))
target_index = 1000000

perm = permutations(permrange)
target_perm = list(perm)[target_index - 1]

answer = ""
for dig in target_perm:
    answer += str(dig)

print(answer)

#: answer: 2783915460
