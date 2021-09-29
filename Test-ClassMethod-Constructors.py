# Additional Constructors

@classmethod
def fromtimestamp(cls, t):
    #"Construct a date from POSIX timestamp (like time.time())."
    y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
    return cls(y, m, d)

@classmethod
def today(cls):
    #"Construct a date from time.time()."
    t = _time.time()
    return cls.fromtimestamp(t)

