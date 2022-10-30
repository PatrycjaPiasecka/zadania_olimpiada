# /* ---------------------------------------------| input |--------------------------------------------- */
paths = []
peaks = []

line = input()
a,b = line.split()

n = int(a) #zmiana
m = int(b)

if n > 1 and n < 100000 and m > 1 and m < 300000:
    for u in range (n):
        high_mountain = input()
        peaks.append(int(high_mountain))
    for l in range (m):
        line = input()
        one,two = line.split()
        o = int(one)
        t = int(two)
        paths.append((o, t))

visited = []
unvisited = []
graph = {}
path = []

# /* ---------------------------------------------| functions |--------------------------------------------- */

def calculate_weight(start, stop):
    a = start - 1
    b = stop - 1  
    return max(peaks[a], peaks[b])

def pop_first_element():
    return unvisited.pop(0)

def pop_element_by_index(index):
    for elem in unvisited:
        if elem['index'] == index:
            unvisited.remove(elem)
            return elem
    return None

def sort_list_by_distance():
    unvisited.sort(key=lambda item: item['distance'])

# /* ---------------------------------------------| graph init |--------------------------------------------- */        

for i in range(1,len(peaks)+1):
  graph[i] = {}

for start, stop in paths:
    graph[start][stop] = calculate_weight(start,stop)
    graph[stop][start] = calculate_weight(start,stop)

# /* ---------------------------------------------| unvisited init |--------------------------------------------- */

for index in range(len(peaks)):
    unvisited.append({'index': index + 1, 'distance': 0 if index == 0 else 1000000, 'via': None})

while unvisited:
    sort_list_by_distance()
    current = pop_first_element()

    for neighbour_index in graph[current['index']]:
        neighbour = pop_element_by_index(neighbour_index)

        if neighbour is not None:
            distance = current['distance'] + graph[current['index']][neighbour['index']]

            if distance < neighbour['distance']:
                neighbour['distance'] = distance
                neighbour['via'] = current['index']

            unvisited.append(neighbour)
    
    visited.append(current)
    
# /* ---------------------------------------------| path |--------------------------------------------- */
first = visited[0]
path.append(first)

for i in range (len(graph)):
    if first['index'] != len(graph):
        if visited[i]['via'] == first['index']:
            path.append(visited[i])
            first = visited[i]
 
# /* -----------------------------------------| return hight |--------------------------------------------- */
hights = []
for j in range(len(path)-1):
    hights.append(calculate_weight(path[j]['index'],path[j+1]['index']))

print(max(hights))







