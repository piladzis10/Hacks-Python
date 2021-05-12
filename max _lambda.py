n = [1,5,7,3,4,4,8,9,-10, 10]


print(max(n, key=n.count))
print(max(n, key=lambda x: x**2 + 1))

print(sorted(n, key = lambda x: x**2, reverse=True))