# Tree  순회 방법

## 1. preorder (전위)

- 처음 지나갈 때 방문
- 자식노드를 좌, 우 순서로 방문

## 2. inorder (중위)

- 왼쪽에서 돌아올 때 방문
- 왼쪽 노드 방문
- 부모 노드 방문
- 오른쪽 자식 방문

## 3. postorder (후위)

- 오른쪽에서 돌아오면서 방문
- 자식 노드를 좌우로 방문하고 부모 노드를 방문

## 어디다 사용?

- 전위 순회
  - 루트 노드를 가장 먼저 방문하기 때문에, 트리의 구조를 파악하기 쉽다.
  - 트리의 레이아웃 파악, 복사, 트리의 균형 파악
- 중위 순회
  - 이진 트리에 많이 활용
  - 이진트리는 왼쪽 자식 노드의 크기가 나보다 작고, 오른쪽 자식 노드의 크기가 나보다 크기 때문
  - 이진트리의 값들을 정렬된 순서로 받아올 수 있다.
  - 빠른 검색: 정렬되어 있기 때문에 빠르게 검색할 수 있음
  - 정렬되지 않은 데이터를 가지고, 이진트리를 구성하면, 정렬된 효과를 얻을 수 있다.
- 후위 순회
  - 리프 노드에서부터 탐색을 시작하는 특징
  - 노드의 삭제와 삽입을 할 경우 자식 노드부터 처리할 수 있다.

# 트리 vs 그래프

## 그래프

- 정의: 노드와 간선으로 구성되는 자료구조
- 방향성: 방향 그래프 O, 무방향 그래프 O
- 루트 노드: X
- 부모 / 자식 관계: X

## 트리

- 정의: 그래프의 한 종류, 방향성이 있는 비순환 그래프
- 방향성: 방향 그래프 O, 무방향 그래프 X
- 루트 노드: O
- 부모 / 자식 관계: O