# Joseph Cardillo

def encode(password):
    int_list = ''
    for i in password:
        if int(i) < 7:
            int_list += str(int(i) + 3)
        else:
            int_list += ((str(int(i) + 3))[1])
    return int_list


def decode(password):
    newpassword = ''
    for i in password:
        i = int(i) - 3
        i = str(i)
        if i == '-1' or i == '-2' or i == '-3':
            i = int(i) + 10
        newpassword += str(i)
    return newpassword


def main():
    print("Menu")
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    option = input('Please enter an option: ')

    if option == '1':
        old_password = input('Please enter your password to encode: ')
        new_password = encode(old_password)
        print('Your password has been encoded and stored! \n')
        print(f'The encoded password is {new_password}, and the original password is {old_password}')

    elif option == '2':
        new_password = input('Please enter you passowrd to decode: ')
        old_password = decode(new_password)
        print('Your password has been decoded and stored! \n')
        print(f'The decoded password is {old_password}, and the original password is {new_password}')


    elif option == '3':
        return False


if __name__ == "__main__":
    while True:
        main()
