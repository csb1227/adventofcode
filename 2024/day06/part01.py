from aoc_methods import read_input, get_guard, get_obstacles

guard_map = read_input("input/actual.txt")
guard = get_guard(guard_map)
obstacles = get_obstacles(guard_map)

print(guard)

guard_is_on_duty = True

while guard_is_on_duty:
    # current_map = guard.view_map()
    next_obstacle = guard.next_obstacle_ahead()

    if next_obstacle:
        guard.walk_to(next_obstacle)
        guard.turn()
    else:
        guard_is_on_duty = False

guard.end_shift()

print(guard)