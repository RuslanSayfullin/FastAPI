#!/usr/bin/python3

def benchmark(items):
    def other_func(func):
        def wrapper(*args, **kwargs):
            import time
            total = 0
            for i in range(items):
                start = time.time()
                return_value = func(*args, **kwargs)
                stop = time.time()
                total += (stop-start)
            print(f"Время выполнения запроса{total/items}")
            return return_value
        return wrapper
    return other_func


@benchmark(items=10)
def get_webpage(url: str) -> str:
    import requests
    page = requests.get(url)
    return page.status_code


example_url = "https://www.google.com"
webpage = get_webpage(example_url)
print(webpage)