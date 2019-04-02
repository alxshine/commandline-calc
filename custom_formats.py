def get_num_bits(v):
    return len(bin(v))-2

def get_num_bytes(v):
    num_bits = get_num_bits(v)
    return num_bits//8 + (num_bits%8 > 0)

hex_digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def format_hex(v):
    num_bytes = get_num_bytes(v)
    mask = 0xf
    ret = ""
    for i in range(8*num_bytes-4, -1, -4):
        current_mask = mask << i
        bits = v & current_mask
        ret += hex_digits[bits >> i]

        if i % 8 == 0 and i > 0:
            ret += ' '
    return ret

def format_bin(v):
    ret = ''
    for i in range(get_num_bits(v)-1, -1, -1):
        bit = (v & (1<<i)) >> i
        ret += str(bit)
        if i % 8 == 0 and i > 0:
            ret += ' '
    return ret

if __name__ == "__main__":
    print(format_bin(0xff00ff))
