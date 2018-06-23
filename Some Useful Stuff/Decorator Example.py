from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style,str(item()))
        return wrapped_item
    return add_wrapping

#@add_wrapping
@add_wrapping_with_style('horribly')
@add_wrapping_with_style('beautifully')
def new_anime():
    return 'a new Anime!'

print(new_anime())
print(new_anime.__name__)