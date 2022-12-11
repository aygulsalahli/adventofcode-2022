with open("input.txt") as f:
    line = f.readline()
    answer = None
    index = 0
    while index < len(line) - 5:
        piece = line[index : index + 4]
        if len(set(piece)) == len(piece):
            answer = index + 4
            break
        index += 1

    print(f"The answer is {answer}")
