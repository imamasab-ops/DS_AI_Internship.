# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:16:17 2026

@author: Dell
"""
#Probability of rolling a 4 on a fair die
favorable = 1
total_outcomes =6
probability = favorable  / total_outcomes
print("Probability of  rolling a 4 on a fair die =", probability)
print ("=",50)

#indipendent event example
p_rain = 0.3
p_traffic = 0.2
p_both = p_rain * p_traffic 
print("Probability of rain=",p_rain)
print("probability of traffic =",p_traffic)
print("probability of both =",p_both)

#conditional probability example 
p_A_and_B =0.1
p_B = 0.4
p_A_given_B = p_A_and_B / p_B
print("probability of A and B =" ,p_A_and_B )
print("probability of B=", p_B)
print("probability of p_A_given_B =", p_A_given_B )

# Given probabilities
P_D = 0.01            # Prior probability of disease
P_not_D = 1 - P_D     # No disease
P_Pos_given_D = 0.95  # True positive rate
P_Pos_given_not_D = 0.05  # False positive rate
# Total probability of testing positive
P_Pos = (P_Pos_given_D * P_D) + (P_Pos_given_not_D * P_not_D)
# Bayes' Theorem
P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos
print("Probability of having disease given positive test:", P_D_given_Pos)

#Task1
import random
# Number of simulations
n = 1000
count_sum_7 = 0
for _ in range(n):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        count_sum_7 += 1
experimental_probability = count_sum_7 / n
print("Experimental Probability (Sum = 7):", experimental_probability)

#Task2
# Independent events
P_heads = 1/2
P_six = 1/6
P_both = P_heads * P_six
print("Probability of Heads AND rolling a 6:", P_both)
# Dependent events (without replacement)
P_first_red = 5/10
P_second_red_given_first = 4/9
P_both_red = P_first_red * P_second_red_given_first
print("Probability both marbles are Red:", P_both_red)
# Simple conditional probability example
count_san = 100
count_san_francisco = 70
P_francisco_given_san = count_san_francisco / count_san
print("P(Francisco | San) =", P_francisco_given_san)

#Task3
# Given probabilities
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Step 1: Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

# Step 2: Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)



