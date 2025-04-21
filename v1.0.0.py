import sys
import time

print("Password strength checker.")
password = input("Enter your password for analysis:")
checker = input("Do you wish to edit or use the default requirements (e/d): ")


def letter(passw):
    return any(cap.isupper() for cap in passw) and any(low.islower() for low in passw)

def number(passw):
    return any(num.isdigit() for num in passw)

def symbol(passw):
    return any(not sym.isalnum() for sym in passw)

def error_output(n):
    if n == "c":
        print(f"the password '{password}'needs a capital or a lowercase letter or both!")
    elif n == "n":
        print(f"the passwd '{password}' is missing at least one number!")
    else:
        print(f"the passwd '{password}' is missing at least one unique symbol!")

def switcher (a):
    if a == 0:
        return 'c'
    if a == 1:
        return 'n'
    else:
        return 's'



err = "[!] 3RR0R invalid argument, try again!"
now = "the password is strong for now..."
strength = f"[*] The passw {password} is viable"
dict1 = {'c':letter(password), 's':symbol(password), 'n':number(password)}
l = len(password)
nle = f"[!] The passwd '{password}' is not long enough {l}<{len(password)}"


if checker == 'd'.lower():
    if len(password) >= 8:
        if number(password) and symbol(password) and letter(password):
            print(now)
        else:
            print("Password is weak")
            sys.exit()
    else:
        print(nle)
        sys.exit()

elif checker == 'e'.lower():
    l = int(input("What is the desired minimum length for the passw check: "))
    c = input("Do you wish the passwd to require at least one lowercase and uppercase letter? (y/n): ")
    n = input("Do you wish your passw to require at least one number? (y/n): ")
    s = input("Do you wish your passw to require at least one unique symbol? (y/n): ")
    check = -1
    if len(password) > l:
        for i in [c, n, s]:
            check += 1
            if i == "y":
                i = switcher(check)
                if dict1[i]:
                    print()
                    time.sleep(1)
                else:
                    error_output(i)
                    sys.exit()

            elif i == "n":
                pass
            else:
                print(err)
                sys.exit()
    else:
        print(nle)
        sys.exit()

else:
    print(err)
    sys.exit()
