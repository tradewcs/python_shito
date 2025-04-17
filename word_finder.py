import nltk
from nltk.corpus import words
import string

nltk.download('words', quiet=True)
word_list = set(word.lower() for word in words.words())

def load_grid(filename):
    with open(filename, 'r') as f:
        grid = [line.strip().lower().split() for line in f.readlines()]
    return grid

def is_valid(x, y, visited, grid_size=5):
    return 0 <= x < grid_size and 0 <= y < grid_size and (x, y) not in visited

def dfs(grid, x, y, visited, current_word, found_words):
    if len(visited) > 3:
        return


    current_word += grid[x][y]
    visited.add((x, y))
    
    if len(current_word) >= 3 and current_word in word_list:
        found_words.add(current_word)

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, visited):
                dfs(grid, new_x, new_y, visited.copy(), current_word, found_words)

def find_words(grid):
    found_words = set()
    for x in range(5):
        for y in range(5):
            dfs(grid, x, y, set(), "", found_words)
    return found_words

if __name__ == '__main__':
    grid = load_grid('grid.txt')
    results = find_words(grid)
    print(f"\nFound {len(results)} words:\n")
    for word in sorted(results):
        print(word)

