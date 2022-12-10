with open("../puzzle1/input.txt") as f:
    elf_calories = []
    calories = 0
    max_calory = -1
    lines = f.readlines()
    for line in lines:
        if line in ["\n", "\r\n"]:
            if calories > max_calory:
                max_calory = calories
            elf_calories.append(calories)
            # resetting calories for the next elf..
            calories = 0
        else:
            calories += int(line)
    elf_calories.sort(reverse=True)
    top3 = elf_calories[0] + elf_calories[1] + elf_calories[2]
    print(f"found the sum of top 3 calories: {top3}")
