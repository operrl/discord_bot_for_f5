import os
try:
    import nacl
except ImportError:
    try:
        if os.name == 'nt':
            os.system("py -m pip install pynacl")
        else:
            os.system("python3 -m install pynacl")
    except Exception as e:
        print("Error:", e)
        exit()