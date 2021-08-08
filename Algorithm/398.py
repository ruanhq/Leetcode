#398. RandomPickIndex:
from random import randint
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        answers = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                if randint(1, count) == count:
                    answers = i
        #sample from the current reservoir of the index of this same value.
        #like reservoir sampling here.
        return answers

#To enforce cross-collection consistency here: 

def pick(self, target: int) -> int:
    answers = None
    count = 0
    for i, x in enumerate(self.nums):
        if x == target:
            count += 1
            #random sample the current reservoir with equal probability here:
            if randint(1, count) == count:
                answers = i
    return answers


#prevent data quality issues:
#(1): test the production data in isolation from the main branch before deployment
#(2): test intermediate results in isolation in DAG to avoid cascading quality issues
#and easily manage the retention of such intermediate results using branching retention logic.

#382. linked list random node:

#built to help you say yes - not to profit off mistakes or misfortune.

#unlike most credit card companies, our bueinsee was built to
#help you say yes - not to profit off mistakes or mis

#paypal -> senior management from paypal -> small, midsize loan -> 
#providing loan -> run parallel -> loan underwrite -> 
#lending providers: sales -> target -> partner with : put in the card
#financing -> buy now -> benefit for the clients -> benefits for our customers

#core business -> to work for this: 
#technical -> hiring managers interview -> group meeting:s
#computer science , model building.

#ask a couple of companies:
#OPT -> visa, transfer -> next space:
#no expectation

#yes
#my side -> 
#get feedback -> computer science fundamentals, model building 
#as well as the machine learning models ->










