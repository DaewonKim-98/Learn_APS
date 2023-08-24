# 비트 연산 예제 2

```python
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output, end='')
a = 0x10
x = 0x01020304
for i in range(0, 4):
    Bbit_print((x >> i * 8) & 0xff)
```

- 엔디안(Endianness)
  - 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법을 의미하며 HW 아키텍처마다 다르다.
  - 주의: 속도 향상을 위해 바이트 단위와 워드 단위를 변환하여 연산할 때 올바르게 이해하지 않으면 오류를 발생시킬 수 있다.
  - 엔디안은 크게 두 가지로 나뉨 0x1234의 표현
    - 빅 엔디안(Big-endian)
      - 보통 큰 단위가 앞에 나옴, 네트워크
      - 12 34
    - 리틀 엔디안(Little-endian)
      - 작은 단위가 앞에 나옴, 대다수 데스크탑 컴퓨터
      - 34 12

# 진수

- 2진수, 8진수, 10진수, 16진수

- 10진수 -> 타 진수로 변환

  - 원하는 타진법의 수로 나눈 뒤 나머지를 거꾸로 읽는다.

  ```python
  bit = [0] * 8
  a = 149
  i = 7
  while a > 0:
      bit[i] = a % 2
      a //= 2
      i -= 1
      
  print(bit)
  print(''.join(map(str, bit)))
  ```

- 타 진수 -> 10진수로 변환

  - 제곱수를 이용