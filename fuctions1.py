# 1. Reversing a list in python


def revlist():
    list1 = [100, 200, 300, 400, 500]
    n = reversed(list1)
    x = list1[::-1]
    print(x)
    print(n)
    # Or this way
    print(list(e for e in reversed(list1)))

# 2. Concatenate two lists index-wise


def zipping():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    res = []
    for i in range(0, len(list1)):
        x = ""
        x = list1[i] + list2[i]
        res.append(x)
    print(res)

# 3. Given a two Python list. Iterate both lists simultaneously such that list1 should display
# item in original order and list2 in reverse order


def iterateboth():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    i = 0
    for x, y in zip(list1, list2[::-1]):
        print(x, y)


# 4. Remove empty strings from the list of strings
def removeempty():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    # for i in list1:
    #     if i == "":
    #         list1.remove(i)
    # print(list1)
    res = list(filter(None, list1))
    print(res)


# 5. Below are the two lists convert it into the dictionary
def creatingdic():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    dic = {}
    # for i in range (0,len(keys)):
    #     dic[keys[i]] = values[i]
    # print(dic)
    dic = dict(zip(keys, values))
    print(dic)


# 6. Merge following two Python dictionaries into one


def mergedic():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
    dict2.update(dict1)
    print(dict2)
    res1 = dict1 | dict2
    print(res1)
    res2 = {**dict1, **dict2}
    print(res2)


# 7. Access the value of key ‘history’ from the below
def accessvalue():
    sampledict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
    print(sampledict["class"]["student"]["marks"]["history"])

# 8. Parse the following JSON to get all the values of a key ‘name’ within an array


def parsejson():
    given = [{"id": 1, "name": "name1", "color": ["red", "green"]},
             {"id": 2, "name": "name2", "color": ["pink", "yellow"]}]
    l = []
    for dic in given:
        l.append(dic["name"])
    print(l)


if __name__ == '__main__':
    zipping()
    iterateboth()
    removeempty()
    creatingdic()
    mergedic()
    accessvalue()
    parsejson()
    revlist()