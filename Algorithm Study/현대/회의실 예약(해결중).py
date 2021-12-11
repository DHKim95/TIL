# N은 회의실 수, M은 예약된 회의 수
N, M = map(int, input().split())
room = {}

for _ in range(N):
    room_name = input()
    room[room_name] = [[num, num+1] for num in range(9,18)]

for _ in range(M):
    name, start, end = input().split()

    for i in range(int(start), int(end)):
        if [i, i+1] not in room[name]:
            pass
        else:
            room[name].remove([i,i+1])

# print(room)
for people in sorted(room.keys()):
    if len(room[people]) == 0:
        print("Room" , people + ":")
        print("Not available")

        if people == sorted(room.keys())[-1]:
            break
        else:
            print('-----')
        continue
    else:
        sub_lst = []
        answer = []
        for i in range(len(room[people])):
            print(i)
