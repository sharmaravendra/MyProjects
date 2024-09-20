
def calc_triangle_area(base,height):
    return 1/2*(base*height)

def calc_square_area(length,height):
    return length*height
def fun_countNum(num):
     with open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\input.txt") as f:
         cnt=0
         for line in f:
             if str(num) in line:
                 # print(line)
                 cnt=cnt+1
     return str(num)+" Appeared "+str(cnt)+" times"
# def fun_countNum(num):
#     with open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\input.txt") as f:
#         for line in f:
#             numbers = line.split(',')
#             clean_text=line.replace("\n", "")
#             print("Sum",int(clean_text[0])+int(clean_text[2]),"|",line)
#     return 1
