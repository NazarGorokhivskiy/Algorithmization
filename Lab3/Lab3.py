def read_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    pairs = []
    for elem in lines[1:]:
        pairs.append(tuple(map(int, elem.split())))
    print("Entered pairs: " + str(pairs)[1:-1])

    return pairs


def algorithm(pairs):
    # algorithm for creating tribes with unique elements
    tribes = [set()]
    tribes[0].add(pairs[0][0])
    tribes[0].add(pairs[0][1])

    pairs_count = pairs.__len__()

    for i in range(1, pairs_count):
        added_index = 0
        should_merge = False
        create_new_item = True

        for j in range(tribes.__len__()):
            if pairs[i][0] in tribes[j] or pairs[i][1] in tribes[j]:
                create_new_item = False
                tribes[j].add(pairs[i][0])
                tribes[j].add(pairs[i][1])

                if should_merge:
                    tribes[added_index] = tribes[added_index].union(tribes[j])
                    tribes.pop(j)
                    break
                should_merge = True
                added_index = j

        if create_new_item:
            tribes.append(set())
            tribes[tribes.__len__() - 1].add(pairs[i][0])
            tribes[tribes.__len__() - 1].add(pairs[i][1])
    print("All tribes: " + str(tribes)[1:-1])

    # algorithm for counting all men and women in tribes
    people_count = []
    for i in range(tribes.__len__()):
        people_count.append([0, 0])
        for tribe_item in tribes[i]:
            if tribe_item % 2 == 0:
                people_count[i][0] += 1
            else:
                people_count[i][1] += 1
    print("People count: " + str(people_count)[1:-1])

    # counting all possible weeding pairs
    wedding_count = 0
    for i in range(people_count.__len__()):
        for j in range(i + 1, people_count.__len__()):
            wedding_count += people_count[i][0] * people_count[j][1]
            wedding_count += people_count[i][1] * people_count[j][0]

    return wedding_count


# main function
pairs_from_file = read_from_file("in2")
wedd_count = algorithm(pairs_from_file)
print("Total possible weddings: %d \n" % wedd_count)
