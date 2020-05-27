# 일반 리스트 더하기
m = [1, 2, 3]
n = [4, 5, 6]
print(m + n)

# print(m - n)
import numpy as np
# 브로드캐스팅
a = np.array([[1, 2]])
print(a)
b = np.array([[1], [2]])
print(b)
c = a + b
print(c)

# 행렬 모양 바꾸기
x = np.array(np.random.random(10))
print(x)
y = x.reshape(2, 5)
print(y)
