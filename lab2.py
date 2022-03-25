import copy

def sub(b, ax):
    r = []
    for i in range(len(b)):
        r.append((abs(b[i] - ax[i])))
    return r

def multiply(a, x):
    ax = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += a[i][j] * x[j]
        ax.append(sum)
    return ax

def findMax(a, y, k):
    m = a[k][k]
    maxCoordinate = [k, k]
    for i in range(len(a) - k):
        for j in range(len(a[i]) - 1 - k):
            if abs(a[i + k][j + k]) > m:
                m = a[i + k][j + k]
                maxCoordinate = [i + k, j + k]
    x = a[k]
    a[k] = a[maxCoordinate(0)]
    a[maxCoordinate[0]] = x
    for i in range(len(a)):
        x = a[i][k]
        a[i][k] = a[i][maxCoordinate[1]]
        a[i][maxCoordinate[1]] = x
        
    c = y[k]
    y[k] = y[maxCoordinate[1]]
    y[maxCoordinate[1]] = c
    return a

def cout(a):
    for i in range(len(a)):
        b = ''
        for j in range(len(a[i]) - 1):
            b += (' ' + str(a[i][j]))
        b += ' | ' + str(a[i][len(a[i]) - 1])
        print(b)
    print('____________')
    
def gaus(a, b):
    z = [x for x in range(len(a))]
    for i in range(len(b)):
        a[i].append(b[i])
    cout(a)
    for i in range(len(a)):
        a = findMax(a, z, i)
        x = a[i][i]
        cout(a)
        for j in range(len(a[i])):
            a[i][j] /= x
        cout(a)
        for j in range(len(a)):
            if j == i:
                continue
            y = a[j][i]
            for k in range(len(a[i])):
                a[j][k] -= y * a[i][k]
        cout(a)
    result = []
    for i in z:
        result.append(a[i][-1])
    print(z)
    return result

def main():
    a = [
        [6.92, 1.28, 0.79, 1.15, -0.66],
        [0.92, 3.5, 1.3, -1.62, 1.02],
        [1.15, -2.46, 6.1, 2.1, 1.483],
        [1.33, 0.16, 2.1, 5.44, -18],
        [1.14, -1.68, -1.217, 9, -3]
    ]
    
    b = [11.172, 0.115, 0.009, 9.349, 5.172]
    
    x = gaus(copy.deepcopy(a), b)
    print('x:')
    print(x)
    ax = multiply(a, x)
    print('Ax:')
    print(ax)
    r = sub(b, ax)
    print('r:')
    print(r)

if __name__ == '__main__':
    main()