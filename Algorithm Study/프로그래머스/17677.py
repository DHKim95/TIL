def solution(str1, str2):
    answer = 0

    # 대소문자 통일
    str1 = str1.lower()
    str2 = str2.lower()

    list1, list2 = [], []
    # 다중집합원소 만들기
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            list1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            list2.append(str2[i:i + 2])

    if len(list1) == 0 and len(list2) == 0:
        answer = 1
    else:
        gyo_lst, hap_lst = [], []
        gyo = set(list1) & set(list2)
        hap = set(list1) | set(list2)

        for g in gyo:
            gyo_lst.append(min(list1.count(g), list2.count(g)))
        for h in hap:
            hap_lst.append(max(list1.count(h), list2.count(h)))

        answer = sum(gyo_lst) / sum(hap_lst)

    answer = answer * 65536

    return int(answer)