import time


MAZE = [
    [3,2,2,2,2,2,2,2,1],
    [0,0,2,2,2,2,2,0,0],
    [2,0,0,2,2,2,0,0,2],
    [2,2,0,0,2,0,0,2,2],
    [2,2,2,0,0,0,2,2,2]]


def fetch_maze():
    print("maze-id {}-{}".format(1, round(time.time())))
    print('['+str(MAZE[0])+',')
    for line in MAZE[1:-1]:
        print(' '+str(line)+',')
    print(' '+str(MAZE[-1])+']')
    return MAZE