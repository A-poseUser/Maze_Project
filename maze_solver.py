import os
import time


def help_d(i, j):
    global maze
    global used
    eval(used[i][j])
    maze[i][j] = '↑'

def help_u(i, j):
    global maze
    global used
    eval(used[i][j])
    maze[i][j] = '↓'

def help_l(i, j):
    global maze
    global used
    eval(used[i][j])
    maze[i][j] = '←'

def help_r(i, j):
    global maze
    global used
    eval(used[i][j])
    maze[i][j] = '→'


def bfs(h):
    global used
    stack = [[h, 1]]
    while stack:
        i, j = stack.pop()
        if used[i+1][j] == '·':
            used[i+1][j] = f"help_u({i}, {j})"
            stack.append([i+1, j])

        if used[i-1][j] == '·':
            used[i-1][j] = f"help_d({i}, {j})"
            stack.append([i-1, j])

        if used[i][j+1] == '·':
            used[i][j+1] = f"help_r({i}, {j})"
            stack.append([i, j+1])

        if used[i][j-1] == '·':
            used[i][j-1] = f"help_l({i}, {j})"
            stack.append([i, j-1])
        

def solve(name_in, name_out):
    global maze
    global used
    with open(os.path.join('examples', name_in), 'r', encoding="utf-8") as f:
        maze = list(map(list, f.read().split("\n")[:-1]))
    used = [[j for j in i] for i in maze] 

    hs = 0
    he = 0
    while maze[hs][0] != 'S':
        hs += 1
    while maze[he][-1] != 'F':
        he += 1
    bfs(hs)
    used[hs][1] = 'None'
    '''
    for i in maze:
        print(''.join(i))
    print("\n")
    '''
    eval(used[he][-2])
    maze[he][-2] = '→'
    used[hs][1] = '→'
    with open(os.path.join('solutions', name_out), 'w', encoding="utf-8") as f:
        for i in maze:
            f.write(''.join(i)+"\n")







    
