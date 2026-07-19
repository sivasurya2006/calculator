class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if(self.b == 0):
              print("divide is not divisible by zero")
        else:
          return self.a/self.b
    def modulas(self):
             if(self.b == 0):
                   print("modules is not divisible by zero")
             else:   
                  return self.a % self.b


while True:
        print("1:add:")
        print("2:sub:")
        print("3:mul:")
        print("4:div:")
        print("5:modulas:")

        choices =int(input("enter the choices:"))
        a=float(input("enter the number 1:"))
        b=float(input("enter the number 1:"))
        user=calc(a,b)
  

        if(choices ==1):
           
            print("Result:", user.add())
         
        elif(choices ==2):
                        print("Result:", user.sub())
        elif(choices ==3):
           
            print("Result:", user.mul())
        elif(choices ==4):
                       print("Result:", user.div())
        elif( choices==5):
           
            print("Result:", user.modulas())
        else:
            print("enter the invalid choices:")
            
 
