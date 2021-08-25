front = rear = 0
N = 10 # Q size
Q = [0] * N


def enqueue(item):
    global rear # 밖에 있는 rear랑 같은것이라고 표현
    # is_full 검사 필요
    if (rear + 1) % N == front:
        print("너 가득차서 못 넣어")
    else:
        rear = (rear + 1) % N
        Q[rear] = item

def dequeue():
    global front
    # is_empty 필요
    if front == rear:
        print("비어서 꺼낼것이 없다.")
    else:
        front = (front + 1) % N
        return Q[front]

# enqueue(1)
# enqueue(2)
# enqueue(3)
#
# print(dequeue())
# print(dequeue())
# print(dequeue())
# print(dequeue())

for i in range(100000):
    enqueue(i)

for i in range(100000):
    print(dequeue())
