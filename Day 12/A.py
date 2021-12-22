def find_path(node, current_path):
    if node in visited and node.islower():
        return
    visited.append(node)
    current_path.append(node)
    if node == "end":
        paths.append([z for z in current_path])
        visited.remove(node)
        current_path.pop()
        return
    for x in connections[node]:
        find_path(x, current_path)
    current_path.pop()
    visited.reverse()
    visited.remove(node)
    visited.reverse()

connections = {}
paths = []
visited = ["start"]
for x in open("./input.txt").readlines():
    nodes = x.rstrip().split("-")
    if nodes[0] in connections.keys():
        connections[nodes[0]].append(nodes[1])
    else:
        connections[nodes[0]] = [nodes[1]]
    if nodes[1] in connections.keys():
        connections[nodes[1]].append(nodes[0])
    else:
        connections[nodes[1]] = [nodes[0]]
for x in connections["start"]:
    find_path(x, ["start"]) 
print(len(paths))
