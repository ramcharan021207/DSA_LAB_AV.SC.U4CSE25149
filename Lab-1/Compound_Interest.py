def compound_interest(p,n):
    if n == 0:
        return 1
    else:
        return p*compound_interest(p,n-1)
print("Ramcharan AV.SC.U4CSE25149")
print(compound_interest(5,3))