def solution(files):
    sub_answer = []
    
    for file in files:
        head, number, tail = "", "", ""
        check = False
        
        for i in range(len(file)):
            # 숫자가 나오면 숫자 꺼내기
            if file[i].isdigit():
                number += file[i]
                check = True
            # 첫번째 단어들 뽑아내기
            elif check == False:
                head += file[i]
            # 이어진 숫자가 끝나면 전부 다 tail로
            else:
                tail = file[i:]
                break
        
        sub_answer.append((head, number, tail))
        
        # 정렬 조건 해주기
        sub_answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
         
    answer = []
    for i in sub_answer:
        answer.append(''.join(i))
    
    return answer