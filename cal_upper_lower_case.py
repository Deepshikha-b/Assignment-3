def str():
    str1 = input("Enter the string here: ")
    count1 = 0
    count2 = 0
    
    for i in str1:
        if i.isupper():
            count1 += 1
        elif i.islower():
            count2 +=1
        else:
            pass
    
    return count1,count2

if __name__ == '__main__':
    uppers, lowers = str()
    print("No. of Upper case characters: ",uppers,"\nNo. of Lower case characters: ",lowers)



