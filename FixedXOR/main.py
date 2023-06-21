import sys

def print_usage():
    print("Usage: python3 main.py <An hex string to encode> <A hex string to XOR against>")
    sys.exit(1)

def xor_strings(a, b):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def main():
    if len(sys.argv) != 3:
        print_usage();
    a = bytes.fromhex(sys.argv[1]).decode()
    b = bytes.fromhex(sys.argv[2]).decode()
    xored = xor_strings(a, b).encode("ascii").hex()

    print(xored)

    

main()
