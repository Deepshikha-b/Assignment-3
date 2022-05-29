def str():
    str1 = input("Enter the string: ")
    str2 = ''
    for i in str1:
        str2 = i + str2
    return str2

if __name__ == '__main__':
    rev_str = str()
    print("Reversed string is: ",rev_str)