# S DES method
def apply_table(inp, table):
    """
    >>> apply_table("0123456789", list(range(10)))
    '9012345678'
    >>> apply_table("0123456789", list(range(9, -1, -1)))
    '8765432109'
    """
    res = ""
    for i in table:
        res += inp[i - 1]
    return res


def left_shift(data):
    """
    >>> left_shift("0123456789")
    '1234567890'
    """
    return data[1:] + data[0]


def xor(a, b):
    """
    >>> xor("01010101", "00001111")
    '01011010'
    """
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res


def apply_sbox(s, data):
    row = int("0b" + data[0] + data[-1], 2)
    col = int("0b" + data[1:3], 2)
    return bin(s[row][col])[2:]


def function(expansion, s0, s1, key, message):
    # print(message)
    left = message[:4]
    # print("left", left)
    right = message[4:]
    # print("right", right)
    temp = apply_table(right, expansion)
    # print("right", temp)
    temp = xor(temp, key)
    # print("xor right", temp)

    left_bin_str = apply_sbox(s0, temp[:4])
    # print("left_bin_str", left_bin_str)

    right_bin_str = apply_sbox(s1, temp[4:])
    # print("right_bin_str", right_bin_str)

    left_bin_str = "0" * (2 - len(left_bin_str)) + left_bin_str
    right_bin_str = "0" * (2 - len(right_bin_str)) + right_bin_str
    temp = apply_table(left_bin_str + right_bin_str, p4_table)
    # print("p4", temp)
    temp = xor(left, temp)
    # print("sw", temp)
    # print(temp + right)
    return temp + right


if __name__ == "__main__":
    key = "1010110110"
    message = "01000110"

    p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
    p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p4_table = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    expansion = [4, 1, 2, 3, 2, 3, 4, 1]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    # print(s0)
    # print(s1)
    # key generation
    temp = apply_table(key, p10_table)
    left = temp[:5]
    # print("left", left)
    right = temp[5:]
    # print("right", right)
    left = left_shift(left)
    # print("left", left)
    right = left_shift(right)
    # print("right", right)
    key1 = apply_table(left + right, p8_table)
    # print("key1", key1)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    # print("left", left)
    right = left_shift(right)
    # print("right", right)
    key2 = apply_table(left + right, p8_table)
    # print("key2", key2)
    # encryption
    temp = apply_table(message, IP)
    temp = function(expansion, s0, s1, key1, temp)
    temp = temp[4:] + temp[:4]
    # print("sw swap", temp)
    temp = function(expansion, s0, s1, key2, temp)
    # print("ip before inverse", temp)
    CT = apply_table(temp, IP_inv)
    print("ip^-1", CT)
    # # decryption
    # temp = apply_table(CT, IP)
    # temp = function(expansion, s0, s1, key2, temp)
    # temp = temp[4:] + temp[:4]
    # temp = function(expansion, s0, s1, key1, temp)
    # PT = apply_table(temp, IP_inv)
    # print("Plain text after decypting is:", PT)
