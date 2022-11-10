import os.path

while True:
    # choose input file
    print("Type the path of the input file or \"exit\" to exit the program:")
    givenInput = input()
    if givenInput == "exit": exit()
    while not os.path.exists(givenInput):
        print("That was no valid path. Type the path of the input file or \"exit\" to exit the program:")
        givenInput = input()
        if givenInput == "exit": exit()

    # bring data from input file in a suitable form
    data = open(givenInput).read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        for j in range(i+1):
            data[i][j] = int(data[i][j])

    # calculate Maximum Path Sums per line
    for i in range(1, len(data)):
        data[i][0] += data[i-1][0]
        data[i][i] += data[i-1][i-1]
        for j in range(1,i):
            data[i][j] += max(data[i-1][j-i], data[i-1][j])

    # calculate result from last line
    result = max(data[-1])

    # print result
    print("The Maximum Path Sum is " + str(result) + ".")