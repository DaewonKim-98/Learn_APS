while True:
    sentence = str(input())
    if sentence == '.':
        break

    balance = True
    for i in range(len(sentence) - 1):
        for j in range(i, len(sentence)):
            if (i == '(' & j == ')') or (i == '[' & j == ']'):

