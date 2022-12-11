with open("input.txt") as f:
    num_of_overlaps = 0
    lines = f.readlines()
    for line in lines:
        first, second = line.split(",")
        first_lower, first_upper = first.split("-")
        first_lower, first_upper = int(first_lower), int(first_upper)
        second_lower, second_upper = second.split("-")
        second_lower, second_upper = int(second_lower), int(second_upper)

        if (
            second_lower <= first_lower <= second_upper
            and second_lower <= first_upper <= second_upper
        ):
            num_of_overlaps += 1
            continue

        if (
            first_lower <= second_lower <= first_upper
            and first_lower <= second_upper <= first_upper
        ):
            num_of_overlaps += 1

    print(f"Number of overlaps: {num_of_overlaps}")
