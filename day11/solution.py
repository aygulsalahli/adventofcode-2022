monkeys = {}
with open("input.txt") as f:
    lines = f.readlines()
    current_monkey = 0
    for line in lines:
        line = line.rstrip()
        if "Monkey " in line:
            current_monkey = int(line[7:-1])
            monkeys[current_monkey] = {}
        elif "  Starting items: " in line:
            items = line[18:].split(", ")
            monkeys[current_monkey]["si"] = items
        elif "  Operation: " in line:
            operation = line[23:24]
            value = line[25:]
            monkeys[current_monkey]["operation"] = operation
            monkeys[current_monkey]["value"] = value
        elif "  Test: divisible by " in line:
            divisible_by = int(line[21:])
            monkeys[current_monkey]["divisible_by"] = divisible_by
        elif "    If true: throw to monkey " in line:
            true_case_monkey = int(line[29:])
            monkeys[current_monkey]["true_case_monkey"] = true_case_monkey
        elif "    If false: throw to monkey " in line:
            false_case_monkey = int(line[30:])
            monkeys[current_monkey]["false_case_monkey"] = false_case_monkey


def monkey_logic(item, monkey):
    operation = monkeys[monkey]["operation"]
    value = monkeys[monkey]["value"]
    value = item if value == "old" else int(value)
    worry_level = eval(f"{item} {operation} {value}")
    worry_level = worry_level // 3
    if worry_level % monkeys[monkey]["divisible_by"] == 0:
        true_case_monkey = monkeys[monkey]["true_case_monkey"]
        monkeys[true_case_monkey]["si"].append(worry_level)
    else:
        false_case_monkey = monkeys[monkey]["false_case_monkey"]
        monkeys[false_case_monkey]["si"].append(worry_level)


round = 1
while round < 21:
    for monkey in range(len(monkeys)):
        monkeys[monkey]["items"] = monkeys[monkey].get("items", 0) + len(
            monkeys[monkey]["si"]
        )
        for item in monkeys[monkey]["si"]:
            monkey_logic(item, monkey)

        monkeys[monkey]["si"] = []
    round += 1

monkey_inspected_items = []
for monkey in range(len(monkeys)):
    monkey_inspected_items.append(monkeys[monkey]["items"])

monkey_inspected_items.sort(reverse=True)
monkey_business = monkey_inspected_items[0] * monkey_inspected_items[1]
print(f"Monkey business is {monkey_business}")
