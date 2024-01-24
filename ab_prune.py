maximum, minimum = float("inf"), float("-inf")


def prune(d, node, maxp, v, A, B):
    if d == 3:
        return v[node]
    if maxp:
        best = minimum
        for i in range(0, 2):
            value = prune(d + 1, node * 2 + i, False, v, A, B)
            best = max(best, value)
            A = max(A, best)
            if B <= A:
                break
        return best
    else:
        best = maximum
        for i in range(0, 2):
            value = prune(d + 1, node * 2 + i, True, v, A, B)
            best = min(best, value)
            B = min(B, best)
            if B <= A:
                break
        return best


scr = []
x = int(input("Enter total number of leaf node:"))
for i in range(x):
    y = int(input(f"Enter node value {i+1}: "))
    scr.append(y)

depth = int(input("Enter depth value:"))
node = int(input("Enter node value:"))
print("The optimal value is:", prune(depth, node, True, scr, minimum, maximum))
