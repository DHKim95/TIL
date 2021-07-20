# 인덱스 활용
site = input()

protocol = site[:4]
host = site[7:22]
other = site[23:]
print(f"protocol: {protocol}")
print(f"host: {host}")
print(f"others: {other}")