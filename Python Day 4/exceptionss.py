def divide(a,b):
    try:
        result =a/b
    except TypeError:
        return "You have to enter a Number Not a String"
    
    except ZeroDivisionError:
            return "Can't Divide by Zero"
    else:
        return result
    finally:
        print("I am running Always")
        
print(divide(10,0))
print(divide("dsaj",2))
        