class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        sum = self.num1 + self.num2
        return sum
   
    def subtract(self):
        sub = self.num2 - self.num1
        return sub
    
    def multiply(self):
        multi = self.num1 * self.num2
        return multi
    
    def divide(self):
        div = self.num2/self.num1
        return div

obj = calculator(10,94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())