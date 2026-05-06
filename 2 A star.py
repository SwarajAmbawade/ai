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

for i in range(v):
    graph[i] = []

e = int(input("Enter number of edges: "))
for i in range(e):
    u, w, cost = map(int, input("Enter edge (u v cost): ").split())
    graph[u].append((w, cost))
    graph[w].append((u, cost))   # remove this if graph is directed

print("\nEnter heuristic values:")
h = {}
for i in range(v):
    h[i] = int(input(f"h({i}): "))

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

# -------- RUN --------
astar(graph, h, start, goal)






# Sample Input
# Enter number of vertices: 4
# Enter number of edges: 4
# Enter edge (u v cost): 0 1 1
# Enter edge (u v cost): 0 2 4
# Enter edge (u v cost): 1 3 3
# Enter edge (u v cost): 2 3 1

# Enter heuristic values:
# h(0): 5
# h(1): 3
# h(2): 2
# h(3): 0

# Enter start node: 0
# Enter goal node: 3


# Expected Output
# Expanding: 0
# Expanding: 1
# Expanding: 3
# Goal reached!


# -------- GRAPH DIAGRAM --------
#
#        (1)
#     1 /   \ 3
#      /     \
#    (0)     (3)
#      \     /
#     4 \   / 1
#        (2)



# new diragram
# -------- GRAPH DIAGRAM --------
#
#              (A)
#            /  |  \
#         1 /   |4  \3
#          /    |    \
#        (B)   (C)   (D)
#        /  \      \    \
#     5 /    \2     \1   \6
#      /      \      \    \
#    (E)      (F)-----(G)
#                2
#
# Goal Node = G
#
# Heuristic Values:
# h(A)=7
# h(B)=6
# h(C)=2
# h(D)=4
# h(E)=5
# h(F)=1
# h(G)=0
#
# Optimal Path:
# A → C → G
#
# Total Cost:
# 4 + 1 = 5
#
# -------------------------------

# Enter number of vertices: 7
# Enter number of edges: 7

# 0 1 1
# 0 2 4
# 0 3 3
# 1 4 5
# 1 5 2
# 2 6 1
# 5 6 2

# Heuristic Values:
# 0 → 7
# 1 → 6
# 2 → 2
# 3 → 4
# 4 → 5
# 5 → 1
# 6 → 0

# Start = 0
# Goal = 6
