latest_command = None
x = 1
cycle = 0
sum = 0
n = 20

with open("input.txt") as f:
    while True:
        cycle += 1

        if cycle == n:
            sum += n * x
            n += 40

        if latest_command:
            _, amount = latest_command.split()
            amount = int(amount)
            x += amount
            latest_command = None
        else:
            line = f.readline().rstrip()
            if not line:
                break
            if line == "noop":
                latest_command = None
            else:
                latest_command = line

    print(f"sum = {sum}")
