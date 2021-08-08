#86. Partition List:

#json to string:

#implementing conversion from json to string:

#Input: Map<String, Object>, Object can
#either be Object, List, Map<String, Object>,
#Output: String





#One analyst case, one statistical role play,
#One job fit interview, one technical interview.

#To solve a real-life business problem, will work
#through a business question with you while
#evaluating your strategy thinking, analytical skills
#and quantitative abilities as you solve for 
#solutions.

#will work with data every day, solve complex
#algebraic equations by hand, we are looking
#for candidates with an analytical mindset, you 
#need to be able to understand data, communicate
#effectively with both business leaders and
#technical teams and leverage data 
#to make the best decisions for our customers.

#As a data scientist at capital one, you will often
#be asked to draw insights and develop recommendations
#based on statistical analysis, 
#your ability to communicate those findings in
#a clear manner, especially to thoes who do not 
#have a data science background,
#will be critical to your success.

#The interviewer will ask an open-ended question
#meant to start your conversation and allow the
#interviewer to learn more about how you would
#approach work and projects.

#technical interview: breadth, depth of your engineeiring
#and technical data science skill-sets in a 
#constructive, conversational setting.

#data science covers a huge variety of technical and
#non-technical skills, with engineering and 
#data skills among the most important,
#we want to make sure we know where you are a real
#expert, and how you'd apply your skills and 
#Knowledge to the kinds of modeling operations
#most important at Capital One

#At the job fit interview we will ask you about your relevant
#background and experience, as well as questions to get some insight
#into how you will fit in with the diverse, collaborative teams
#here at Capital One, the job fit conversations is also a great time
#to ask the interviewer any questions you may have about the role at
#Capital One.

#Science and technical abilities are important to us but 
#cultural and team fit are just as important,
#communication skills, teamwork, values and ethics are
#all within the job fit's interview.

#Break-even example: want to make $40000 this year and I 
#make $20 per pair of shoes, how many pairs of shoes do I need to sell: 2000 pairs of shoes.
#Weighted average example: 15 students takes the SAT, 8 of them
#have average score of 660, other students had an average score of 720
#The average score of the whole group: ((8 * 660) + 7 * 720)/ 15 = 688

#Define the target market, competitors, build off core competencies
#Barriers to entry, business cycle stage
#Methods of measuring viability, opportunity cost
#Source of revenue: subscriptions, newsstand sales, 
#advertising, customer lists, internet

#costs: print, distribution, content development, marketing/ promotions
#The next step is to understand the economics of the
#business, what are the profit drivers in the magazine publishing business?

#Strong communications skills: communicate in a clear,
#concise manner and walk your interview through your process.
#
#Strategic business insight: consider how the data relates to
#the relevant business
#
#Feature Engineering: show your creativity through your suggestions and observations
#Investigator approach: be curious throughout the interview and try to determine the reasons behind the analysis
#Modeling instinct: show your understanding of different models and consider the benefits
#and drawbacks of given models.
#
#Analyst case: content focused on a strategic business questions.
#Includes calculations,
#you and the interviewer will wlrk through the case as a team.
#Involve solving a real-life business problem, which could be 
#based upon a variety of business topics,
#interactive in nature.

#Evaluate your analytical skills, conceptual problem-solving skills,
#and communication skills.

#Content focused on statistical analyses, does not include calculations.
#You will act as a consultant and the interviewer as a Business Manager/
#
#Business Managers, show your creativity through your suggestions and observations
#investigator approach: be curious throughout the interview

#Will there be a break?
#How long do the interview last?
#Modeling instinct, show your understanding of different models
#and consider the benefits and drawbacks of given models.

#Consider the benefits and drawbacks of given models.


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyNode1 = indicator1 = ListNode(0)
        dummyNode2 = indicator2 = ListNode(0)
        while head:
            if head.val < x:
                indicator1.next = head
                indicator1 = indicator1.next
            else:
                indicator2.next = head
                indicator2 = indicator2.next
            head = head.next
        indicator2.next = None
        indicatro1.next = dummyNode2.next
        return dummyNode1.next



#Two pointers,
#Topological sorting,
#
#Starting from the different ones:

#Delete a guy from a list.



















