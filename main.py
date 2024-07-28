"""
1. The program accepts from the user ranges for the coefficients a, b, c of the quadratic equation: ax2 + bx + c = 0.
It goes through all the variants of integer

coefficients in the specified ranges, determines quadratic equations that have a solution
"""


import import_table as values




def roots():
    a1=values.income_values("a lower")
    a2=values.income_values("a upper")
    b1=values.income_values("b lower")
    b2=values.income_values("b upper")
    c1=values.income_values("c lower")
    c2=values.income_values("c upper")



    if a2>a1 and b2>b1 and c2>c1:
        #check for correct start/stop limits
        for a in range(a1,a2+1):
            for b in range(b1,b2+1):
                for c in range(c1,c2+1):
                    if a!=0:
                        D=b**2-4*a*c
                        if D<0:
                            print(f'{a},{b},{c} NO')
                        elif D==0:
                            root=-b/(2*a)
                            print(f'{a},{b},{c} Yes {round(root,2)}')
                        else:
                            root1=(-b+(D**0.5))/(2*a)
                            root2=(-b-(D**0.5))/(2*a)
                            print(f'{a} ,{b} ,{c} Yes {round(root1,2)},{round(root2,2)}')
                    else:
                        root=-(c/b)
                        print(f'{a}, {b}, {c} equation is linear {round(root,2)}')
    else:
        return print("please enter correct limits")
    return print("Get yor results:)")
roots()
