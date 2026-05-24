def string_reversal(string):
    if  len(string) == 0:
        return string
    else:
        return string_reversal(string[1:]) + string[0]
    
string  = "Lary is learning Python"
reversed_string = string_reversal(string)
print(reversed_string)