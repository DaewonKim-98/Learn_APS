# 문자열

## 문자의 표현

- 컴퓨터에서의 문자 표현
  - 글자 A를 메모리에 저장하는 방법
  - 메모리는 숫자만을 저장할 수 있기 때문에 각 문자에 맞는 숫자들을 저장
  - 네트워크가 발전되기 전 미국의 각 지역 별로 코드체계를 정해 놓고 사용
  - 혼동을 피하기 위해 표준안으로 아스키 코드 문자 인코딩 표준 제정
  - ASCII는 128 문자를 표현
  - 확장 아스키는 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 기호 등 부가적인 문자 추가
  - 각 나라에서 자국의 문자를 표현하기 위해 코드를 만들었는데
  - 서로 다른 국가 간에 정보를 주고받을 때 문제 발생
  - 다국어 처리를 위해 표준을 마련했고 이걸 **유니코드**라 한다.

### 유니코드 인코딩

- UTF-8(in web)
  - MIN: 8bit, MAX: 32bit(1 byte *4)
- UTF-16(in windows, java)
  - MIN: 16bit, MAX: 32bit(2 byte *4)
- UTF-3(in unix)
  - MIN: 32bit, MAX: 32bit(4 bAyte *1)

### phton 인코딩

- 2.x 버전 - ASCII -> #-*- coding: utf-8 -*- (첫줄에 명시)
- 3.x버전 - 유니코드 UTF-8 -> 생략가능



## 문자열

- fixed length
- variable length
  - lenth controlled(Java)
  - delimited(C 언어)

- pythono에서의 문자열 처리
  - 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음



## 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법

  - ```python
    s = 'Reverse'
    s_lst = list(s)
    N = len(s)
    
    for i in range(N // 2):
        s_lst[i], s_lst[N - 1 - i] = s_lst[N - 1 - i], s_lst[i]
        
    s = ''.join(s_lst)
    ```



## 문자열 숫자를 정수로 변환하기

- int() 와 같은 atoi() 함수 만들기

  - ```python
    def atoi(s):
        i = 0
        for x in s:
            i = i*10 + ord(x) - ord('0')
        return i
    
    s = '123'
    a = atoi(s)
    print(a + 1)
    ```

  - 