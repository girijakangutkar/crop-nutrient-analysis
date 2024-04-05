import serial
import time

"""
def getsensordata():
    print("---------Reading collection starts now----------")
    sr = serial.Serial("com10",9600)
    st = list(str(sr.read(),'utf-8'))
    sr.close() 
    print("------Reading collection ends successfully------")
    return int(str(''.join(st[:])))
"""
def getsensordata():
    ser=serial.Serial("com10",9600)
    data = []
    for i in range(5):
        b = ser.readline()
        string_n = b.decode()
        string =string_n.rstrip()
        flt = float(string)
        data.append(string)
        time.sleep(0.1)
    ser.close()
    print(data)    