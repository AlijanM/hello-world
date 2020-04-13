def case_converter(s):
    newlist = []
    for i in range(len(s)):
        if i % 2 == 0:
            newlist.append(s[i].upper())
        else:
            newlist.append(s[i].lower())

    print(''.join(newlist))


case_converter('hello')