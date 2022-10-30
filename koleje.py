# /* ---------------------------------------------| input |--------------------------------------------- */
line = input()
a,b = line.split()
n = int(a)
m = int(b)
connections = []
for k in range (m):
   line = input()
   o,p = line.split()
   connections.append([int(o),int(p)]) 

neighbours = []
graph = {}
need = 0
# /* ---------------------------------------------| functions |--------------------------------------------- */
def _neighbours(current):
    how_many = 0
    for neighbour in current:
        if current[neighbour] == 0:
            how_many += 1 
    return how_many          
# /* ---------------------------------------------| graph |--------------------------------------------- */
for i in range(1, n+1):
    graph[i] = {}
for city, neighbour in connections:
    graph[city][neighbour] = 0
    graph[neighbour][city] = 0
# /* ---------------------------------------------| neighbours |--------------------------------------------- */
for j in range (1,len(graph)+1):
    neighbours.append(_neighbours(graph[j]))

for u in range (len(neighbours)):
    if neighbours[u] - 2 == -1:
        need += 1
    elif neighbours[u] - 2 == -2:
        need += 2
    else:
        need += 0
print(need)
k = 2