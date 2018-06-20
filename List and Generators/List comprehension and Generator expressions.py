#List - Time efficient, uses space
#Generators - Space efficient, takes time

lis = [i for i in range(5)]    # [] -> List
print(lis)
gen = (i for i in range(5))    # () -> Generator 
print(gen)



inputList = [10,200,30,45,418,346,769,84,17,25]

def less_than_100(num):
    if num < 100:
        return True
    else:
        return False;

lis2 = [i for i in inputList if less_than_100(i)]
print(lis2)

gen2 = (i for i in inputList if less_than_100(i))
# This is similar to -
#    gen2 = []
#    for i in inputList:
#        if less_than_100(i):
#            gen2.append(i)

[print(i) for i in gen2]
(print(i) for i in gen2)  #Does not print anything because it is a generator
