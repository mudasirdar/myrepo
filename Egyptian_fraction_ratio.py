 
# Python3 program to print a Ratio of Egyptian Fraction 
import math
 
   
def ratioOfegyptianFraction(nr, dr): 
   
    print("The Ratio of Egyptian Fraction " +
          "Representation of {0}/{1} is".format(nr, dr), end="\n") 
   
    ef = [] 
   
    while nr != 0: 
   
        x = math.ceil(dr / nr) 
   
        ef.append(x) 
   
        nr = x * nr - dr 
        dr = dr * x 
   
    for i in range(len(ef)): 
        if i != len(ef) - 1: 
            print(" 1/{0} :" .  
                    format(ef[i]), end = " ") 
        else: 
            print(" 1/{0}" . 
                    format(ef[i]), end = " ") 
   

ratioOfegyptianFraction(6, 14) 



