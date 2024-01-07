A = input()
A = A.split(" ")

N = int(A[0])
M = int(A[1])


for i in range(0, N):
    if(i%2 != 0):
        print((i * ".|.").center(M, "-"))

print("WELCOME".center(M, "-"))

for i in reversed(range(0, N)):
    if(i%2 != 0):
        print((i * ".|.").center(M, "-"))