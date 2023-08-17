class CircleQueue:
    def __init__(self, size):
        self.size = size # q의 용량 초기화
        self.queue = [None] * size
        self.front = self.rear = 0

    def is_empty(self):
        if self.front == self.rear
            return True
        return False

    def enq(self):
        if self.is_full():
            raise Exception('Queue is Full!!')
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = self.item


    def deq(self):
        if self.is_empty():
            raise Exception('Queue is emptyD')
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]

