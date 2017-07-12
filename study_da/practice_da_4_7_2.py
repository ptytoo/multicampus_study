# -*- coding: utf-8 -*-
import numpy as np

#ndarray안의 모든 데이터는 같은 데이터형이어야 한다 list가 아니고 array이므로!
x=np.array([1,2,3])
print(x.dtype)
print(np.exp(-np.inf)) ##np.inf은 무한대를 의미

#print(np.array([1, 0]) / np.array([0, 0]))

###배열 생성###
x = np.array([1,2,3])
print(x)
a=np.zeros(5)
print(a)
a=np.ones(3)
print(a)
b=np.zeros((5,2), dtype="f8")
print(b)
c=np.zeros(5, dtype="S4")
c[0] = "abcd"
c[1] = "ABCDE"
print(c)
d=np.ones((2,3,4),dtype="i8")
print(d)
e=range(10)
print(e)
f=np.ones_like(e, dtype="f")
print(f)
f=np.zeros_like(e, dtype="f")
print(f)
g=np.empty((4,3))
print(g)
print(np.arange(10))
print(np.arange(3,21,2)) #시작, 끝(포함x), 단계

print(np.linspace(0,100,5))  #시작 끝(포함), 갯수
print(np.logspace(0,4,4,endpoint=False))

print(np.random.seed(0))
print(np.random.rand(4))
print(np.random.randn(3,5))

###전치 연산###
#행과 열을 바꾸는 작업
A = np.array([[1,2,3],[4,5,6]])
print(A.T)

###배열의 크기 변형###
#내부데이터 보존한 채로 형태만 변형
a=np.arange(12)
print(a)
b=a.reshape(3,4)
print(b)
print(a.reshape(2,2,-1))
print(a.reshape(2,-1,2))

print(a.flatten()) #배열을 무조건 1차원으로 펼치기

x=np.arange(5)
print(x)
print(x.reshape(1,5))
print(x.reshape(5,1))
#1차원 증가시키기
print(x[:,np.newaxis])

###배열 연결###
# hstack 배열을 옆으로 연결
# vstack 배열을 위아래로 연결
# dstack 배열을 깊이방향으로 합친다
# stack
# r_     배열을 좌우로 연결
# c_     배열의 차원을 증가시킨 후 좌우로 연결
# tile   동일한 배열을 반복하여 연결
a1=np.ones((2,3))
print(a1)
a2=np.zeros((2,2))
print(a2)
print(np.hstack([a1,a2]))

b1=np.ones((2,3))
print(b1)
b2=np.zeros((3,3))
print(b2)
print(np.vstack([b1,b2]))

c1=np.ones((3,4))
print(c1)
c2=np.zeros((3,4))
print(c2)
print(np.dstack([c1,c2])) #3*4가 3*4*2가 된다
print((np.dstack([c1,c2]).shape))

#...?이거 에러나는데?
#c3=np.stack([c1,c2])
#print(c3)
#print(c3.shape)

#3*4에서 3*2*4가 된다
# c=np.stack([c1,c2],axis=1)
# print(c)
# print(c.shape)

print(np.r_[np.array([1,2,3]),np.array([4,5,6])])
print(np.c_[np.array([1,2,3]),np.array([4,5,6])])

a=np.array([0,1,2])
print(np.tile(a,2))
print(np.tile(a,(3,2)))

###그리드 생성###
# http://freeprog.tistory.com/15
import matplotlib.pyplot as plt

x=np.arange(3)
print(x)
y=np.arange(5)
print(y)
X,Y = np.meshgrid(x,y)
print(X)
print(Y)
print([zip(x,y) for x,y in zip(X,Y)])
plt.scatter(X,Y,linewidths=10)
plt.show()