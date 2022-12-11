size_of_dirs = {}
stack = []

with open("input.txt") as f:
    lines = f.readlines()
    current_dir = None

    for index, line in enumerate(lines):
        line = line.rstrip()
        if "$ cd " in line:
            current_dir = line[5:]
            if current_dir != "..":
                current_dir = f"{index}{current_dir}"
                stack.append(current_dir)
            else:
                stack.pop()

        elif "$ ls" in line:
            continue
        else:
            p1, p2 = line.split()
            if "dir" not in p1:
                for e in stack:
                    if e in size_of_dirs:
                        size_of_dirs[e] += int(p1)
                    else:
                        size_of_dirs[e] = int(p1)

    result = 0
    for e, v in size_of_dirs.items():
        if v <= 100000:
            result += v

    print(result)
