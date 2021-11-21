names = ["azad","andy","louis","will","edward"]
homes = [[3,4],[-1,5],[-4,4],[3,4],[-5,0]]
grades = [4.19, 3.77, 4.41, 3.65, 3.58]

def solution(names, homes, grades):
    answer = []
    sort_people = []
    for name, home, grade in zip(names, homes, grades):
        sort_people.append((name, home, grade))

    sort_people = sorted(sort_people, key=lambda x: (-int(x[2]), -(x[1][0] ** 2 + x[1][1] ** 2), x[0]))

    for name in names:
        for people in range(len(sort_people)):
            if name == sort_people[people][0]:
                answer.append(people+1)
                break

    return answer

print(solution(names, homes, grades))