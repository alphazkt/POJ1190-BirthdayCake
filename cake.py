# -*- coding: utf-8 -*-
'''
Created on 2017年5月12日
m层蛋糕体积为n 最小表面积
@author: Alphatao

'''
from math import sqrt
global area,needV,m,minV,minA,minArea

def MaxVforNRH(n,r,h):
    maxv=0
    for i in range(n):
        maxv+=(r-i)*(r-i)*(h-i)
    return maxv

def dfs(v,n,r,h):
    global area,needV,m,minV,minA,minArea
    if n==0:
        if v>0:
            return
        else:
            minArea = min(minArea,area)
            return
    if v<=0:
        return
    if minV[n]>v:
        return
    if area+minA[n]>=minArea:
        return
    if (h<n or r<n):
        return
    if MaxVforNRH(n,r,h)<v:
        return
    for rr in range(r,n-1,-1):
        if n==m:#当前是最底层
            area = rr*rr
        for hh in range(h,n-1,-1):
            area += 2*rr*hh
            dfs(v-rr*rr*hh,n-1,rr-1,hh-1)
            area -= 2*rr*hh    

if __name__ == '__main__':
    global area,needV,m,minV,minA,minArea
    minA=[0 for i in range(30)] #侧面积
    minV=[0 for i in range(30)] #体积
    needV,m=map(int,raw_input('v,m=').split())
    for i in range(1,m+1):
        minV[i]=minV[i-1]+i*i*i
        minA[i]=minA[i-1]+2*i*i
    if minV[m]>needV:
        print 'impossible'
    else:
        maxH = (needV-minV[m-1])/(m*m)+1#底层最大高度
        maxR = int(sqrt((needV-minV[m-1])/m)+1)
        area=0
        minArea =999999
        dfs(needV,m,maxR,maxH)
        if minArea==999999:
            print'can not find'
        else:
            print minArea
    
