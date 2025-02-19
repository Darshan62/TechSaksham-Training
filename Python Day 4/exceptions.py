#Division By zero Exception
def divide(a,b):
    try:
        result =a/b
    except ZeroDivisionError:
        return "Can't Divide by Zero"
    else:
        return result

print(divide(10,2))
print(divide(10,0))

