def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    check = {}
    lst = {}

    for port in report:
        a, b = port.split(' ')
        if b not in check:
            check[b] = 1
        else:
            check[b] += 1

        if a not in lst:
            lst[a] = [b]
        else:
            if b not in lst[a]:
                lst[a] += [b]

    for id, cnt in check.items():
        if cnt >= k:
            for user, user2 in lst.items():
                if id in user2:
                    answer[id_list.index(user)] += 1

    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)