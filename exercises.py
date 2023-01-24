weight = float(input("Weight: "))
kg_or_lb = input("(K)g or (L)bs: ")
if kg_or_lb == "k":
    weight = weight
    print("Weight in Kg: "+weight)
elif kg_or_lb == "l":
    weight = weight * 2.2
    print("Weight in Lbs: "+str(weight))
else:
    print("not defined")
