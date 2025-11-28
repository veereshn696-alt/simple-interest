import sys
if len(sys.argv) >= 4:
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
else:
    p = 100
    r = 2
    t = 3

si = (p * r * t) / 100

print("Principal:", p)
print("Rate:", r)
print("Time:", t)
print("Simple Interest =", si)
