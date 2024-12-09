class Node:
    def __init__(self, name, h=0):
        self.name = name
        self.g = float('inf')  # cost from start (for A*)
        self.h = h            # heuristic value (for A*)
        self.f = float('inf')  # total cost (g + h) (for A*)
        self.parent = None
        self.neighbors = {}    # dictionary of neighbor / cost pairs

def a_star_search(start, goal):
    FRINGE = []
    CLOSED = []
    
    start.g = 0
    start.f = start.g + start.h
    FRINGE.append(start)

    print("\n## A* Search Progress:")
    step = 1
    
    while FRINGE:
        current = min(FRINGE, key=lambda x: x.f)

        print(f"\nStep {step}:")
        print(f"Current Node: {current.name} (f={current.f}, g={current.g}, h={current.h})")
        print(f"FRINGE: {[node.name for node in FRINGE]}")
        print(f"CLOSED: {[node.name for node in CLOSED]}")
        
        if current == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            print("\n## Final Result:")
            print(f"Path Found: {' -> '.join(path[::-1])}")
            print(f"Total Cost: {goal.g}")
            return path[::-1]
        
        FRINGE.remove(current)
        CLOSED.append(current)
        
        for neighbor, cost in current.neighbors.items():
            if neighbor in CLOSED:
                continue
                
            tentative_g = current.g + cost
            
            if neighbor not in FRINGE:
                FRINGE.append(neighbor)
                print(f"Added {neighbor.name} to FRINGE")
            elif tentative_g >= neighbor.g:
                continue
                
            neighbor.parent = current
            neighbor.g = tentative_g
            neighbor.f = neighbor.g + neighbor.h
            print(f"Updated {neighbor.name}: f={neighbor.f}, g={neighbor.g}, h={neighbor.h}")
    
        step += 1
    
    print("\nNo path found!")
    return None

def bfs_search(start, goal):
    FRINGE = []
    CLOSED = []
    
    FRINGE.append(start)
    
    print("\n## BFS Search Progress:")
    step = 1
    
    while FRINGE:
        current = FRINGE.pop(0)  # FIFO
        
        print(f"\nStep {step}:")
        print(f"Current Node: {current.name}")
        print(f"FRINGE: {[node.name for node in FRINGE]}")
        print(f"CLOSED: {[node.name for node in CLOSED]}")
        
        if current == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            print("\n## Final Result:")
            print(f"Path Found: {' -> '.join(path[::-1])}")
            return path[::-1]
        
        CLOSED.append(current)
        
        for neighbor, _ in current.neighbors.items():
            if neighbor in CLOSED or neighbor in FRINGE:
                continue
                
            neighbor.parent = current
            FRINGE.append(neighbor)
            print(f"Added {neighbor.name} to FRINGE")
            
        step += 1
    
    print("\nNo path found!")
    return None

def dfs_search(start, goal):
    FRINGE = []
    CLOSED = []
    
    FRINGE.append(start)
    
    print("\n## DFS Search Progress:")
    step = 1
    
    while FRINGE:
        current = FRINGE.pop()  # LIFO
        
        print(f"\nStep {step}:")
        print(f"Current Node: {current.name}")
        print(f"FRINGE: {[node.name for node in FRINGE]}")
        print(f"CLOSED: {[node.name for node in CLOSED]}")
        
        if current == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            print("\n## Final Result:")
            print(f"Path Found: {' -> '.join(path[::-1])}")
            return path[::-1]
        
        CLOSED.append(current)
        
        for neighbor, _ in current.neighbors.items():
            if neighbor in CLOSED or neighbor in FRINGE:
                continue
                
            neighbor.parent = current
            FRINGE.append(neighbor)
            print(f"Added {neighbor.name} to FRINGE")
            
        step += 1
    
    print("\nNo path found!")
    return None

# Create nodes
START = Node("START", h=0)
A = Node("A", h=2)
B = Node("B", h=5)
C = Node("C", h=2)
D = Node("D", h=1)
GOAL = Node("GOAL", h=0)

# Define neighbors
START.neighbors[A] = 5
START.neighbors[B] = 5
START.neighbors[D] = 5

A.neighbors[START] = 5
A.neighbors[C] = 5

B.neighbors[START] = 5
B.neighbors[D] = 5

C.neighbors[A] = 5
C.neighbors[D] = 5
C.neighbors[GOAL] = 5

D.neighbors[START] = 5
D.neighbors[B] = 5
D.neighbors[C] = 5
D.neighbors[GOAL] = 5

GOAL.neighbors[D] = 5
GOAL.neighbors[C] = 5

# Run all three searches
print("\nRunning A* Search:")
a_star_search(START, GOAL)

print("\nRunning BFS Search:")
bfs_search(START, GOAL)

print("\nRunning DFS Search:")
dfs_search(START, GOAL)