# Joseph Cardillo

def encode(password):
    int_list = ''
    for i in password:
        if int(i) < 7:
            int_list += str(int(i) + 3)
        else:
            int_list += (str(int(i) - 7))
    return int_list


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

    # elif option == '2':

    elif option == '3':
        return False


if __name__ == "__main__":
    while True:
        main()
