# DP(Dynamic Programming)

- 동적 계획 알고리즘은 그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘
- 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

## 피보나치 수 DP 적용

- 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조

1. 문제를 부분 문제로 분할
   - Fibonacci(n) 함수는 Fibonacci(n - 1)과 Fibonacci(n - 2)의 합
   - Fibonacci(n - 1)은 Fibonacci(n - 2)와 Fibonacci(n - 3)의 합
   - ...
   - Fibonacci(n)은 Fibonacci(n - 1), Fibonacci(n - 2), Fibonacci(n - 3) 의 부분집합으로 나뉨
2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분부터 해를 구한다.
3. 그 결과는 상위 테이블에 저장하고, 테이블에 정장된 부분 문제의 해를 이용하여 상위 문제를 구함

- 피보나치 수 DP 적용 알고리즘

  ```python
  def fibo2(n):
      f = [0] * (n + 1)
      f[0] = 0
      f[1] = 1
      for i in range(2, n + 1):
          f[i] = f[i - 1] + f[i - 2]
          
      return f[n]
  ```

- memoization를 쓴

  ```python
  def fibo(n):
      if n < 2:
         	return memo
      else:
          if memo[n] == 0:
              memo[n] = fibo(n - 1) + fibo(n - 2)
  N = 30
  memo = [0] * (n + 1)
  memo[0] = 0
  memo[1] = 1
  cnt = 0
  print(fobo(n))
  ```

## DP 구현 방식

- recursive  방식: fib1()
- iterative 방식: fib2()
- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 효율적
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문



# DPS(깊이우선탐색)

- 비선형적인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
- 두 가지 방법
  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth First Search, BFS)
- 시작 정점의 한 방향으로 갈 수 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

## DFS 알고리즘

1. 시작 정점 v를 결정하여 방문

2. 정점 v에 인접한 정점 중에서

   1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push 하고 정점 w를 방문
   2. 그리고 w를 v로 하여 다시 반복
   3. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 반복

3. 스택이 공백이 될 때까지 방문

   ```python
   def dfs(n, V, adj_m):
       stack = [] # 스택 생성
       visited = [0] * (V + 1) # visited 생성
       visited[n] = 1 # 시작점 방문 표시
       print(n) # do(n)
       while True:
           for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w
               if adj_m[n][w] == 1 and visited[w] == 0:
                   stack.append(n) # push(n), v = w
                   n = w
                   print(n) # do(w)
                   visitend[n] = 1 # w 방문 표시
                   break
           else:
               if stack:# 스택에 지나온 정점이 남아 있으면
                   n = stack.pop() # pop()해서 다시 다른 w를 찾는다.
               else:
                   break
           return visited
   
   
   V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
   arr = list(map(int, input().split()))
   adj_m = [[0] * (V + 1) for _ in range(V + 1)]
   for i in range(E):
       v1, v2 = arr[i * 2], arr[i * 2 + 1]
       adj_m[v1][v2] = 1
       adj_m[v2][v1] = 1
       
   dfs(1, V, adj_m)
       
   ```

   