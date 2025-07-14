#!/usr/bin/python3

def bencmark(iterator):
    def realdec(func):
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            return_data = func(*args, **kwargs)
            stop = time.time()
            print(f"Вреся работы функции {stop-start} с переменной{iterator}")
            return return_data
        return wrapper
    return realdec

@bencmark(iterator=10)
def get_response():
    import requests

    result = requests.get("http://www.google.com")
    return result

iteration = get_response()

print(iteration)
