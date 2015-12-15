import json
def init_dcl(shell, fil):
    fil = json.loads(open(fil).read())
    for d in fil: 
        module = getattr(shell.module, d)
        for f in fil[d]: shell.add_macro(f, getattr(module, fil[d][f]))
