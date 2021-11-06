# for matrix A
matrix_A = []
i = 0
X = float(input("how many rows for matrix_A: "))
Y = float(input("how many columns for matrix_A: "))
while i < Y:             # for column
    k = 0
    R = []
    i = i + 1
    while k < X:          # for row
        a = float(input(" input no for matrix A: "))
        R.append(a)
        k = k+1
    matrix_A.append(R)
# for matrix B
matrix_B = []
n = 0
W = float(input("how many rows for matrix_B: "))
Z = float(input("how many column for matrix_B: "))
while n < Z:              # for column
    m = 0
    C = []
    n = n + 1
    while m < W:          # for row
        b = float(input("input no for matrix B: "))
        C.append(b)
        m = m+1
    matrix_B.append(C)
# print("matrix_B is " + str(matrix_B))
# print("matrix_A is " + str(matrix_A))
# for multiplication:
if len(matrix_B) == len(R):
    az=0
    ax=[]
    while az < X :

        ay=0
        ab=[ ]
        while ay < Y:

            ao=0
            ap=[]
            while ao < Z:
                h= matrix_A[az][ao]*matrix_B[ap][ay]
                ap.append(h)
                ao += 1
            ab.append(ap)
            ay +=1


print(h)

