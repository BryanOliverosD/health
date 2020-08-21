import sys
from itertools import cycle
def validateRut(rut):
    try:
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux_rut = rut[:-1]  
        digit_verifier = rut[-1:]

        reverse = map(int, reversed(str(aux_rut)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(reverse,factors))
        remainder = (-s)%11

        if str(remainder) == digit_verifier:
            return True
        elif digit_verifier=="K" and remainder==10:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def validateDose(dose):
    if 0.15 <= dose <= 1.0:
        return True
    else:
        return False

def validateSize(element, maximum):
    if len(element) > maximum:
        return True
    else:
        return False