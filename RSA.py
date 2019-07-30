##  Please note, PSL references 'Python Standard Library'.
##  Note the format in comments is as such: variable (type)

def Convert_Text(_string):
    """
    Objective:
    Function should convert string to corresponding list of 
    (ASCII) integers.

    Argument:
    _string (str): Message to be converted to ASCII integers.

    Return:
    list1 (list): List of ASCII integers converted from message.

    Example:
    _string = Message
    list1 = [77, 101, 115, 115, 97, 103, 101]
    """
    list1 = []  ##  Empty list to append ASCII characters.
    for i in range(len(_string)):   ##  len() is from PSL and sets length range of message/string to be converted.
        list1.append(ord(_string[i]))   ##  ord() is from PSL and converts char to ASCII.
    return list1

def Convert_Numbers(_list):
    """
    Objective:
    Function should convert list of ASCII integers into 
    corresponding string.

    Argument:
    _list (list): List of ASCII integers to be converted to message string.

    Return:
    _string (str): Message string converted from list of ASCII integers.

    Example:
    _list = [77, 101, 115, 115, 97, 103, 101]
    _string = Message
    """
    _string = ''
    for i in range(len(_list)):
        _string += chr(_list[i])    ##  chr() converts single ASCII string character to corresponding letter.
    return _string

def Convert_Binary_String(_int):
    """
    Objective:
    Convert integer to corresponding binary format as a string.

    Argument:
    _int (int): Integer to be converted to binary format.

    Return:
    binary (str): Binary conversion as a string of input integer.

    Example:
    _int = 16
    binary = 10000
    """
    binary = ''
    list2 = []
    if _int == 0:
        binary += str(0)
        return binary  ##   Returns binary = 0 for _int = 0.
    while (_int > 0):   ##  Loop converts integer to reverse binary format.
        binary_digit = _int % 2
        list2.append(binary_digit)  ##  Appends binary digits to list2. Example: 00001
        _int = _int // 2
    i = len(list2) - 1  ##  Sets length of i to length of list to start at 0.
    while (i >= 0): ##  Loop reverses into binary string for _int.
        binary += str(list2[i]) ##  Appends binary to ordered list to create string.
        i = i - 1
    return binary

def FME(b, n, m):
    """
    Objective:
    Fast Modular Exponentiation to find x = b**n mod m.

    Argument:
    b (int): Base
    n (int): Exponent
    m (int): 

    Return:
    x (int): Modulus

    Example:
    b = 13
    n = 153
    m = 845733
    x = 174586
    """
    x = 1
    Convert_Binary_String(n)
    power = b**n
    while (n > 0):
        k = n % m
        n = n // 2
        if  k == 1:
            x = (x * power) % m
            power = pow(power, 2) % m
    return x


def Div_Algorithm(c, d):
    """
    Objective:
    Calculates both c divided by d (quotient) and c mod d.
    Note that c / d calculated without use of division operator (/).
    Note that algorithm calculates c mod d without use of mod operator (%).

    Argument:
    c (int): Dividend.
    d (int): Divisor

    Return:
    x (int): x = c / d
    y (int): y = c % d

    Example:
    c = 10
    d = 3
    (x, y) = (3, 1)
    """
    x = 0
    y = abs(c)
    while y >= d:
        y = y - d   ##  Subtracts y (dividend) by d (divisor).
        x = x + 1   ##  While loop is x + 1 times y can be subtracted by d.
        if c < 0 and y > 0: ##  self-note: within in while loop or not???
            y = d - y
            x = -(x + 1)    ##  Calculates number of times y subtracted by d for negative dividend.
            y = abs(y)
    return x, y ##  Returns (x = c / d, y = c mod d).

def Euclidean_Algorithm(a, b):
    """
    Objective:
    Calculates the greatest common divisor (GCD) between two numbers a, b.

    Argument:
    a (int): Integer to find GCD relative to integer b.
    b (int): Integer to find GCD relative to integer a.

    Return:
    x (int): GCD of a, and b.

    Example:
    a = 100
    b = 30
    x = 10
    """
    x = a
    y = b
    if (b == 0):
        return "Error: Cannot calculate GCD of 0. Please try again."
        RSA_Menu()
    while y != 0:    ##  While loop continues until y = 0 (r = 0 in mod calculation).
        r = x % y
        x = y
        y = r
    return x

import random   ##  Module to generate random numbers.

def Find_Public_Key_e(p, q):
    """
    Objective:
    Create public keys for RSA. Values (e, n).

    Argument:
    p (int): User-selected prime number.
    q (int): User-selected prime number.

    Return:
    Public_Key_e e, n (int, int): Public key values e and n.

    Example:
    p = 23
    q = 101
    Public_Key_e (e, n) = (59, 2323)
    """
    n = (p * q)
    phi_n = (p - 1) * (q - 1)   ##  Calculates phi(n), where n = p * q.
    #e = 3
    e = random.randrange(3, 139) ##  Range to start at 3 and keep relatively small.
    while ((e % 2) == 0):   ##  Loop to make sure random e value is odd.
        e = random.randrange(3, 139)
    gcd = Euclidean_Algorithm(e, phi_n) ##  Check that e and phi(n) are relatively prime and that gcd = 1.
    while (gcd != 1 and e != p and e != q):   ##  self-note: Verify loop conditions
        gcd = Euclidean_Algorithm(e, phi_n) ##  Check if e relatively prime to phi(n).
        e = e + 2   ##  Add 2 to odd number to keep odd and != (p or q).
    Public_Key_e = (e, n)
    return Public_Key_e

def Find_Private_Key_d(e, p, q):
    """
    Objective:
    Use Extended Euclidean Algorithm to calculate d.
    Modular inverse of: d * e = 1 mod phi(n).
    Create private key d.

    Argument:
    e (int): Public Key exponent value from Find_Public_Key_e function.
    p (int): First prime value previously selected by user in Find_Public_Key_e function.
    q (int): Second prime value previously selected by user in Find_Public_Key_e function.

    Return:
    d (int): Private key value d. Found via modular inverse of: d * e = 1 mod phi(n).

    Example:
    e = 59
    p = 23
    q = 101
    d = 1939
    """
    ##  Calculate phi(n).
    phi_n = (p - 1) * (q - 1)

    ##  Saved initial values for e and n.
    original_e = e
    original_phi_n = phi_n

    ##  Set initial values of Bezout Coefficients.
    s1, s2, t1, t2 = 1, 0, 0, 1

    ##  Loop to calculate value of d.
    while (phi_n > 0):
        e = s1 * original_e + t1 * original_phi_n
        phi_n = s2 * original_e + t2 * original_phi_n
        q = e // phi_n
        r = e % phi_n
        e = phi_n
        phi_n  = r

        s = s1 - q  * s2
        t = t1 - q * t2
        s1 = s2
        t1 = t2
        s2 = s
        t2 = t

    ##  Loop to return positive Bezout Coefficient.
    d = s1 + original_phi_n
    return d

def Encode(n, e, message):
    """
    Objective:
    Through RSA, utilize public keys (e, n) to encrypt a message as ciphertext.

    Argument:
    e (int): Public Key exponent value from Find_Public_Key_e function.
    n (int): Public key modulus calculated from Find_Public_Key_e function.
    message (str): User-input message from...to be encrypted.

    Return:
    ciphertext (list): List of encrypted characters that corresponds to each character from the string message.

    Example:
    e = 59
    n = 2323
    message  = Encrypted!
    ciphertext = [2162, 1154, 1118, 1747, 1181, 632, 1864, 1616, 807, 2029]
    """
    ciphertext = [] ##  Empty list to be appended with encrypted message ciphertext.
    ASCII_list = Convert_Text(message)  ##  Message converted to list of ASCII characters.

    ##  Loop uses Fast Modular Exponentiation to encrypt each ASCII character.
    ##  Each character is then appended to list ciphertext.
    for i in range(len(ASCII_list)):
        ciphertext.append(FME(ASCII_list[i], e, n))
    return ciphertext

def Decode(n, d, ciphertext):
    """
    Objective:
    Decrypt ciphertext list of encrypted numbers utilizing RSA public key n and private key d.

    Argument:
    n (int): Public key modulus calculated from Find_Public_Key_e function.
    d (int): Private key calculated from Find_Private_Key_d
    cipher_text (list): Message of encrypted ciphertext as a list.

    Returns:
    message (str): Decrypted message - should match original user-input message.

    Example:
    n = 
    d = 
    ciphertext = 
    message = 
    """
    Decrypted_list = [] ##  Empty list - to be appended with decrypted ASCII characters.

    ##  
    for i in range(len(ciphertext)):
        Decrypted_list.append(FME(ciphertext[i], d, n))
    message = Convert_Numbers(Decrypted_list)
    return message

def Brute_Force_Cracker(composite):
    """
    Objective:

    Argument:

    Return:

    Example:

    """
    i = 2
    for i in range(2, (composite - 1)):
        if(composite % i == 0):
            return(i, (composite // i))
        else:
            i += 1

def is_sqrt(integer):
    """
    Objective:

    Argument:

    Return:

    Example:

    """
    x = integer
    y = (x + integer // x) // 2
    while y < x:
        x = y
        y = (x + integer // x) // 2
    return x

def isqrt(n):
    """
    Objective:

    Argument:

    Return:

    Example:

    """
    return int(n ** 0.5)

def Mod_Brute_Force(n):
    """
    Objective:

    Argument:

    Return:

    Example:

    """
    a = is_sqrt(n)
    b2 = a ** 2 - n
    b = isqrt(n)
    count = 0
    while pow(b, 2) != b2:
        a += 1
        b2 = pow(a, 2) - n
        b = isqrt(b2)
        count += 1
    p = a - b
    q = a + b
    assert n == p * q
    return p, q

def Get_Prime():
    """
    Objective:

    Argument:

    Return:

    Example:

    """
    l1 = []
    for x in range(2, 2000):
        if all(x % i != 0 for i in range(2, x)):
            l1.append(x)
    print(l1)


def Menu_Get_Keys():
    """
    Objective:
    Prompts user to input prime number selections for p and q. Creates Public Keys e, and 
    n with Find_Public_Key_e. Creates Private Key, d, with Find_Private_Key_d. Prints 
    values for e, n, and d.
    """
    p = int(input("Enter a prime integer for p: "))
    q = int(input("Enter a second prime integer for q: "))
    e, n = Find_Public_Key_e(p, q)
    d = Find_Private_Key_d(e, p, q)
    print("\nYour public key e is: ", str(e))
    print("Your public key n is: ", str(n))
    print("Your private key d is: ", d)
    input("\nPress ENTER to continue.\n")


def Menu_Encode_Message():
    """
    Objective:
    Prompt user input of public keys e and n, and to type message to be encrypted. Generates
    ciphertext of message using the functions: Encode, convert_text, FME. Prints message 
    to screen as encrypted list.
    """
    e = int(input("Enter Public Key From Key Generation - e: "))
    n = int(input("Enter Public Key From Key Generation - n "))
    message = input("Enter message to be encrypted: ")
    encoded_message = Encode(n, e, message)
    print("\nYour message as ciphertext: ", encoded_message)
    input("\nPress ENTER to continue.\n")

def Menu_Decode_Message():
    """
    Objective:
    Prompt user input of public key n and private key d, and to type ciphertext as a list 
    to decrypt as original message. Generates message using functions: Decode, 
    Convert_Numbers, FME. Prints message to screen.
    """
    n = int(input("Enter Public Key From Key Generation - n: "))
    d = int(input("Enter Private Key From Key Generation - d: "))
    ciphertext = input("Enter encrypted ciphertext as a list (e.g. [1, 2, 3]): ")
    print("\nPlease be patient. This make take a couple minutes.")
    ciphertext = ciphertext.replace("[", "")
    ciphertext = ciphertext.replace("]", "")
    ciphertext = [int(i) for i in ciphertext.split(",")]
    plaintext = Decode(n, d, ciphertext)
    print("\nThe decrypted message is: " + plaintext)
    input("\nPress ENTER to continue.\n")

import time
def Menu_Brute_Force_Cracker():
    """
    Objective:
    Crack the code.
    """
    composite = int(input("Enter Public Key - n: "))
    start = time.time()
    cracked_d = Brute_Force_Cracker(composite)
    print("\nYour prime factors were: ", cracked_d)
    end = time.time()
    print(end - start, "Seconds Elapsed")
    #print("\nIt took " + end - start + " seconds to crack.")
    input("\nPress ENTER to continue.\n")

def Menu_Mod_Brute_Force():
    """
    Objective:
    Faster Crack
    """
    composite = int(input("Enter Public Key - n: "))
    start = time.time()
    cracked_pq = Mod_Brute_Force(composite)
    print("\nYour prime factors were: ", cracked_pq)
    end = time.time()
    print(end - start, "Seconds Elapsed")
    input("\nPress ENTER to continue.\n")

def Menu_Get_Prime():
    """
    Objective: Print list of prime numbers.
    """
    print("\nList of prime numbers through 2000: \n")
    Get_Prime()
    print("\n")

def RSA_Menu():
    """
    Prompt user to select from (insert number) options:
    1. Get Keys
    2. Encode Message
    3. Decode Message
    4. Brute Force Cracker
    5. Mod Brute Force Cracker Floor[Sqrt[n]] = x. n mod x until = 0
        to find p.
    6. 
    """
    print("**************************************************".center(115))
    print("Welcome to the RSA Menu".center(115))
    print("\n")
    print("Please Select From the Following - Type a Number and Press ENTER:".center(115))
    print("\n")
    print("1. Start with Key Generation".center(110))
    print("2. Encode Message".center(100))
    print("3. Decode Message".center(100))
    print("4. Brute Force Decryption".center(107))
    print("5. Modified Decryption.".center(105))
    print("6. List Prime Numbers Through 2000.".center(117))
    print("7. Exit Program".center(98))
    print("**************************************************".center(115))
    valid_input = False
    while not valid_input:
        user_input  = int(input("\nType your selection and press ENTER: \n"))
        if user_input in range(1, 8):
            valid_input = True
    if user_input == 1:
        Menu_Get_Keys()
        RSA_Menu()
    elif user_input == 2:
        Menu_Encode_Message()
        RSA_Menu()
    elif user_input == 3:
        Menu_Decode_Message()
        RSA_Menu()
    elif user_input == 4:
        Menu_Brute_Force_Cracker()
        RSA_Menu()
    elif user_input == 5:
        Menu_Mod_Brute_Force()
        RSA_Menu()
    elif user_input == 6:
        Menu_Get_Prime()
        RSA_Menu()
    elif user_input == 7:
        print("\nClosing Program!!!!!!!")
        exit

def main():
    RSA_Menu()
if __name__ == '__main__':
    main()

