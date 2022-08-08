ipv6 = input().split(':')

# 갯수 채워주기
if ipv6.count(''):
    while len(ipv6) > 8:
        del ipv6[ipv6.index('')]
    while len(ipv6) < 8:
        ipv6.insert(ipv6.index(''), '0000')

for i in range(8):
    if len(ipv6[i]) < 4:
        ipv6[i] = '0' * (4-len(ipv6[i])) + ipv6[i]

print(*ipv6, sep=':')