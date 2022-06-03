class MyCustomError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr("Log Not Found")

try:
    raise MyCustomError(3*2)
    
except MyCustomError as m:
    print(f"User Defined Exception: {m}")