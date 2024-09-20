# f=open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\funny.txt","a")
# f.write("\nI LOVE C++")
# f.close()
# Read file line by line
f=open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\funny.txt","r")
# whole file read.
# print(f.read())
# Read line by line
f_out=open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\funny_out.txt","w")
for line in f:
    tokens=line.split(' ')
    # f_out.write("No. of Words:"+str(len(tokens))+" "+line)
    print(tokens)
    # print(tokens,len(tokens))
f.close()
f_out.close
