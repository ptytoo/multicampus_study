# -*- coding: utf-8 -*-
import numpy as np
# a = np.array([0,1,2,3,4,5,6,7,8,9])
# print(a)
# print(type(a))


a = [0,1,2,3,4,5,6,7,8,9]
# b=[]
# for ai in a:
#     b.append(ai*2)
# print(b)

#numpy ==> 벡터형 연산 가능
test = np.array(a)
print(type(test))
print(test*2)
test

#보통은...
L=[0,1,2,3,4,5,6,7,8,9]
print(2*L)

a = np.array([1,2,3])
b = np.array([10,20,30])
print(2*a+b)
print(np.exp(a))
print(np.log(b))
print(np.sin(a))

b=np.array([[10,20,30,40],[50,60,70,80]])
print(b)
print(len(b))
print(len(b[0]))

c = np.array([[[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]],
             [[13,14,15,16],
              [17,18,19,20],
              [21,22,23,24]]])

print(c)
print(len(c))
print(len(c[0]))
print(len(c[0][0]))

print(a.ndim)
print(a.shape)

print(b.ndim)
print(b.shape)

print(c.ndim)
print(c.shape)

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
print(a[0,1])
print(a[-1,-1])

#array slice
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(a)
print(a[0,:])
print(a[:,1])
print(a[1,1:])
print(a[:2,:2])

#practice2
# 이 행렬에서 값 7 을 인덱싱한다.
# 이 행렬에서 값 14 을 인덱싱한다.
# 이 행렬에서 배열 [6, 7] 을 슬라이싱한다.
# 이 행렬에서 배열 [7, 12] 을 슬라이싱한다.
# 이 행렬에서 배열 [[3, 4], [8, 9]] 을 슬라이싱한다.
m = np.array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
print(m)
print(m[1,2])
print(m[2,-1])
print(m[1,1:3])
print(m[1:,2])
print(m[:2,3:])

#배열 인덱싱(데이터베이스 질의 기능)
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True, False, True, False, True, False])
print(a[idx])
print(a[a%2==0])

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) * 10
idx = np.array([0, 1, 4, 6, 8])
print(a[idx])

a = np.array([0, 1, 2, 3]) * 10
idx = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
print(a[idx])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
#왜 답이 다르게 나오지...?;;;;
d=[True,False,False,True]
print(a[:, [True,False,False,True]])
print(a[:, d])

print(a[[2,0,1],:])
