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