with open("datasets/rosalind_lgis.txt", "r") as file:
    data = file.readlines()
seq = list(map(int, data[1].split(" ")))
num = data[0]
print(seq)

def perms(data_set):
    list_of_subs = []
    sub = []
    for digit in range(len(data_set)):
        counter = 0
        for digit_2 in range(digit, len(data_set)):
            sub = [data_set[digit]]
            if data_set[digit_2] > data_set[digit]:
                sub.append(data_set[digit_2])
                list_of_subs.append(sub)
                counter += 1
        if counter == 0:
            list_of_subs.append(sub)

    return list_of_subs


print(perms(seq))


def join_pairs(list_of_pairs):
    list_of_joined = [[]]
    for pair in range(len(list_of_pairs)):
        for pair_2 in range(pair, len(list_of_pairs)):
            if list_of_pairs[pair_2][0] == list_of_pairs[pair][-1] and len(list_of_pairs[pair_2]) > 1:
                list_of_pairs[pair].append(list_of_pairs[pair_2][-1])
            if len(list_of_pairs[pair_2]) == 1 and list_of_pairs[pair_2][0] > list_of_pairs[pair][-1]:
                list_of_pairs[pair].append(list_of_pairs[pair_2][0])

                # print(list_of_pairs[pair])

        list_of_joined.append(list_of_pairs[pair])

    print(list_of_joined)

print(join_pairs(perms(seq)))
