def sum():
    lst_size = int(input("Enter the list size: "))
    lst = []
    total = 0
    for i in range(lst_size):
        data = int(input("Enter your element: "))
        lst.append(data)
    print("List: ",lst)

    for i in lst:
        total += i

    return total,lst

if __name__ == "__main__":
    summ,list = sum()
    for i in list:
        print(i,end=' ')
        if i != list[-1]:
            print("+",end=' ')
    print(" =",summ)
