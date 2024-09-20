a=["hey","bro","you'r","awesome"]
# for i in a:
#     print(i)

# print(dir(a))
itr=iter(a)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# for element in [1,2,3]:
#     print(element)
# for element in (1,2,3):
#     print(element)
for key in {'one':1,'two': 2,'three': 3}:
    print(key)
for char in "123":
    print(char)
for line in open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\input.txt"):
    # print(line,end='')
    print(line)
#Reverse iterator
itr=reversed(a)
print(next(itr))
