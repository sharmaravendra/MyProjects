#num=input("Enter a number: ")
#num=int(num)
#if num%2==0:
#    print("Number is even.")
#else:
#    print("Number is Odd.")
indian=["samosa","kachori","pavbhaji"]
chinese=["shushi","chin1"]
italian=["ital1","ital2"]
dish=input("Enter dish name:")
if dish in indian:
    print("The dish is India.")
elif dish in chinese:
    print("dish is chinese")
elif dish in italian:
    print("Dish is Italian")
else:
    print("List not defined")