# 5. Implementirati dekorator podeli koji ima jedan parametar sep.
# Ovaj dekorator modifikuje funkciju koja vraca string,
# tako sto rezultat deli po separatoru sep i vraca listu dobijenih stringova.

def divide(sep):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result.split(sep)
            else:
                raise ValueError("Must be string")

        return wrapper

    return decorator


@divide(sep=",")
def get_string():
    return "This,is,a,test,string"


@divide(sep=" ")
def get_other_string():
    return "This is a test string"


print(get_string())
print(get_other_string())
