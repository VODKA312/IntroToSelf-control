# start - 搜索算法的“开始”节点。
# goal - “目标”节点。
# path - 与地图上的有效交叉点访问序列相对应的整数数组。
# Ex: start=5, goal=34, path=[5,16,37,12,34]
from math import sqrt 

def shortest_path(M,start,goal):
    # The dictionary of the intersections of M
    nodes=M.intersections
    
    # The list that shows the connectivity of M
    roads=M.roads
    
    # The set of nodes already explored
    closedSet=set()
    
    # The set of intersections that are going to be explored
    openSet=set()
    openSet.add(start)
    
    
    # The dict that cantains the most efficient father node of every node
    Father={}
    
    # For each node, the cost of getting from the start node to that node.
    gScore={start:0}
    
    # For each node, the total cost of getting from the start node to the goal
    value=calc_H(nodes[start], nodes[goal])
    fScore={start:value}
    
    while len(openSet) is not 0:
        
        current = min(openSet, key=fScore.get)
        if current == goal:
            return reconstruct_path(Father, current)

        openSet.remove(current)

        closedSet.add(current)
        
        for neighbor in roads[current]:
            if neighbor in closedSet:
                continue
                
            #gScore[neighbor] = calc_G(nodes[current], nodes[neighbor])
            tentative_gScore = gScore[current] + calc_G(nodes[current], nodes[neighbor])
            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue
            gScore[neighbor] = tentative_gScore
            Father[neighbor] = current
            fScore[neighbor] = gScore[neighbor] + calc_H(nodes[neighbor], nodes[goal])
        
    print("shortest path called")
    return False

def calc_G(node1, node2):
    return sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)

def calc_H(node1, end):
    return sqrt((node1[0]-end[0])**2+(node1[1]-end[1])**2)

def reconstruct_path(Father, current):
    total_path = [current]
    while current in Father.keys():
        current = Father[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

