import os
if __name__ == '__main__':
    def p_decorate(func):
        def func_wrapper(name1):
            return "<p>{0}</p>".format(func(name1))
        return func_wrapper

@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("john")



