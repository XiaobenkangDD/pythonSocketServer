import struct

def strToFloat(s):
    temp=str(s)
    temp=temp.replace(" ","")
    temp=temp[6:8]+temp[4:6]+temp[2:4]+temp[0:2]
    return struct.unpack('<f', bytes.fromhex(temp))[0]

'''
bytes to hex string 
16进制数组转为字符串
'''
def bytesToHexString(bs):
    result=""
    if len(bs):
        result = ''.join(['%02X ' % b for b in bs])
        result = result.replace(" ", "")
    return result





