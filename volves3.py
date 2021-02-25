volwes=['a', 'i','o', 'u','e']
word=input("Введи слово: ")
answer=[]
dict_latter={}
for latter in word:
    if latter in volwes:
        if latter not in answer:
            dict_latter[latter]=1
            answer.append(latter)
        else:
            dict_latter[latter]+=1
for k,v in sorted(dict_latter.items()):
    print(k, v)
