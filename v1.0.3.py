import sys

def letter(passw):
    return any(c.isupper() for c in passw) and any(c.islower() for c in passw)

def number(passw):
    return any(c.isdigit() for c in passw)

def symbol(passw):
    return any(not c.isalnum() for c in passw)

def check_password(passw, min_len=8, req_letter=False, req_number=False, req_symbol=False):
    weaknesses = []
    if len(passw) < min_len:
        weaknesses.append(f"too short (needs {min_len} chars)")
    if req_letter and not letter(passw):
        weaknesses.append("missing uppercase and lowercase letters")
    if req_number and not number(passw):
        weaknesses.append("missing a number")
    if req_symbol and not symbol(passw):
        weaknesses.append("missing a symbol")
    return weaknesses

def main():
    print("J Checker :p")
    use_list = input("[*] Check a password list? (y/n): ").lower()

    if use_list == 'y':
        file_path = input("[*] Enter password list file (name or path): ")
        try:
            with open(file_path, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("[!] Error: File not found!")
            sys.exit(1)
    elif use_list == 'n':
        passwords = [input("[*] Enter password to check: ")]
    else:
        print("[!] Invalid input!")
        sys.exit(1)

    checker = input("[*] Use default or custom requirements? (d/c): ").lower()
    if checker not in ['d', 'c']:
        print("[!] Invalid input!")
        sys.exit(1)

    if checker == 'd':
        min_len, req_letter, req_number, req_symbol = 8, True, True, True
    else:
        min_len = int(input("[*] Minimum password length: "))
        req_letter = input("[*] Require uppercase and lowercase? (y/n): ").lower() == 'y'
        req_number = input("[*] Require a number? (y/n): ").lower() == 'y'
        req_symbol = input("[*] Require a symbol? (y/n): ").lower() == 'y'

    for password in passwords:
        weaknesses = check_password(password, min_len, req_letter, req_number, req_symbol)
        if weaknesses:
            print(f"[!] Password '{password}' issues: {', '.join(weaknesses)}")
        else:
            print(f"[*] Password '{password}' is strong!")

if __name__ == "__main__":
    main()
