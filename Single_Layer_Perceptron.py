# Single Layer Perceptron


n = int(input('Введите n - длину списка: ')) 
x1 = []
for i in range(n):
    x1.append(int(input('Введите элемент матрицы x1 (1 или -1): ')))
x2 = []
for i in range(n):
    x2.append(int(input('Введите элемент матрицы x2 (1 или -1): ')))


W = [[0 for x in range(n**2)] for y in range(n**2)]    
for i in range(n):
    for j in range(n):
        if i==j:
            W[i][j]=0
        else:
            W[i][j]=x1[i]*x1[j]+x2[i]*x2[j]

z=[]
for i in range(n):
    z.append(int(input('Введите элемент матрицы z (1 или -1): ')))

print('x1 = ',x1)
print('x2 = ',x2)
print('z = ',z)

Y=[]
for i in range(n):
    summ=0
    for j in range(n):
        summ+=W[i][j]*z[j]
    if summ>=0:
        Y.append(1)
    else:
        Y.append(-1)

count=0
while Y!=z:
    for i in range(n):
        summ=0
        for j in range(n):
            summ+=W[i][j]*Y[j]
    if summ>=0:
        Y[i]=1
    else:
        Y[i]=-1
    count+=1
    if count==100000:
        print('За 100000 итераций совпадения не выявлено')
        break
        
print('Y = ',Y)
