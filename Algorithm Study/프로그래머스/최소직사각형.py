def solution(sizes):
    for size in sizes:
        size.sort(reverse=True)
    w, h = [], []
    for size in sizes:
        w.append(size[0])
        h.append(size[1])

    answer = max(w) * max(h)
    return answer