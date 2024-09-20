x=input("Enter number1:")
y=input("Enter number2:")
try:
    # z=int(x) / int(y)
    z = int(x) / int(y)
# except Exception as e:
#     print("Exception occured:",e)
#     z=None
except ZeroDivisionError as a:
    print(a)
    z = None
# to know type of error to handle
# except Exception as e:
#      print("Exception Type:",type(e).__name__)
#      z = None

except TypeError as e:
     print(type(e).__name__)
     z = None
print("Division is:",z)