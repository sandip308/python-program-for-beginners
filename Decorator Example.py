def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Congrats")
        else:
            result_function(marks)
    return distinction

@decor_result

def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")
result([50,60,15,90,66])
