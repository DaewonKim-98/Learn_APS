# 스택

- 스택의 특성

  - 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료 구조
  - 스택에 저장된 자료는 선형 구조를 갖는다.
    - 자료 간의 관계가 1대 1의 관계를 갖는다.
  - 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
  - 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(Last in First Out)
    - 1, 2, 3으로 자료를 삽입한 수 꺼내면 3, 2, 1로 꺼낼 수 있다.

- 스택의 구현

  - 스택을 프로그램에서 구현하기 위해 필요한 자료구조와 연산

    - 자료구조: 자료를 선형으로 저장할 저장소
    - 배열을 사용할 수 있다.
    - 저장소 자체를 스택이라 부르기도 한다.
    - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.

  - 연산

    - 삽입: 저장소에 자료를 저장한다. 보통 push 라고 부른다.
    - 삭제: 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순, pop으로 부른다.
    - 스택이 공백인지 아닌지를 확인하는 연산: isEmpty
    - 스택의 top에 있는 item(원소)을 반환하는 연산: peek

  - 스택의 push 알고리즘

    - append 메소드를 통해 리스트의 마지막에 데이터를 삽입

    - ```python
      def push(item):
          s.append(item)
      ```

    - ```python
      def push(item, size):
          global top
          top += 1
          if top == size:
              print('overflow!')
          else:
              stack[top] = item
              
      size = 10
      stack = [0] * size
      top = -1
      
      push(10, size)
      top += 1
      stack(top) = 20
      ```

  - 스택의 pop 알고리즘

    - ```python
      def pop():
          if len(s) == 0:
              return True
          else:
              return s.pop()
      ```

    - ```python
      def pop():
          global top
          if top == -1:
              print('underflow!')
              return 0
          else:
              top -= 1
              return stack[top + 1]
              
      print(pop())
      
      if top > -1:
          top -= 1
          print(stack[top + 1])
      ```

- 스택 구현 고려 사항

  - 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다.
  - 이를 해결하는 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다.
  - 동적 연결리스트를 이용하여 구현하는 방법을 의미
  - 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점



## 스택의 응용1 : 괄호검사

- 괄호의 종류: 대괄호[], 중괄호{}, 소괄호()
- 조건
  - 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
  - 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
  - 괄호 사이에는 포함 관계만 존재
- 괄호를 조사하는 알고리즘
  - 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입하고, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지 검사
  - 스택이 비어 있으면 조건 1 또는 조건 2에 위배되고 괄호의 짝이 맞지 않으면 조건 3에 위배
  - 마지막 괄호까지를 조사한 후에도 스택에 괄호가 남아 있으면 조건 1에 위배



## 스택의 응용:  function call

- 함수 호출과 복귀에 따른 전체 프로그램의 수행 순서
- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로 스택을 이용해 수행 순서 관리
  - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
  - 함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제하면서 프레임에 저장되어 있던 복귀 주소를 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

## 재귀호출

- 자기 자신을 호출하여 순환 수행되는 것

- 함수에서 실행해야 하는 작업의 특성을 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성

- 피보나치 수를 구하는 재귀함수

  - ```python
    def fibo(n):
        if n < 2:
            return n
        else:
            return fibo(n - 1) + fibo(n - 2)
    ```

  - 이 알고리즘은 엄청난 중복 호출이 있다는 문제점

## Memoization

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 것

- '메모리에 넣기'라는 의미

- 피보나치 수를 구하는 알고리즘에서 fibo(n) 을 계산하자마자 저장하면 실행시간을 O(n)으로 줄임

  - ```python
    # memo를 위한 배열을 할당하고, 모두 0으로 초기화
    # memo[0]을 0으로 memo[1]는 1로 초기화
    
    def fibo1(n):
        global memo
        if n >= 2 and memo[n] == 0:
            memo[n] = (fibo1(n - 1) + fibo1(n - 2))
        return memo[n]
    
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    ```

  - 