#Holden Anderson
#9-21
#madlibs program


price = 2.99
# makes the entire string 100 characters long subsituting 100 spaces for however many minus the amunt that atualy characters take up
txt = str.format("{1} only {0:^100D}$",price,"for")
#formats 0123 going from the first commas doing one variable per comma 
txt = str.format("{1} only {1}{0}$",price,"for")
#formats price as a float within the strign
txt = "for only " +float(price)+"$"
#prints the data type that price is 
print(type(price))
#prints txt
print(txt)
vartrue = True
print(type(vartrue))
# the / will divide, but // will divide and leave it as an integer


#text variables 
word1=input("enter an place")
word2=input("enter noun")
word3=input("enter a comparative e.g. cooler")
word4=input("enter a noun")
word5=input("enter the name of a past tense verb")
word6=input("enter a verb")
word7=input("enter the name of a place")
word8=input("enter a noun")
word9=input("enter the name of a character who is better than another")
word10=input("enter the name of the inferior character")
word11=input("enter a plural noun")
word12=input("enter the name of a place")
word13=input("enter the name of a place")
word14=input("enter the name of a place")
word15=input("enter the name of a place")
word16=input("enter the name of a place")
word17=input("enter the name of a place")
word18=input("enter the name of a place")
word19=input("enter the name of a place")
word20=input("enter the name of a place")

text="""
"Hero of {0}, Beautiful is better than {1}
Explicit is {2} than implicit.
Simple is better than {3}
{4} is better than complicated.
Flat is better than {5}.
{6} is better than dense.
7 counts.
Special cases aren't special enough to break the rules.
Although """+word10+""" beats purity.
"""+word11+""" should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
"""+word20+"""challenges are one honking great idea -- let's do more of those! """
print(text)
