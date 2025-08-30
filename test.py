import sys
import heapq

n, m = map(int, input().split())
teams = []
for _ in range(n):
    members = list(map(int, input().split()))
    members.sort()
    teams.append(members)
# 初始化指针和最小值
min_heap = []
current_max = float('inf')



