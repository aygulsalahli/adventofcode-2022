def get_mapping_value(char):
    if char.islower():
        return ord(common) - 96
    return ord(char) - 38


with open("../input.txt") as f:
    sum = 0
    lines = f.readlines()
    for index, line in enumerate(lines):
        step = index % 3 + 1
        if step == 1:
            first = line
        elif step == 2:
            second = line
        else:
            common = "".join(set(first).intersection(second).intersection(line)).strip()
            sum += get_mapping_value(common)

    print(f"Here is the sum of badges: {sum}")
