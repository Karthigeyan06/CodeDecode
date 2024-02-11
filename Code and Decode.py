def code_decode():
    w=[]
    qn=int(input('Enter the operation 1. Code  2. Decode :'))
    def code():
        wd=input("Enter the word to code:")
        for i in range(0, len(wd)):
            j=wd[i]
            cd=ord(j)
            c=[]
            c.append(cd)
            print("The code :",c)
        return ''
    def decode():
        Num=int(input("Enter the no. of numbers to decode:"))
        
        i=1
        
        while i<=Num:
            i+=1
            cod=int(input('Enter the number :'))
            decod=chr(cod)
            
            w.append(decod)
           
        print("The decoded Message:",w)
        return ''
    if qn==1:
        print(code())
    elif qn==2:
        print(decode())
    else:
        print()
    return code_decode()
    

print(code_decode())
    

                    
