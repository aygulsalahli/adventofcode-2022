a = []
highest_scenic_score = -1

with open("../input.txt") as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        line = line.rstrip()
        a.append([int(x) for x in line])

    rows = len(a)
    columns = len(a[0])

    for row in range(rows):
        for col in range(columns):
            if row == 0 or row == len(a) - 1 or col == 0 or col == len(a[0]) - 1:
                continue

            top = top = 0
            for i in reversed(range(row)):
                top += 1
                if a[i][col] >= a[row][col]:
                    break

            bottom = 0
            for i in range(row + 1, rows):
                bottom += 1
                if a[i][col] >= a[row][col]:
                    break

            left = 0
            for j in reversed(range(col)):
                left += 1
                if a[row][j] >= a[row][col]:
                    break

            right = 0
            for j in range(col + 1, columns):
                right += 1
                if a[row][j] >= a[row][col]:
                    break

            scenic_score = top * bottom * left * right
            if highest_scenic_score < scenic_score:
                highest_scenic_score = scenic_score

    print(highest_scenic_score)
