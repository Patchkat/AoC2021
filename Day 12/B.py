def find_path(node, current_path, add_small):
    if node == 'start' or (node in visited and node.islower() and not add_small):
        return add_small
    visited.append(node)
    current_path.append(node)
    if node.islower() and visited.count(node) == 2:
        add_small = False
    if node == "end":
        paths.append([z for z in current_path])
        visited.remove(node)
        current_path.pop()
        return add_small
    for x in connections[node]:
        add_small = find_path(x, current_path, add_small)
    current_path.pop()
    if node.islower() and visited.count(node) == 2:
        add_small = True
    visited.reverse()
    visited.remove(node)
    visited.reverse()
    return add_small


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
    find_path(x, ["start"], True) 
print(len(paths))
