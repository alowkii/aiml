# We have the Map of Romania. In this map, the distance between various places in Romania is given.
# If we have to reach from one place to another place there exist several paths.
# #Write a Python Program to find the shortest distance between any two places using a A* search algorithm.


import heapq

example_map = {
    "S": {"A": 5, "B": 2},
    "A": {"B": 3, "G": 5, "S": 5},
    "B": {"A": 3, "C": 3, "D": 1, "S": 2},
    "C": {"B": 3, "E": 1, "G": 4},
    "D": {"B": 1, "E": 4},
    "E": {"C": 1, "D": 4, "G": 2},
    "G": {"A": 5, "C": 4, "E": 2},
}

example_heuristic = {"S": 5, "A": 3, "B": 4, "C": 2, "D": 6, "E": 3, "G": 0}


def a_star_search(graph, start, goal, heuristic1):
    open_list = [(0, start)]
    closed_set = set()

    g_score = {location: float("inf") for location in graph}
    g_score[start] = 0

    while open_list:
        current_g, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return g_score[goal]

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, distance in graph[current_node].items():
            tentative_g = g_score[current_node] + distance

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic1[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return float("inf")


start_location = "A"
goal_location = "D"

shortest_distance = a_star_search(
    example_map, start_location, goal_location, example_heuristic
)

if shortest_distance < float("inf"):
    print(
        f"The shortest distance from {start_location} to {goal_location} is {shortest_distance} km."
    )
else:
    print(f"No path found from {start_location} to {goal_location}.")
