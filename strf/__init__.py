import inspect
def strf(s): return s.format(**inspect.currentframe().f_back.f_locals)