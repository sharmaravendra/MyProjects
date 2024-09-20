def process_file():
    try:
        f=open("D:\\Ravendra\\PycharmProjects\\pythonProject\\temp_files\\input.txt")
        x=1/0
    except FileNotFoundError as e:
        print("Inside except")
    # except ZeroDivisionError as e:
    #     print("Div by Zero")
    finally:
        print("cleaning up file")
        f.close()

process_file()
