import random
class RandomNumbers:
    amount = None
    minrange =None
    maxrange = None
    
    def generate_random_numbers(self,amount,minrange,maxrange):
        amount1 = amount
        randlist = random.sample(range(minrange,maxrange),amount)
        return randlist
    

R =RandomNumbers() 
print(R.generate_random_numbers(10,200,300))
