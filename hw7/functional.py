def sequential_map(*args):
    container = list(args[-1])
    functions = args[0:(len(args)-1)]
    for function in functions:
        container = list(map(function, container))
    return container

def consensus_filter(*args):
    container = list(args[-1])
    functions = args[0:(len(args)-1)]
    for function in functions:
        container = list(filter(function, container))
    return container

def conditional_reduce(fun1, fun2, container):
    # Создадим функцию reduce вместо импорта из functools    
    def reduce(function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
        else:
            value = initializer
        for element in it:
            value = function(value, element)
        return value
    # Проведем операции с нашей функцией
    container_fun1 = list(filter(fun1, container))
    container_fun2 = reduce(fun2,container_fun1)
    return container_fun2

def func_chain(*args):
    def chain(value):
        for function in args:
            value = function(value)
        return value
    return chain

def sequential_map2(*args):
    container = list(args[-1])
    functions = func_chain(*args[0:(len(args)-1)])
    return functions(container)

# Создадим функцию partial вместо импорта из functools 
def partial(func, /, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

def multiple_partial(*args, **values):
    result = []
    for function in args:
        result.append(partial(function, **values))
    return result

