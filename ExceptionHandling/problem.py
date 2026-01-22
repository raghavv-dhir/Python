def ErrHandle():
    try:
        print("I am here, opening all the files")
        return
    except ZeroDivisionError as e:
        print(e)
    finally: #It will even run if return is there (because finally block runs in every condition)
        print("Closing all the files")

ErrHandle()
