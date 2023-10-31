# Joseph Cardillo

def encode(password):
    int_list = ''
    for i in password:
        x = int(i) + 3
        int_list += str(x)
    return int_list



def main():
    while True:
        print("Menu")
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = input('Please enter an option: ')

        if option == '1':
            password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored! \n')
            # print(password)


if __name__ == "__main__":
    main()