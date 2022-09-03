import sys


# multiply list x (of size n) with matrix P (of size n x m)
def multiply_matrices(x, P):
    res = [0 for i in range(len(x))]
    for j in range(len(x)):
        for k in range(len(P)):
            res[j] += x[k] * P[k][j]
    return res


# read the input file in specified format
# return dictionary of vertices and edge matrix
def read_data(file_name: str):
    vertices = {}
    with open(file_name) as f:
        lines = f.readlines()
    vertices_count = int(lines[0].strip()[10:])
    for i in range(1, vertices_count + 1):
        v = lines[i].strip()
        v_id, v_name = v.split(' ')
        vertices[int(v_id)] = v_name[1:-1]

    edge_mx = [[0 for i in range(vertices_count)]
               for j in range(vertices_count)]
    edge_lines = lines[vertices_count + 2:]
    for line in edge_lines:
        n1, n2 = line.strip().split(' ')
        edge_mx[int(n1) - 1][int(n2) - 1] = 1
        edge_mx[int(n2) - 1][int(n1) - 1] = 1
    return vertices, edge_mx


def pagerank(file_name: str):
    vertices, edge_mx = read_data(file_name)

    rate = 0.15
    teleport_prob = rate / len(vertices)

    # build Transition (probability) matrix
    P = []
    for edges in edge_mx:
        out_ways = sum(edges)
        p = []
        for node in edges:
            p.append(teleport_prob if node == 0
                     else teleport_prob + (1 - rate) * (node / out_ways))
        P.append(p)

    # initial x values are 1/N
    x = [1 / len(vertices) for i in range(len(vertices))]

    # power iteration method with max iteration = 250
    # at each iteration, temp =  x * P
    # if there is no improvement, exit the loop, else x = temp
    for i in range(0, 250):
        temp = multiply_matrices(x, P)
        imp = sum([abs(val_1 - val_2) for val_1, val_2 in zip(x, temp)])
        if imp < 0.0000000001:
            break
        x = temp

    # print maximum 50 scores and corresponding person
    for n in range(1, 51):
        val = sorted(x)[-n]
        index = x.index(val)
        print(n, vertices[index + 1], val)


# run the program with filename as command-line argument
if __name__ == '__main__':
    pagerank(sys.argv[1])
