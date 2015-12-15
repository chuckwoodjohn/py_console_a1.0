class Macro:
    def __init__(self, call, func):
        self.call = call
        self.func = func
        
    def __call__(self, shell, *args, **kwargs):
        self.func(shell, *args, **kwargs)
