import os
import random
def generate(name):

    # Черный квадрат
    black_square = ' '# "\u25A0"
    # Белый квадрат
    white_square = 'H'# "\u25A1"
    h = 25
    w = 49
    maze = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i % 2 != 0 and j % 2 != 0 and i < h-1 and j < w-1:
                maze[i][j] = 1
    steck = [(1,1)]
    def dfs(x,y,steck):
        maze[x][y] = 2
        nups = []
        walls = []
        countnup = 0
        if x - 2 > 0 and maze[x-2][y] != 2:
            nups.append((x-2,y))
            walls.append((x-1,y))
            countnup += 1
        if x + 2 < h and maze[x+2][y] != 2:
            nups.append((x + 2, y))
            walls.append((x + 1, y))
            countnup += 1
        if y - 2 > 0 and maze[x][y-2] != 2:
            nups.append((x, y-2))
            walls.append((x, y - 1))
            countnup += 1
        if y + 2 < w and maze[x][y+2] != 2:
            nups.append((x, y + 2))
            walls.append((x, y + 1))
            countnup += 1
        if countnup >= 2:
            steck.append((x,y))
        if countnup >= 1:
            a = random.randint(0, countnup - 1)
            maze[walls[a][0]][walls[a][1]] = 2
            dfs(*nups[a], steck)
        else:
            if len(steck) == 0:
                return
            dfs(*steck.pop(),steck)
    dfs(1,1,steck)

    maze[1][0] = "S"
    maze[h-2][w-1] = "·"
    for i in range(h):
        maze[i].append("█")
    maze[h-2][w] = "F"
    
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 0:
                maze[i][j] =  "█"
            if maze[i][j] == 2:
                maze[i][j] = '·'

    with open(os.path.join('examples', name), 'w', encoding="utf-8") as f:
        for i in maze:
            f.write(''.join(i)+"\n")
    



