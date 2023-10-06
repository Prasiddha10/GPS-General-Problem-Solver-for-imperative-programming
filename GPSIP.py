# Define the initial state and goal state
initial_state = (3, 3, 1)  # (missionaries on the left, cannibals on the left, boat position)
goal_state = (0, 0, 0)     # (missionaries on the left, cannibals on the left, boat position)

# Define a function to check if a state is valid
def is_valid_state(state):
    missionaries_left, cannibals_left, boat_position = state
    if missionaries_left < 0 or cannibals_left < 0:
        return False
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    if (
        (missionaries_left < cannibals_left and missionaries_left > 0) or
        (missionaries_right < cannibals_right and missionaries_right > 0)
    ):
        return False
    return True

# Define a function to generate valid successor states
def get_successor_states(state):
    successors = []
    missionaries_left, cannibals_left, boat_position = state

    # Move 1 missionary to the right
    new_state = (missionaries_left - 1, cannibals_left, 1 - boat_position)
    if is_valid_state(new_state):
        successors.append(new_state)

    # Move 1 cannibal to the right
    new_state = (missionaries_left, cannibals_left - 1, 1 - boat_position)
    if is_valid_state(new_state):
        successors.append(new_state)

    # Move 1 missionary and 1 cannibal to the right
    new_state = (missionaries_left - 1, cannibals_left - 1, 1 - boat_position)
    if is_valid_state(new_state):
        successors.append(new_state)

    # ... Repeat for other possible moves

    return successors

# Define a depth-first search algorithm to find a solution
def depth_first_search(state, path):
    if state == goal_state:
        return path
    for successor in get_successor_states(state):
        if successor not in path:
            new_path = path + [successor]
            solution = depth_first_search(successor, new_path)
            if solution is not None:
                return solution
    return None

# Find and print the solution
solution_path = depth_first_search(initial_state, [initial_state])
if solution_path:
    for state in solution_path:
        print(state)
else:
    print("No solution found.")
