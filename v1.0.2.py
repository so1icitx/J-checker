import sys

print("J checker :p ")
password = input("[*] Enter your password for analysis:")
checker = input("[*] Do you wish to edit or use the default requirements (e/d): ")

def letter(passw):
    return any(cap.isupper() for cap in passw) and any(low.islower() for low in passw)

def number(passw):
    return any(num.isdigit() for num in passw)

def symbol(passw):
    return any(not sym.isalnum() for sym in passw)

def error_output(n):
    end = []
    weaknesses = [
        {'c':f"needs a capital or a lowercase letter or both"},
        {'n':f"is missing at least one number"},
        {'s':f"is missing at least one unique symbol"}
    ]
    print(n)
    for a in n:
        for w in weaknesses:
            if a in w:
                end.append(w[a])
                pass


    print(f"[!] the passwd {password}, {', also '.join(end)}")

def switcher (a):
    if a == 0:
        return 'c'
    if a == 1:
        return 'n'
    if a == 2:
        return 's'

err = "[!] 3RR0R invalid argument, try again!"
strength = f"[*] The passw {password} is viable"
dict1 = {'c':letter(password), 's':symbol(password), 'n':number(password)}

if checker == 'd'.lower():
    if len(password) >= 8:
        weakness = []
        if not number(password):
            weakness.append('n')
        if not symbol(password):
            weakness.append('s')
        if not letter(password):
            weakness.append('c')
        if weakness != "":
            error_output(weakness)

    else:
        print(f"[!] The passwd '{password}' is not long enough {len(password)}<{8}")
        sys.exit()

elif checker == 'e'.lower():
    l = int(input("[*] What is the desired minimum length for the passw check: "))
    c = input("[*] Do you wish the passwd to require at least one lowercase and uppercase letter? (y/n): ").lower()
    n = input("[*] Do you wish your passw to require at least one number? (y/n): ").lower()
    s = input("[*] Do you wish your passw to require at least one unique symbol? (y/n): ").lower()
    check = -1


    if len(password) > l:
        weaknessis = []
        for i in [c, n, s]:
            check += 1
            if i == "y":
                i = switcher(check)
                if dict1[i]:
                    pass
                else:
                    weaknessis.append(f'{i}')
            elif i == "n":
                check += 1
                pass
            else:
                print(err)
                sys.exit()

        if weaknessis != "":
                error_output(weaknessis)
    else:
        print(f"[!] The passwd '{password}' is not long enough {len(password)}<{l}")
        sys.exit()

else:
    print(err)
    sys.exit()
