import random
class RandomNumbers:
    amount = None
    minrange =None
    maxrange = None
    
    def generate_random_numbers(self,amount,minrange,maxrange):
        assert maxrange > minrange, 'maximum range should be greater than minimum range' #precondtion 1
        assert amount < maxrange, 'the amount of numbers that will be returning should be less than the maximum range.' #precondtion 2

        amount1 = amount
        randlist = random.sample(range(minrange,maxrange),amount)
        return randlist
    

R =RandomNumbers() 
r1=R.generate_random_numbers(5,10,50)
print(R.generate_random_numbers(10,200,300))
print(r1)
