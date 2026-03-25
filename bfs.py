import collections
def bfs(graph , root):
    visited = []
    queue= collections.deque([root])
    visited.append(root)
    while queue:
        vertex = queue.popleft()
        for i in graph[vertex]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited



if __name__ == "__main__":
    graph = {0: [1, 2 , 3], 1: [0,2], 2: [0,1,4], 3: [0] , 4:[2]}
    print(bfs(graph , 0))

