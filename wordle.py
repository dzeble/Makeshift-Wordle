from tkinter import Widget
from colorama import Cursor
from flask import g
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
import random
from urllib.request import urlopen
import re 



#designate the kv file 
Builder.load_file('wordle.kv')


#getting words from a dictionary website
word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
response = urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()
dataFiveList =[]
#looking for the 5 letter words from the list
for five in WORDS :
    if len(five) == 5:
    #putting all the 5 leter words in a list
        dataFiveList.append(five)
#random selection from the list of 5 letter words
randomFive =(random.choice(dataFiveList))
#printing the word in the console
print(randomFive)

#list that will have the letters of the word
kay = []

#generates the list values to put in the kay list
temp = list(randomFive.upper())
for dum in temp:
    kay.append(str(chr(dum)))
#variable to display the word(answer)
ans = "".join([str(item) for item in kay])




#word to guess
daword = randomFive

#split word into letters
print(kay)
stew = kay[0]
meat = kay[1]
soup = kay[2]
pepper = kay[3]
sauce = kay[4]

#list for each row
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []


#list to count which row we are on
game_count = []

class MyLayout(Widget):
    def test(self) :

        game_count.append("next")

        #give separated letters variables
        self.testString1 = stew
        self.testString2 = meat
        self.testString3 = soup
        self.testString4 = pepper
        self.testString5 = sauce

        #give each input text box text a variable for the first row
        trial1= self.ids.spot1.text
        trial2 = self.ids.spot2.text
        trial3 = self.ids.spot3.text
        trial4 = self.ids.spot4.text
        trial5 = self.ids.spot5.text
        #give each input text box text a variable for the second row
        trial6= self.ids.spot6.text
        trial7 = self.ids.spot7.text
        trial8 = self.ids.spot8.text
        trial9 = self.ids.spot9.text
        trial10 = self.ids.spot10.text
        #give each input text box text a variable for the third row
        trial11= self.ids.spot11.text
        trial12 = self.ids.spot12.text
        trial13 = self.ids.spot13.text
        trial14 = self.ids.spot14.text
        trial15 = self.ids.spot15.text
        #give each input text box text a variable for the fourth row
        trial16= self.ids.spot16.text
        trial17 = self.ids.spot17.text
        trial18 = self.ids.spot18.text
        trial19 = self.ids.spot19.text
        trial20 = self.ids.spot20.text
        #give each input text box text a variable for the fifth row
        trial21= self.ids.spot21.text
        trial22 = self.ids.spot22.text
        trial23 = self.ids.spot23.text
        trial24 = self.ids.spot24.text
        trial25 = self.ids.spot25.text
        #give each input text box text a variable for the sixth row
        trial26= self.ids.spot26.text
        trial27 = self.ids.spot27.text
        trial28 = self.ids.spot28.text
        trial29 = self.ids.spot29.text
        trial30 = self.ids.spot30.text

        row1 = [trial1,trial2,trial3,trial4,trial5]
        row2 = [trial6,trial7,trial8,trial9,trial10]
        row3 = [trial11,trial12,trial13,trial14,trial15]
        row4 = [trial16,trial17,trial18,trial19,trial20]
        row5 = [trial21,trial22,trial23,trial24,trial25]
        row6 = [trial26,trial27,trial28,trial29,trial30]
 

####
        #check if the first row is complete
        if row1 == kay :
            print("complete row")
            #display the answer
            self.ids.topLabel.text = ans
            #disable the boxes
            self.ids.spot1.disabled = True
            self.ids.spot2.disabled = True
            self.ids.spot3.disabled = True
            self.ids.spot4.disabled = True
            self.ids.spot5.disabled = True

        #if the answer was wrong
        if row1 != kay and\
             len(game_count) == 1:
             #disable boxes
            self.ids.spot1.disabled = True
            self.ids.spot2.disabled = True
            self.ids.spot3.disabled = True
            self.ids.spot4.disabled = True
            self.ids.spot5.disabled = True
            #move to the next row
            self.ids.spot6.disabled = False 
            self.ids.spot6.focus = True 

        #check if the letters match in the first row with the colours
        if trial1 == self.testString1:
            self.ids.spot1.background_color = (0,0.5,0,0.8)
        if trial1 != self.testString1 and trial1 in kay:
            self.ids.spot1.background_color = (0.2, 0.3,0.5,1)

        if trial2 == self.testString2:
            self.ids.spot2.background_color = (0,0.5,0,0.8)
        if trial2 != self.testString2 and trial2 in kay:
            self.ids.spot2.background_color = (0.2, 0.3,0.5,1)

        if trial3 == self.testString3:
            self.ids.spot3.background_color = (0,0.5,0,0.8)
        if trial3 != self.testString3 and trial3 in kay:
            self.ids.spot3.background_color = (0.2, 0.3,0.5,1)

        if trial4 == self.testString4:
            self.ids.spot4.background_color = (0,0.5,0,0.8)
        if trial4 != self.testString4 and trial4 in kay:
            self.ids.spot4.background_color = (0.2, 0.3,0.5,1)

        if trial5 == self.testString5:
            self.ids.spot5.background_color = (0,0.5,0,0.8)
        if trial5 != self.testString5 and trial5 in kay:
            self.ids.spot5.background_color = (0.2, 0.3,0.5,1)

        

####
         #check if the second row is complete
        if row2 == kay:
            print("complete row")
            self.ids.topLabel.text = ans

            self.ids.spot6.disabled = True
            self.ids.spot7.disabled = True
            self.ids.spot8.disabled = True
            self.ids.spot9.disabled = True
            self.ids.spot10.disabled = True

            
        if row2 != kay and\
            len(game_count) == 2:
            self.ids.spot6.disabled = True
            self.ids.spot7.disabled = True
            self.ids.spot8.disabled = True
            self.ids.spot9.disabled = True
            self.ids.spot10.disabled = True

            self.ids.spot11.disabled = False
            self.ids.spot11.focus = True

        #check if the letters match in the second row
        if trial6 == self.testString1:
            self.ids.spot6.background_color = (0,0.5,0,0.8)
        if trial6 != self.testString1 and trial6 in kay:
            self.ids.spot6.background_color = (0.2, 0.3,0.5,1)

        if trial7 == self.testString2:
            self.ids.spot7.background_color = (0,0.5,0,0.8)
        if trial7 != self.testString2 and trial7 in kay:
            self.ids.spot7.background_color = (0.2, 0.3,0.5,1)

        if trial8 == self.testString3:
            self.ids.spot8.background_color = (0,0.5,0,0.8)
        if trial8 != self.testString3 and trial8 in kay:
            self.ids.spot8.background_color = (0.2, 0.3,0.5,1)

        if trial9 == self.testString4:
            self.ids.spot9.background_color = (0,0.5,0,0.8)
        if trial9 != self.testString4 and trial9 in kay:
            self.ids.spot9.background_color = (0.2, 0.3,0.5,1)

        if trial10 == self.testString5:
            self.ids.spot10.background_color = (0,0.5,0,0.8)
        if trial10 != self.testString5 and trial10 in kay:
            self.ids.spot10.background_color = (0.2, 0.3,0.5,1)

####
         #check if the third row is complete
        if row3 == kay:
            print("complete row")
            self.ids.topLabel.text = ans

            self.ids.spot11.disabled = True
            self.ids.spot12.disabled = True
            self.ids.spot13.disabled = True
            self.ids.spot14.disabled = True
            self.ids.spot15.disabled = True

            
        if row3 != kay and\
            len(game_count) == 3:
            self.ids.spot11.disabled = True
            self.ids.spot12.disabled = True
            self.ids.spot13.disabled = True
            self.ids.spot14.disabled = True
            self.ids.spot15.disabled = True

            self.ids.spot16.disabled = False
            self.ids.spot16.focus = True


        #check if the letters match in the third row
        if trial11 == self.testString1:
            self.ids.spot11.background_color = (0,0.5,0,0.8)
        if trial11 != self.testString1 and trial11 in kay:
            self.ids.spot11.background_color = (0.2, 0.3,0.5,1)

        if trial12 == self.testString2:
            self.ids.spot12.background_color = (0,0.5,0,0.8)
        if trial12 != self.testString2 and trial12 in kay:
            self.ids.spot12.background_color = (0.2, 0.3,0.5,1)

        if trial13 == self.testString3:
            self.ids.spot13.background_color = (0,0.5,0,0.8)
        if trial13 != self.testString3 and trial13 in kay:
            self.ids.spot13.background_color = (0.2, 0.3,0.5,1)

        if trial14 == self.testString4:
            self.ids.spot14.background_color = (0,0.5,0,0.8)
        if trial14 != self.testString4 and trial14 in kay:
            self.ids.spot14.background_color = (0.2, 0.3,0.5,1)

        if trial15 == self.testString5:
            self.ids.spot15.background_color = (0,0.5,0,0.8)
        if trial15 != self.testString5 and trial15 in kay:
            self.ids.spot15.background_color = (0.2, 0.3,0.5,1)


####
         #check if the fourth row is complete
        if row4 == kay:
            print("complete row")
            self.ids.topLabel.text = ans

            self.ids.spot16.disabled = True
            self.ids.spot17.disabled = True
            self.ids.spot18.disabled = True
            self.ids.spot19.disabled = True
            self.ids.spot20.disabled = True

           
        if row4 != kay and\
            len(game_count) == 4:
            self.ids.spot16.disabled = True
            self.ids.spot17.disabled = True
            self.ids.spot18.disabled = True
            self.ids.spot19.disabled = True
            self.ids.spot20.disabled = True

            self.ids.spot21.disabled = False
            self.ids.spot21.focus = True

        #check if the letters match in the fourth row
        if trial16 == self.testString1:
            self.ids.spot16.background_color = (0,0.5,0,0.8)
        if trial16 != self.testString1 and trial16 in kay:
            self.ids.spot16.background_color = (0.2, 0.3,0.5,1)

        if trial17 == self.testString2:
            self.ids.spot17.background_color = (0,0.5,0,0.8)
        if trial17 != self.testString2 and trial17 in kay:
            self.ids.spot17.background_color = (0.2, 0.3,0.5,1)

        if trial18 == self.testString3:
            self.ids.spot18.background_color = (0,0.5,0,0.8)
        if trial18 != self.testString3 and trial18 in kay:
            self.ids.spot18.background_color = (0.2, 0.3,0.5,1)

        if trial19 == self.testString4:
            self.ids.spot19.background_color = (0,0.5,0,0.8)
        if trial19 != self.testString4 and trial19 in kay:
            self.ids.spot19.background_color = (0.2, 0.3,0.5,1)

        if trial20 == self.testString5:
            self.ids.spot20.background_color = (0,0.5,0,0.8)
        if trial20 != self.testString5 and trial20 in kay:
            self.ids.spot20.background_color = (0.2, 0.3,0.5,1)


####
         #check if the fifth row is complete
        if row5 == kay:
            print("complete row")
            self.ids.topLabel.text = ans

            self.ids.spot21.disabled = True
            self.ids.spot22.disabled = True
            self.ids.spot23.disabled = True
            self.ids.spot24.disabled = True
            self.ids.spot25.disabled = True

            
        if row5 != kay and\
            len(game_count) == 5:
            self.ids.spot21.disabled = True
            self.ids.spot22.disabled = True
            self.ids.spot23.disabled = True
            self.ids.spot24.disabled = True
            self.ids.spot25.disabled = True

            self.ids.spot26.disabled = False
            self.ids.spot26.focus = True

        #check if the letters match in the fifth row
        if trial21 == self.testString1:
            self.ids.spot21.background_color = (0,0.5,0,0.8)
        if trial21 != self.testString1 and trial21 in kay:
            self.ids.spot21.background_color = (0.2, 0.3,0.5,1)

        if trial22 == self.testString2:
            self.ids.spot22.background_color = (0,0.5,0,0.8)
        if trial22 != self.testString2 and trial22 in kay:
            self.ids.spot22.background_color = (0.2, 0.3,0.5,1)

        if trial23 == self.testString3:
            self.ids.spot23.background_color = (0,0.5,0,0.8)
        if trial23 != self.testString3 and trial23 in kay:
            self.ids.spot23.background_color = (0.2, 0.3,0.5,1)

        if trial24 == self.testString4:
            self.ids.spot24.background_color = (0,0.5,0,0.8)
        if trial24 != self.testString4 and trial24 in kay:
            self.ids.spot24.background_color = (0.2, 0.3,0.5,1)

        if trial25 == self.testString5:
            self.ids.spot25.background_color = (0,0.5,0,0.8)
        if trial25 != self.testString5 and trial25 in kay:
            self.ids.spot25.background_color = (0.2, 0.3,0.5,1)


####
         #check if the sixth row is complete
       
        if row6 == kay:
            print("complete row")
            self.ids.topLabel.text = ans

            self.ids.spot26.disabled = True
            self.ids.spot27.disabled = True
            self.ids.spot28.disabled = True
            self.ids.spot29.disabled = True
            self.ids.spot30.disabled = True

            
        if row6 != kay and\
            len(game_count) == 6:    
            self.ids.topLabel.text = ans

            self.ids.spot26.disabled = True
            self.ids.spot27.disabled = True
            self.ids.spot28.disabled = True
            self.ids.spot29.disabled = True
            self.ids.spot30.disabled = True

        #check if the letters match in the sixth row
        if trial26 == self.testString1:
            self.ids.spot26.background_color = (0,0.5,0,0.8)
        if trial26 != self.testString1 and trial26 in kay:
            self.ids.spot26.background_color = (0.2, 0.3,0.5,1)

        if trial27 == self.testString2:
            self.ids.spot27.background_color = (0,0.5,0,0.8)
        if trial27 != self.testString2 and trial27 in kay:
            self.ids.spot27.background_color = (0.2, 0.3,0.5,1)

        if trial28 == self.testString3:
            self.ids.spot28.background_color = (0,0.5,0,0.8)
        if trial28 != self.testString3 and trial28 in kay:
            self.ids.spot28.background_color = (0.2, 0.3,0.5,1)

        if trial29 == self.testString4:
            self.ids.spot29.background_color = (0,0.5,0,0.8)
        if trial29 != self.testString4 and trial29 in kay:
            self.ids.spot29.background_color = (0.2, 0.3,0.5,1)

        if trial30 == self.testString5:
            self.ids.spot30.background_color = (0,0.5,0,0.8)
        if trial30 != self.testString5 and trial30 in kay:
            self.ids.spot30.background_color = (0.2, 0.3,0.5,1)

        

    
   

        
            

        

class WordleApp(App):
    testtext = "yo"
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    WordleApp().run()