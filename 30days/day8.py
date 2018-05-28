#Dicionários
#Lista telefônica

n = int(input())

telefones = {}

for t in range(n):
    new_tel = input().split()
    new_data = [x for x in new_tel]
    telefones[new_data[0]] = new_data[1]
    
while True:
    name = input()
    if name in telefones:
        print(name + "=" + telefones[name])
    else:
        print("Not found")
