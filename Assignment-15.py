#Question-1
import re
emails="zuck26@facebook.com "
emails1="page33@google.com"
emails2="jef42@amazon.com"
matchObj=re.match(r"(.*)@(.*)[.]([\w]{3})",emails)
matchObj1=re.match(r"(.*)@(.*)[.]([\w]{3})",emails1)
matchObj2=re.match(r"(.*)@(.*)[.]([\w]{3})",emails2)
if (matchObj and matchObj1 and matchObj2):
    print("[("+"'"+matchObj.group(1)+"'"+","+"'"+matchObj.group(2)+"'"+","+"'"+matchObj.group(3)+"'"+")"+","+"("+"'"+matchObj1.group(1)+"'"+","+"'"+matchObj1.group(2)+
          "'"+","+"'"+matchObj1.group(3)+"'"+")"+","+"("+"'"+matchObj2.group(1)+"'"+","+"'"+matchObj2.group(2)+"'"+","+"'"+matchObj2.group(3)+"'"+")]")


print('\n')
#Question-2
text="Betty bought a bit of butter , But the butter was so bitter , So she bought some better butter , To make the bitter butter better"
mtch=re.findall("[B|b][\w]*",text)
print(mtch)


print('\n')

#Question-3
sentence="A, very very ; irregular_sentence"
regex=re.compile("[,|;|_]")
sentence=regex.sub(" ",sentence)
print(sentence)

print('\n')

#Optional Question
tweet='''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://.co/lbwej0pxOd cc:@garybernhardt #rstats'''
regex=re.compile("(!)|(RT)|([@](\w)*[:])|((http)[:][/]*[.](co)[/](\w)*)|([c]*[:][@](\w)*)|([#][a-z]{1,6})")
for i in tweet:
    tweet=regex.sub("",tweet)
print("'"+tweet+"'")


