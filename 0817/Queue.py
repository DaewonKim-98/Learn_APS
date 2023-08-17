class LinearQueue:
    def __init__(self, size):
        self.size = size # q의 용량 초기화
        self.queue = [None] * size
        self.front = self.rear = -1

    # 공백 상태
    def is_empty(self):
        return self.front == -1 # front -1이면 q가 공백상태

    # 포화 상태
    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, item):
        if self.is_full(): # 포화 상태 체크
            print('현재 큐가 포화 상태입니다.')
            return
        elif self.is_empty():
            self.front = self.rear = 0
        self.rear = self.rear + 1 # rear 값을 다음으로 이동
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print('현재 큐가 비어있습니다.')
            return None
        item = self.queue[self.front] # front 아이템 반환
        # deq 아이템 하나 남은 경우, 큐를 초기화 해준다.
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = self.front + 1
        return item