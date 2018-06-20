password = ( 8, 4, 2, 6)


foundPassword = False;
for i in range(10):
    if foundPassword == True:
        break
    for j in range(10):
        if foundPassword == True:
            break
        for k in range(10):
            if foundPassword == True:
                break
            for l in range(10):
                if (i,j,k,l) == password:
                    print("Password found: {}".format((i,j,k,l)))
                    foundPassword = True
                    break
                
            
# Using a generator:

def generate_password():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    yield (i,j,k,l) 

for (i,j,k,l) in generate_password():
    if (i,j,k,l) == password:
        print("Password found: {}".format((i,j,k,l)))