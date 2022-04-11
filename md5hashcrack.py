import hashlib
import argparse

parser = argparse.ArgumentParser(description="MD5 Cracker")
parser.add_argument("-md5 ", dest="hash", help="md5 hash", required=True)
parser.add_argument("-w", dest="wordlist",help="wordlist",required=True)
pared_args = parser.parse_args

def main():
    hash_cracked = ""
    with open(parsed_args.wordlist)
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == parsed.args.hash:
                hash_cracked = line 
                print("\nMD5-hash has been successfully cracked. The value is %s."%line)

    if hash_cracked == "":
        print("\nFailed to cracked the hash. Try using different dictionary.") 

if __name__ == "__main__":
    main()