def my_func(x1, x2, x3):
    try:
     if (not isinstance(x1, float)) or (not isinstance(x2, float)) or (not isinstance(x3, float)):
           return ("Error: parameters should be float")
     number = (x1+x2+x3)*(x2+x3)*x3
     denominator = x1+x2+x3
     value = float(number/denominator)
     return value
    except:
        return ("Not a number – denominator equals zero")

def convert(hours, minutes):
    if hours < 0 or minutes < 0:
            return "Error: parameters should be positive"
    shours = hours * 3600
    sminutes = minutes * 60
    sec = shours+sminutes
    return sec


