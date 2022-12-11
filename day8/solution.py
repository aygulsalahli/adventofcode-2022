a = []

with open("input.txt") as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        line = line.rstrip()
        a.append([int(x) for x in line])

    rows = len(a)
    columns = len(a[0])
    amount = 0
    for row in range(rows):
        for col in range(columns):
            if row == 0 or row == len(a) - 1 or col == 0 or col == len(a[0]) - 1:
                amount += 1
                continue

            # visible from the top?
            visible = True
            for i in range(row):
                if a[i][col] >= a[row][col]:
                    visible = False
                    break

            if visible:
                amount += 1
                continue

            # visible from the bottom?
            visible = True
            for i in range(row + 1, rows):
                if a[i][col] >= a[row][col]:
                    visible = False
                    break

            if visible:
                amount += 1
                continue

            # visible from the left?
            visible = True
            for j in range(col):
                if a[row][j] >= a[row][col]:
                    visible = False
                    break

            if visible:
                amount += 1
                continue

            # visible from the right?
            visible = True
            for j in range(col + 1, columns):
                if a[row][j] >= a[row][col]:
                    visible = False
                    break

            if visible:
                amount += 1

    print(amount)
