
import math as mt
#import numpy as np

def seq(n):
    pii=0
    for i in range(n):
        pii += mt.sqrt(12) * pow(-1,i) / ((2*i + 1)*pow(3,i))
    return pii
print ('the value of pi is : ',seq(3),'the error is : ',abs(seq(3)-mt.pi))
