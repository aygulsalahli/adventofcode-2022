latest_command = None
x = 1
sprite = 1
cycle = 0
sum = 0
n = 20
crt = ""

with open("../input.txt") as f:
    while True:
        cycle += 1

        d = (cycle % 40) - 1
        if d < 0:
            d = max((cycle % 40) - 1, 40 - (cycle % 40) - 1)

        if sprite - 1 <= d <= sprite + 1:
            crt += "#"
        else:
            crt += "."

        if latest_command:
            _, amount = latest_command.split()
            amount = int(amount)
            x += amount
            sprite += amount
            latest_command = None
        else:
            line = f.readline().rstrip()
            if not line:
                break
            if line == "noop":
                latest_command = None
            else:
                latest_command = line

    print(f"{crt}")
