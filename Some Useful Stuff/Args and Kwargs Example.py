

x = 'Hey! This is x.'
y = 'Hey! This is y.'
z = 'Hey! This is z.'

def post_var(*args):
    for var in args:
        print(var)
        
post_var(x)

post_var(x,y,z)

def post_var_2(regular_arg, *args):
    print(regular_arg)
    for var in args:
        print(var)

post_var_2('My vars:',x,y,z)

def post_var_3(**kwargs):
    for key, var in kwargs.items():
        print(key,var)

post_var_3(x = 'Hey! This is x.',
             y = 'Hey! This is y.',
             z = 'Hey! This is z.')
