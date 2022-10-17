def mi_funcion(param1, param2):
    return 'hola {} {}'.format(param1, param2)


def logger(fn_to_decorate):
    def wrapper(*args, **kwargs):
        print("Function %s called with arguments: %s, %s" % (fn_to_decorate.__name__, args, kwargs))
        return fn_to_decorate(*args, **kwargs)
    
    return wrapper


my_logger = logger(mi_funcion)
print(my_logger("Jon", "Snow"))