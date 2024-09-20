book={}
book['tom']={
    'name':'tom',
    'address':'1-hop street qld',
    'phone':33207106
}
book['rav']={
    'name':'rav',
    'address':'doha qatar',
    'phone':22456798
}

import json
# s=json.dumps(book)
# print(s)
# with open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\book.txt","w") as f:
#     f.write(s)
f=open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\book.txt","r")
s=f.read()
print(s)
print(type(s))
book=json.loads(s)
# print(book)
# print(type(book))
for person in book:
    print(person)