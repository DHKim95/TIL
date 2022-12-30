from itertools import combinations


def solution(relation):
    # 세로 원소 다넣기
    rel_transpose = []
    for i in zip(*relation):
        rel_transpose.append(tuple(i))

    # all_len = len(relation) # 전체 행 길이
    col_len = len(relation[0])  # 전체 열 길이

    answer = []
    # 조합 수 만들기
    cand = []
    for num in range(1, col_len + 1):
        # append, extend ...
        cand.extend(set(combinations(range(col_len), num)))

    # 열별로 정리
    for can in cand:
        database = [rel_transpose[idx] for idx in can]
        zip_database = list(zip(*database))

        # 유일성 테스트 다르면 컷, 중복제거
        if len(zip_database) != len(set(zip_database)):
            # print(zip_database, set(zip_database))
            continue

        # 최소성
        for item in answer:
            # print("본다", item, can)
            # print("여기",set(item).intersection(set(can)), set(item))
            # 가져온거에서 현재조합뺀건데 같으면 중복이니깐 넘기기
            if set(item).intersection(set(can)) == set(item):
                break
        # 다 만족하면 조건충족 추가
        else:
            answer.append(can)

    return len(answer)