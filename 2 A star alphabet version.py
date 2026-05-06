import heapq

def astar(graph, h, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    
    g_cost = {start: 0}

    while pq:
        f, node = heapq.heappop(pq)

        print("Expanding:", node)

        if node == goal:
            print("Goal reached!")
            return

        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + h[neighbor]
                heapq.heappush(pq, (f, neighbor))

    print("No path found")


# -------- INPUT PART --------

v = int(input("Enter number of vertices: "))
graph = {}

print("Enter vertex names:")
vertices = []
for i in range(v):
    node = input(f"Vertex {i+1}: ")
    graph[node] = []
    vertices.append(node)

e = int(input("Enter number of edges: "))
for i in range(e):
    u, w, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)
    graph[u].append((w, cost))
    graph[w].append((u, cost))   # remove if directed

print("\nEnter heuristic values:")
h = {}
for node in vertices:
    h[node] = int(input(f"h({node}): "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# -------- RUN --------
astar(graph, h, start, goal)