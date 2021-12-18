genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []

    dic_index = {}
    dic_sum = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic_index:
            dic_index[genre] = [(idx, play)]
        else:
            dic_index[genre].append((idx, play))

        if genre not in dic_sum:
            dic_sum[genre] = play
        else:
            dic_sum[genre] += play
    # print(dic_index)
    # print(dic_sum)

    for(key, value) in sorted(dic_sum.items(), key=lambda x: x[1], reverse=True):
        for (i, play) in sorted(dic_index[key], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

print(solution(genres,plays))