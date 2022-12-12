matrix = [[0 for i in range(1000)] for i in range(1000)]
middle = len(matrix) // 2
h_at = (middle, middle)
set_of_visited_points = set()
t_at = (middle, middle)
list_of_tales = [t_at] * 9
set_of_visited_points.add(t_at)


def adjacent(h_at, t_at):
    if t_at[0] - 1 <= h_at[0] <= t_at[0] + 1 and t_at[1] - 1 <= h_at[1] <= t_at[1] + 1:
        return True
    return False


def move_tails():
    global h_at
    current = list_of_tales[0]
    if not adjacent(h_at, current):
        moved_to = move_tail(h_at, current)
        list_of_tales[0] = moved_to
    for i in range(1, 9):
        follows_h_at = list_of_tales[i - 1]
        current = list_of_tales[i]
        if not adjacent(follows_h_at, current):
            moved_to = move_tail(follows_h_at, current)
            list_of_tales[i] = moved_to
            if i == 8:
                set_of_visited_points.add(moved_to)


def move_tail(h_at, t_at):
    # same row
    if h_at[0] == t_at[0]:
        # up
        if h_at[1] < t_at[1]:
            t_at = (t_at[0], t_at[1] - 1)
        # low
        else:
            t_at = (t_at[0], t_at[1] + 1)
    # same column
    elif h_at[1] == t_at[1]:
        # left
        if h_at[0] < t_at[0]:
            t_at = (t_at[0] - 1, t_at[1])
        # right
        else:
            t_at = (t_at[0] + 1, t_at[1])
    # up left
    elif h_at[0] < t_at[0] and h_at[1] < t_at[1]:
        t_at = (t_at[0] - 1, t_at[1] - 1)
    # up right
    elif h_at[0] > t_at[0] and h_at[1] < t_at[1]:
        t_at = (t_at[0] + 1, t_at[1] - 1)
    # bottom left
    elif h_at[0] < t_at[0] and h_at[1] > t_at[1]:
        t_at = (t_at[0] - 1, t_at[1] + 1)
    # bottom right
    elif h_at[0] > t_at[0] and h_at[1] > t_at[1]:
        t_at = (t_at[0] + 1, t_at[1] + 1)

    return t_at


def move(direction, steps):
    global h_at
    while steps:
        if direction == "D":
            h_at = (h_at[0] + 1, h_at[1])
        if direction == "U":
            h_at = (h_at[0] - 1, h_at[1])
        if direction == "L":
            h_at = (h_at[0], h_at[1] - 1)
        if direction == "R":
            h_at = (h_at[0], h_at[1] + 1)
        move_tails()
        steps -= 1


with open("../input.txt") as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        line = line.rstrip()
        direction, steps = line.split()
        move(direction, int(steps))

    print(len(set_of_visited_points))
