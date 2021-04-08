with open("rosalind_lgis.txt", "r") as file:
    data = file.readlines()

sequence_int = list(map(int, data[1].split(" ")))


def permutations(data_set, n):
    list_of_increasing = [[]]

    for number in range(len(data_set)):
        for i in range(1, len(data_set)-number):
            increasing = []
            increasing.append(data_set[number])
            for counter in range(i, len(data_set) - number):
                if data_set[number + counter] >= increasing[-1]:
                    increasing.append(data_set[number + counter])
            if len(increasing) > len(list_of_increasing):
                list_of_increasing = increasing
                print(list_of_increasing)
    return list_of_increasing
print(permutations(sequence_int, 5))


