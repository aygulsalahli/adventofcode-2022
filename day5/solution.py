list_of_stacks = []


def move_like_jagger(line):
    if "move" not in line:
        return

    cmds = line.split()
    print(cmds)
    count, from_, to_ = int(cmds[1]), int(cmds[3]) - 1, int(cmds[5]) - 1
    while count > 0:
        elem = list_of_stacks[from_].pop(0)
        list_of_stacks[to_].insert(0, elem)
        count -= 1


with open("input.txt") as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        if line in ["\n", "\r\n"]:
            continue
        if "move" in line:
            move_like_jagger(line)
        else:
            parts = list(map("".join, zip(*[iter(line)] * 4)))
            for ip, part in enumerate(parts):
                if part[1].isnumeric():
                    break
                if index == 0:
                    list_of_stacks.append([] if part[1] == " " else [part[1]])
                    print(f"list of stacks created: {list_of_stacks}")
                else:
                    if part[1] != " ":
                        list_of_stacks[ip].append(part[1])

    result = ""
    for stack in list_of_stacks:
        result += stack[0]

    print(f"The answer is {result}")
