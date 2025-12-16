# USACO 2022 Bronze #1: Herdle

answer_dict = {}
guess_dict = {}
matrix1 = [[], [], []]
matrix2 = [[], [], []]

for row in range(3):
    answer = input()
    for letter in answer:
        if letter in answer_dict.keys():
            answer_dict[letter] += 1

        else:
            answer_dict[letter] = 1

        matrix1[row].append(letter)

for row in range(3):
    guess = input()
    for letter in guess:
        if letter in guess_dict.keys():
            guess_dict[letter] += 1

        else:
            guess_dict[letter] = 1

        matrix2[row].append(letter)

#print(matrix1, matrix2)#, answer_dict, guess_dict)

commons = list(set(answer_dict.keys()).intersection(set(guess_dict.keys())))
#print(commons)
yellows = {}
greens = 0

for term in commons:
    #print(term)
    yellows[term] = min([answer_dict[term], guess_dict[term]])

for row in range(3):
    for column in range(3):
        if matrix1[row][column] == matrix2[row][column]:
            yellows[matrix2[row][column]] -= 1
            greens += 1

print(greens)
print(sum(list(yellows.values())))
