import time
from functools import wraps
from typing import Callable, List

def time_to_return(func:Callable) -> Callable:
    #@wraps(func)
    def wrapper(*agrs, **kwargs) -> None:
        t1:float = time.perf_counter()
        func(*agrs, **kwargs)
        t2:float = time.perf_counter()
        print(f"function {func.__name__} took {(t2 - t1):.3f}s to execute")
    return wrapper

@time_to_return
def weather_in_city(city:str, weather:str) -> None:
    #inserting some delay to measure time
    time.sleep(2)
    print (f"weather today in {city} is {weather}")

weather_in_city(city="San Franciso", weather="Windy")