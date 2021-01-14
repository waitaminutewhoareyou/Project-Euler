def cancelQ(argument):
    numerator, denominator = argument
    if numerator == denominator:
        return False
    if not (10<= numerator <= 99) and ( 10<= denominator <= 99):
        raise Exception("OOD")
    numerator = str(numerator)
    denominator = str(denominator)
    if '0' in numerator or '0' in denominator:
        return False
    intersection = set(numerator) & set(denominator)

    if len(intersection)> 0:
        try:
            new_numerator = (set(numerator)- intersection).pop()
            new_denominator = (set(denominator)- intersection).pop()
            outcome = int(numerator)/int(denominator) == int(new_numerator)/int(new_denominator)
        except (KeyError, ZeroDivisionError):
            return False
        return outcome
    else:
        return False

space = [(i,j) for  i in range(10,100) for j in range(10, i)]

res = list(filter(cancelQ, space))
print(res)

