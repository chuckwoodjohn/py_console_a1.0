import json
__AUTHOR__ = "chuckwoodjohn"
__VERSION__ = "A.1.0"
__DATE__ = "12.15.15"

from console_a10 import dcl, stream, macro
import sys
class Shell:
    def __init__(self, module=sys.modules[__name__], dcls=[], sttngs={}, sfiles=[]):
        self.init_vars()
        self.module = module
        self.init_dcls(dcls)
        self.init_sttngs(sttngs)
        self.init_sfiles(sfiles)
    def init_vars(self):
        self.macros = []
        self.settings = {}
        self.set_setting("RUN", True)
        self.outstream = stream.Stream()
        self.instream = stream.Stream()
        self.add_out = self.outstream.push
        self.show = self.outstream.show_unaccs
        self.get_input = self.instream.get_input
        self.get_last = self.instream.get_last
    def init_dcls(self, dcls):
        for d in dcls: dcl.init_dcl(self, d)
    def init_sttngs(self, sttngs):
        for s in sttngs: self.set_setting(s, sttngs[s])
    def init_sfiles(self, sfiles):
        for s in sfiles: 
            s = json.loads(open(s).read())
            for v in s: self.set_setting(v, s[v])
    def set_setting(self, set, val): self.settings[set] = val
    def get_setting(self, set): return self.settings[set]
    def add_macro(self, call, func): self.macros.append(macro.Macro(call, func))
    def run_macro(self, call, *args, **kwargs): 
        for m in self.macros:
            if m.call == call: m(self, *args, **kwargs); return True
        return False
    def run_input(self):
        inpt = self.get_last().get().split()
        call = inpt.pop(0)
        self.run_macro(call, *inpt)
    def mainloop(self):
        while self.get_setting("RUN"): 
            self.show()
            self.get_input(">>> ")
            self.run_input()
    
        
