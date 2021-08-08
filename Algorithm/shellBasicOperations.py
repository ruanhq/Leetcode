#Shell basic operations:

#word frequency:

"""
the day is sunny the the 
the sunny is is is is is is 
"""

#Shell script is a computer program designed to be run by 
#the unix shell, a command-line interpreter,
#the various dialects of shell scripts are considered to be 
#scripting languages, 
#typical operations performed by shell scripts includes file
#manipulation, program execution, print text.

#run the program, logging, called a wrapper here.

echo "Hello World"

nano First.sh #modification mode here.


bash First.sh
chmod a+x First.sh
./First.sh

echo -e "\n Removing \t backslash \t characters \n"
echo -n "Printing text without newline"
echo "Printing text with newline"

nano example2.sh

#using while loop:
nano example4.sh

valid = true
count = 1
while [$valid]
do
echo $count
if [$count -eq 5];
then break
fi 
((count ++))
done


#!/bin/bash
for (( counter = 10; counter > 0; counter --))
do 
echo -n "$counter "
done 
printf "\n"

#echo -n "$counter " 

#!/bin/bash
n = 10
if [$n -lt 10];
then 
echo "AAA1"
else
echo "FSAWAA"
fi

#!/bin/bash
echo "Enter username"
read username
echo "Enter password"
read password

if [[( $username == "admin" && $password == "secret")]]; then
echo "valid user"
else 
echo "invalid user"
fi

#!/bin/bash
echo "Total arguments: $#"
echo "1st argument = $1"
echo "2nd argument = $2"

string3 = $string1 + $string2
stirng3+= "is a good tutorial blog site"

string3+= "is a good tutorial blog site"

n = 10
if [$n -lt 10];
then 
echo "AAA1"
else 
echo "AAA2"
fi



class Solution:
    def isClosed(self, grid, row, column):
        if grid[row][column] == 1:
            return True
        if row <= 0 or row >= nr - 1 or columns <= 0 or column >= nc - 1:
            return False
        nr = len(grid)
        nc = len(grid[0])
        grid[row][column] = 1
        up = self.isClosed(grid, row + 1, column, nr, nc)
        down = self.isClosed(grid, row - 1, column, nr, nc)
        left = self.isClosed(grid, row, column - 1, nr, nc)
        right = self.isClosed(grid, row, column + 1, nr, nc)
        return up or down or left or right
    def closedIslaned(self, grid):
        result = 0 
        if not grid or len(grid) == 0:
            return 0  
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0 and self.isClosed(grid, i, j):
                    result += 1
        return result




class Solution:
    def closedIsland(self, grid):
        if len(grid) == 0 or len(grid[0])

#spam behaviors:
"""
spammers not followed by legitimate users -> followed by different users draw plots comparison
spammers' tweets are unsolicited, number of likes and retweets for their tweets are
expected to be less compared to legitimate users
spammers' tweets are ignored by legitimate users, number of replies and mentions spammers get
are expected to be low compared to legitimate users
spammers tend to post same or similar tweets which are posted by one or more controlled accounts.

Spammers tend to use lots of hashtags(trending ones) to acquire more users
newwork of users with relationships between them and tweets -> graph 

The distance between a spammer and a legitimate user is further than distance between 
two legitimate users
The connectivity between a spammer and a legitimate user is more robust than the
connectivity between two legitimate users.

Graph-based features provide the most robust performance to detect spam and spammers -> hard to manipulate and not user controlled
"""


























