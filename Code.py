def code():
        wd=input("Enter the word to code:")
        for i in range(0, len(wd)):
            j=wd[i]
            cd=ord(j)
            c=[]
            c.append(cd)
            print("The code :",c)
        return ''