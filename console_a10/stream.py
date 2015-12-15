class StreamObject:
    def __init__(self, data=None): self.data = data; self.accs = False
    def is_accs(self): return self.accs
    def get(self, accs=True): self.accs = accs; return self.data
    def show(self, accs=True): print(self.get(accs))

class Stream:
    def __init__(self): self.stream = []
    def get_last(self): return self.stream[-1]
    def get_unaccs(self): 
        for s in self.stream: 
            if not s.is_accs(): yield s
    def show_last(self): self.get_last().show()
    def show_unaccs(self): 
        for s in list(self.get_unaccs()): s.show()
    def push(self, data): self.stream.append(StreamObject(data))
    def get_input(self, prompt=None): self.push(raw_input(prompt))
