import random
from dataclasses import dataclass
@dataclass
class RandomNumbers:
    amount = None
    minrange =None
    maxrange = None
    
    def generate_random_numbers(self,amount,minrange,maxrange):
        assert maxrange > minrange, 'maximum range should be greater than minimum range' #precondtion 1
        assert amount < maxrange, 'the amount of numbers that will be returning should be less than the maximum range.' #precondtion 2

        amount1 = amount
        randlist = random.sample(range(minrange,maxrange),amount)
        
        assert sum(randlist) >= 100 ,"The sum of the numbers in randomlist should be greater than or equal to 100"
        assert randlist[2] %2 != 0 , "The number at index 2 should not be an even number" #postcondtion
        return randlist
    

R =RandomNumbers() 
r1=R.generate_random_numbers(5,100,200)
print(R.generate_random_numbers(10,200,300))
print(r1)
