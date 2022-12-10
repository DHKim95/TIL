def solution(elements):
    answer = []
    len_elements = len(elements)
    elements_two = elements*2
    
    for plus in range(1, len_elements+1):
        for start in range(len_elements):
            # print(elements_two[start:start+plus])
            answer.append(sum(elements_two[start:start+plus]))
    
    return len(set(answer))