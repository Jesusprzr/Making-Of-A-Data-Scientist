library(SDSFoundations)
acl <- AustinCityLimits
macl <- acl[acl$Gender == 'M',]
table(acl$Gender)
genmmy <- table(macl$Grammy, macl$Genre)
barplot(genmmy, legend=T, beside=T)
table(macl$Grammy)
35/(46+35)
#0.4320988
prop.table(genmmy, 2)
table(macl$Grammy)
table(macl$Grammy, macl$Genre)
#Probability that a randomly selected male artist FROM EACH OF THE GENRES won a grammy?
#It said FROM EACH, that means within the genre, so the correct way of calculating
#or creating a prop.table was using also the 2, refering to the y axis separated, 
#country with countro, jazz with jazz, and so on... Because we want to know the 
#probability just within the genre.
table(acl$Facebook.100k)
agemmy <- table(acl$Facebook.100k, acl$Age.Group)
prop.table(agemmy, 2)
