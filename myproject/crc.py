def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def crc_division(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    return tmp

def encode_data(data, key):
    key_len = len(key)
    appended_data = data + '0' * (key_len - 1)
    remainder = crc_division(appended_data, key)
    codeword = data + remainder
    return codeword

def check_data(received, key):
    remainder = crc_division(received, key)
    if "1" in remainder:
        print("Error detected in data!")
    else:
        print("No error detected (data is correct).")

data = "1101011011"
key = "10011"

print("Original Data:", data)
codeword = encode_data(data, key)
print("CRC Codeword:", codeword)

received_data = "11010110111110"
check_data(received_data, key)

received_data = "11010110111111"
check_data(received_data, key)
