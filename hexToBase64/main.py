import sys
import base64

def print_usage():
    print("Usage: python3 main.py <A hex string to encrypt>")
    sys.exit(1)

def hex_to_b64(h: str):
    try:
        ret = base64.b64encode(bytes.fromhex(h)).decode()
    except:
        print("Not a hex string")
        sys.exit(2)
    return ret

def main():
    if len(sys.argv) != 2:
        print_usage()
    b64 = hex_to_b64(sys.argv[1])
    print(b64)

main()
