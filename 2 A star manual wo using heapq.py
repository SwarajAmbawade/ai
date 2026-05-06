# code without heapq, manually finding smallest
def astar(graph, h, start, goal):
    open_list = [(0, start)]   # (f, node)
    g_cost = {start: 0}

    while open_list:
        # 🔥 Find node with smallest f manually
        min_index = 0
        for i in range(len(open_list)):
            if open_list[i][0] < open_list[min_index][0]:
                min_index = i

        f, node = open_list.pop(min_index)

        print("Expanding:", node)

        if node == goal:
            print("Goal reached!")
            return

        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + h[neighbor]
                open_list.append((f, neighbor))

    print("No path found")