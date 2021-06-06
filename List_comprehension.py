x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i,j,k] for i in [s for s in range(x+1)] for j in [o for o in range(y+1)] for k in [p for p in range(z+1)] if i+j+k!=n])