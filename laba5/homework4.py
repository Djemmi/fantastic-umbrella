hashmap = {1: "line1", 2: "line2", 3: "line3", 4: "line4", 5: "line5"}


def reverseDict(dic: {}) -> {}:
    dict_keys = []
    dict_values = []
    reversed_dict = {}

    for addkey in hashmap.keys():
        dict_keys.append(addkey)

    for key in dict_keys:
        dict_values.append(hashmap[key])

    for x in range(len(dict_keys)):
        reversed_dict[dict_values[x]] = dict_keys[x]
    return reversed_dict


print(reverseDict(hashmap))
