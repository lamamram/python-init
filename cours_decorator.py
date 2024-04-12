# %%
# définition
# un décorateur est une fonction 
# qui prend en paramètre une fonction
# et qui retourne un fonction

def debug(f):
    # fonction wrapper qui redéfinit la fonciton en paramètre f
    # wrapper doit avoir une signature la plus générque possible
    def wrapper(*args, **kwargs):
        ret = f(*args, **kwargs)
        if "debug" in kwargs and kwargs["debug"]:
            print(locals())
        return ret
    return wrapper


