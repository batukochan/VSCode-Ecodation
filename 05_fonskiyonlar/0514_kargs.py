"""
def pDilleri(**kargs):
    print(type(kargs))
    for key, value in kargs.items():
        print(f"{key}-{value}")


pDilleri(
    programlamaDili="python",
    seviye="yüksek",
    interpreter=True,
    versiyon=3.64
)
"""
"""
dilPython = {
    "programlamaDili": "python",
    "seviye": "yüksek",
    "interpreter": True,
    "versiyon": 3.64
}

dilCSharp = {
    "programlamaDili": "C#",
    "seviye": "yüksek",
    "interpreter": False,
    "versiyon": 8.0
}

"""
"""
def dilBilgisi(dil):
    print(f"{dil['dilPython']}")


diller = {
    dilPython: {
        "programlamaDili": "python",
        "seviye": "yüksek",
        "interpreter": True,
        "versiyon": 3.64
    }

    dilCSharp: {
        "programlamaDili": "C#",
        "seviye": "yüksek",
        "interpreter": False,
        "versiyon": 8.0
    }
}
dilBilgisi(diller)
"""
