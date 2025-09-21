import numpy as np

def lift(a,b):
    a_men=np.mean(a)
    b_men=np.mean(b)


    lift=(b_men-a_men) /a_men
    return str(round(lift*100))+"%"


