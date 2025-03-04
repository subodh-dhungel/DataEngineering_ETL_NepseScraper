class PrimeNumbers:
    def isPrimeNumber(self,n):
        if n<2:
            return False
        
        for i in range(2,n):
            if n%i == 0:
                return False
            else:
                return True
            

    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        self.num += 1
        if self.num > 100:
            raise StopIteration
        else:
            x=self.isPrimeNumber(self.num)
            return self.num if x else None
        
myPrimeNumbers = PrimeNumbers()
for i in myPrimeNumbers:
    if i is not None:
        print(i)