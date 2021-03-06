# Tutorial 09
Created Thursday 10 November 2016

1) A bag contains five blue balls, seven red balls and eight green balls. What is the probability of drawing two balls of the same colour on two successive draws?
------------------------------------------------------------------------------------------------------------------------------------------------------------------


### (i)with replacement:
	
R+G+B = 5+7+8 = 20
	
Chances of pulling 2 red balls = 7/20 * 7/20
Chances of pulling 2 green balls = 8/20 * 8/20
Chances of pulling 2 blue balls = 5/20 * 5/20
Chances of pulling 2 same color balls =  7/20 * 7/20 + 8/20 * 8/20 + 5/20 * 5/20 = 0.345


### (ii)without replacement.
R+G+B = 5+7+8 = 20
	
P(2R) = P(R) + P(R|R) = 7/20 * 6/19 = 0.11053
P(2G) = P(G) + P(G|G) = 8/20 * 7/19 = 0.14737
P(2B) = P(B) + P(B|B) = 7/20 * 6/19 =  0.05
P(X|X) where X is R, G or B =  P(2R) + P(2G) + P(2B) = .30789
	


2) Suppose you have a fair dice with four sides (maybe a pyramid). You throw it four times.
-------------------------------------------------------------------------------------------


### (i)What is the probability of throwing a 4 first, then three other numbers?
1/4 * 3/4 * 3/4 * 3/4 = 0.10547
	

### (ii)Use the binomial formula to compute the probability of throwing exactly one 4 in four throws. (Hint: Multiply the probability found above with the factor prescribed by the binomial formula. Can you see why this is the right factor?)
binomial formula = factorial(4)/(factorial(1)*factorial(4-1)) = 4
1/4 * 3/4 * 3/4 * 3/4 * 4= 0.10547 *4 = 0.42188


### (iii) Same question for the probability of throwing exactly two 4’s in four throws.
binomial formula = factorial(4)/(factorial(2)*factorial(4-2)) = 6
1/4 * 1/4 * 3/4 * 3/4 * 6= 0.-34146 *6  = 0.21094
	

### (iv) Same question for the probability of throwing exactly four 4’s in four throws.
binomial formula = factorial(4)/(factorial(4)*factorial(4-4)) = 1
1/4 * 1/4 * 3/4 * 3/4 * 1= 0.035156


### 3) What is the probability of throwing a one exactly three times in ten throws of a fair six-sided dice?

binomial = factorial(10)/(factorial(3)*factorial(7)) = 120
(1/6)^3 * (5/6)^7 *20 = 0.15505


### 4) A supermarket stocks eggs in boxes of 6, and 10% of the eggs are found to be cracked. Assuming that the cracked eggs are distributed at random and that the customer selects a box at random, what is the probability that the box that the customer selects will have no cracked eggs?

9/10^6= 0.53144

