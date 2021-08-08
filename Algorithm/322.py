#322. Coin Change:
#coins = [1, 2, 5] -> amount
#Calculate the smallest number of coins required to 
#form a tree here:

#exponential solution: the problem can be solved in polynomial time
#F(S)-> amount(S) using [c_0, ... c_n-1]

#optimal solutions can be constructed by optimal solutions of subproblems here, 
#F(S) = F(S - C) + 1

#val_1, val_2, ... -> S which is optimal and the last coin's denominator is C
#F(S) = F(S - C) + 1

#states[S, [n-1]] = min(states[S, [n - 2]], states[S, [n - 3]] + 1(n - 2)] likethis here.

#FDR(t) ~~ E[V(t)]/ E[S(t)] -> the FDR at 
#a certain threshold can be estimated 
#as the expected # of false positive ratio at that
#threshold divided by the expected number of features
#called significant at that threshold here.

#Code -> build -> QA -> stage -> production: significance levels here.
#

F(S) = min_{i = 0, ..., n - 1} F(S - c_i) + 1
S >= c_i -> #relationship between n and n - 1(but also use one of the other values)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

    def helper(self, coins, remainder, currCount):
        if remainder < 0:
            return -1
        if remainder == 0:
            return 0
        if count[]

if random.randint(1, currentCount) == currentCount:
    result = currentCount



y to the power x: y ^ x here, the reservoir sampling here.
#show enough respect to your collaborators here.
#linked-list random node -> traverse until the end of the linked list here.
#Continuous deployment VS continuous delivery here

y to the power x: y ^ x
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        nrows = len(coins) + 1
        ncols = amount + 1
        states = [[float("inf") for _ in range(ncols)] for _ in range(nrows)]
        for i in range(nrows):
            states[i][0] = 0

        for i in range(1, nrows):
            for j in range(1, ncols):
                if j < coins[i - 1]:
                    states[i][j] = states[i - 1][j]
                else:
                    taking = 1 + states[i][j - coins[i - 1]]
                    leaving = states[i - 1][j]
                    dp[i][j] = min(taking, leaving)
        if dp[-1][-1] == float('inf'):
            return -1
        else:
            return dp[-1][-1]

if j < coins[i - 1]:
    states[i][j] = states[i - 1][j]

taking = 1 + states[i][j - coins[i - 1]]
leaving = states[i - 1][j]
states[i][j] = min(taking, leaving)


Trie trie = new Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")



trie.insert("apple")
trie.search("apple")
trie.startsWith("ap")
trie.insert("appl")
trie.search("ap")

class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}
    def insert(self, word: str) -> None:
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.isWord = True
    def search(self, word: str) -> bool:
        node = self
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isWord
    def startsWith(self, prefix: str) -> bool:
        node = self
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True







































