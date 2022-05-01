#Let, P(X=0) = Pr
#P(X=1) = Pb

#No.of red balls = 5 and No.of blue balls = 10 i.e.,Total no.of balls = 15 implies,
Pr = 5/15 
Pb = 10/15 

#Checks for the probability condition i.e., less than or equals to 1 and greater than or equals to 0.
if Pr<=1 and Pr>=0:
   "continue"
if Pb<=1 and Pb>=0:
   "continue"
   
p = Pr + Pb

if p == 1:
  print("P(X=0) = 1/3 and P(X=1) = 2/3") 
