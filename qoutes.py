#Eric Broadbent
#9-21

#Random""

import random

#Main


quote1='"Dub Dub is like the SuperBowl" -WWDC Guest'


quote2='"I\'d look at myself in the mirror and be like:\n maybe I do look like I have a frog in my'\
        +'\n mouth\" \n \t \t \t -Tom Holland'


quote3= '"If I had a nickle for every time I was dumb I would not have to be smart to make "'\
        +'a lot of money” \n \t \t \t -Mr. Andy Sandwich'


quote4='"The internet is forever" \n \t \t \t -Ferb'


quote5='"Good for you, dude. You found your passion and went for it- \n'\
        + '"crippling the US government along the way, but whatever…" \n \t \t \t – Katy'


quote6='"It’s the art of confusion; \n works great on stupid people. \n \t \t \t – Katy"'



quote7='"The present is theirs; the future, for which I really worked, is mine.\"\n \t \t \t -Nikola Tesla'


quote8='"Any sufficently advanced technology is insdistinguishable from '\
        +'magic\" \n \t \t \t -Arthur C. Clarke\'s 3rd law'


qoute9='"Okay sure you can make some toy sports car but you can\'t make a sedan '\
        +'you can\'t there\'s no way you could compete with the luxury sedans that are '\
        +'gasoline because they\'re the best and there\'s no way you can make an electric '\
        +'car that\'s like that, so we did\” -Elon Musk'


qoute10='"Oh my gosh Shang-Chi was so good I wish Chinese people were real"'




##num = random.randint(0,9)
##if num == 0:
##    print(qoute1)
##elif num == 1:
##    print(qoute2)
quotes=[quote1,quote2,quote3,quote4,quote5,quote6,quote7,quote8,quote9,quote10]
output = random.choice(qoutes).replace("*","\n \t \t \t")
output = output.replace("%","\n \n \n \n \n \t \t \t")
print(output)
##print(quote2.isalpha())
##print(qoute7.replace("i""EEE")

##end
input("Press enter to exit")
