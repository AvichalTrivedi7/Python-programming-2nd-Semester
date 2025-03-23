# We will write the A* search algorithm program for 8-puzzle problem (The matrix will be made using numpy)
 
import numpy as np
import heapq

class Puzzle:
    def __init__(self, start, goal):
        self.start = start   
        self.goal = goal
        self.rows, self.cols = start.shape
        
    def find_blank(self, state):
        return tuple(np.argwhere(state == 'X')[0]) # Will give the coordinates of the X tile
    
    def get_neighbors(self, state):
        blank_pos = self.find_blank(state)
        row, col = blank_pos
        moves = {
            'Up': (row - 1, col),
            'Down': (row + 1, col),
            'Left': (row, col - 1),
            'Right': (row, col + 1)
        }
        valid_moves = []
        
        for move, (r, c) in moves.items():
            if 0 <= r < self.rows and 0 <= c < self.cols:
                new_state = state.copy()
                new_state[row, col], new_state[r, c] = new_state[r, c], new_state[row, col]
                valid_moves.append(new_state)
        
        return valid_moves
    
    def misplaced_tiles(self, state):
        return np.sum((state != self.goal) & (state != 'X'))
    
    def a_star_search(self):
        start_tuple = tuple(map(tuple, self.start))
        goal_tuple = tuple(map(tuple, self.goal))
        
        pq = []  # Priority Queue
        h_start = self.misplaced_tiles(self.start)
        heapq.heappush(pq, (h_start, 0, start_tuple))   # (f(x), g(x), state)
        visited = set()
        parent_map = {}
        
        while pq:
            _, g, current_state = heapq.heappop(pq)
            
            if current_state == goal_tuple:
                return self.reconstruct_path(parent_map, start_tuple, goal_tuple)
            
            if current_state in visited:
                continue
            visited.add(current_state)
            
            state_np = np.array(current_state)
            for neighbor in self.get_neighbors(state_np):
                neighbor_tuple = tuple(map(tuple, neighbor))
                if neighbor_tuple not in visited:
                    h = self.misplaced_tiles(neighbor)
                    f = g + 1 + h
                    heapq.heappush(pq, (f, g + 1, neighbor_tuple))
                    parent_map[neighbor_tuple] = current_state
        
        return None  # No solution found
    
    def reconstruct_path(self, parent_map, start, goal):
        path = []
        state = goal
        while state != start:
            path.append(state)
            state = parent_map[state]
        path.append(start)
        return path[::-1]
    
    def print_path(self, path):
        for step, state in enumerate(path):
            print(f"Step {step}:")
            print(np.array(state), "\n")
        print(f"Solution found in {len(path) - 1} moves.")

# Define start and goal states
goal_state = np.array([[1,2,3], [4,5,6], [7,8,'X']])
start_state = np.array([[1,2,3], [4,8,5], [7,'X',6]])

# Solve the puzzle
puzzle = Puzzle(start_state, goal_state)
solution_path = puzzle.a_star_search()
if solution_path:
    puzzle.print_path(solution_path)
else:
    print("No solution found.")
