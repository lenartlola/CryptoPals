import sys
import binascii

def print_usage():
    print("This script would decrypt a xored string that has been encoded using one single byte character.")
    print("Usage: python3 main.py <A hex string to decode> <a character to xor>")
    sys.exit(1)


def decode_string(s):
    x = binascii.unhexlify(s)
    for key in range(256):
        decoded = "".join(chr(i ^ key) for i in x)
        if decoded.isprintable():
            print("Key: ", key, "decoded: ", decoded)

def main():
    if len(sys.argv) != 2:
        print_usage()
    res = decode_string(sys.argv[1])
    print("Decode: ", res)

main()
