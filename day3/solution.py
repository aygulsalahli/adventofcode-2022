def get_mapping_value(char):
    if char.islower():
        return ord(common) - 96
    return ord(char) - 38


with open("input.txt") as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        common = "".join(set(first).intersection(second))
        sum += get_mapping_value(common)

    print(f"here is the sum: {sum}")
