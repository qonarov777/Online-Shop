def conv(x, h):
     [n, m] = map(len, [x, h])
     result = [0] * (n + m - 1)
     for i in range(n):
             for j in range(m):
                     result[i + j] = x[i] * h[j]
     return result