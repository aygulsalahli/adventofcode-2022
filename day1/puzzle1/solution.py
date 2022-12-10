with open("input.txt") as f:
    calories = 0
    max_calory = -1
    lines = f.readlines()
    for line in lines:
        if line in ["\n", "\r\n"]:
            if calories > max_calory:
                max_calory = calories
            # resetting calories for the next elf..
            calories = 0
        else:
            calories += int(line)

    print(f"found the food ELF with {max_calory} calories...")
