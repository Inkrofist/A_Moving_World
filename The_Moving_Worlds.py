"""
Title: The Moving World
Date: 08/04/18 - 08/06/18
Author: Trevor Jackson
"""
import time
import random
"""
Possible character names:
Elia Gil
"""

arlo_error_response = ["'I'm not sure if I caught what you said. Could you say it again for me?...'",
                       "'Sorry boy, I didn't quite catch that. Would you say it again for me?...'",
                       "'I'm sorry son, my hearing isn't too good, could you repeat yourself?...'",
                       "'Whaddya say?...'",
                       "'Come again son?...'"]
terminal_error_response = ["PLEASE TRY AGAIN", "ERROR", "THAT IS NOT RECOGNIZED"]


print """
     -----
    --- ---
   ---   --- 
  ---     --- 
 -------------   
 -------------   
 ---       ---
 ---       ---

 ---       ---   --------   ---       ---  -----------  ---    ---   ----------
 ----     ----  ----------  ---       ---  -----------  ----   ---  -----------
 -----   -----  ---    ---  ---       ---      ---      -----  ---  ---
 --- ----- ---  ---    ---   ---     ---       ---      ------ ---  ---   
 ---  ---  ---  ---    ---    ---   ---        ---      --- ------  ---     ----
 ---  ---  ---  ---    ---     --- ---         ---      ---  -----  ---     ----
 ---       ---  ----------      -----      -----------  ---   ----  -----------
 ---       ---   --------        ---       -----------  ---    ---   ---------  

 ---       ---   --------   ---------   ---         -------
 ---       ---  ----------  ----------  ---         ----------
 ---  ---  ---  ---    ---  ---    ---  ---         ---    ----
 ---  ---  ---  ---    ---  ----------  ---         ---     ---
 --- ----- ---  ---    ---  ---------   ---         ---     ---
 -----   -----  ---    ---  ---  ---    ---         ---    ----
 ----     ----  ----------  ---   ---   ----------  ----------
 ---       ---   --------   ---    ---  ----------  -------

"""
#time.sleep(4)
print ""
print ""
print "'Hello?...'"
#time.sleep(2.5)
print "'You awake yet?...'"
#time.sleep(2.5)
print ""
print "You struggle, but manage, to open your eyes."
print ""
#time.sleep(3)
print "'Ah, finally, I was starting to get a bit worried there.'"
#time.sleep(3.5)
print ""
print "Your eyes dart towards the voice. It's a short man with an old pair of goggles that takes up the majority of his face."
#time.sleep(5)
print ""
print "'Where am I? Who are you?' you ask."
#time.sleep(3)
print ""
print "'Nowhere and no one special,' replies the man with his hardened voice,"
#time.sleep(3)
print "'but I was sure you were a gonner there.'"
#time.sleep(3)
print ""
print "'A gonner?'"
#time.sleep(2)
print "'What happened?' you ask getting a bit concerned."
#time.sleep(3)
print ""
print "You quickly try to get up from the bed only to feel a shot of pain down your spine."
#time.sleep(4)
print ""
print "'AAAaHHH!' You scream in pain."
#time.sleep(2)
print ""
print "'Slow down there,' the man cautions,"
#time.sleep(3)
print "'you damn nearly ruined all the work I've done on you.'"
#time.sleep(3)
print ""
print "The man gently pushes you back into a laying position."
print ""
#time.sleep(3)
print "'If you just wait there, I'll tell you everything.'"
#time.sleep(3)
print ""
print "Feeling somewhat reassured, you calm down and control your breathing."
#time.sleep(3)
print ""
print "'Alright, what do you want to know?...'"

def conversation_1():
    choice_1 = raw_input(" : 'Where am I?...' [1], 'What happened to my back?...' [2], 'Who am I?...' [3], 'I don't have any more questions...' [4] : ")
    if choice_1 == "1":#the town
       # time.sleep(1)
        print ""
        print "'Where exactly am I?' you inquire."
        #time.sleep(2)
        print ""
        print "'Ah, well, like I said before, nowhere special. This town has been cast into the shadows.' the man's voice wimpers."
        #time.sleep(7)
        print "'Once a great influence on the world, Pitterton made millions with its lumber factories and such.'"
        #time.sleep(7)
        print "'But you see, this world suffers, and Pitterton does too. Our city grew too big, eventually spanning hundreds of millions of acres.'"
        #time.sleep(7)
        print ""
        print "'Wow, that's incredible.' you say, fascinated."
        #time.sleep(3)
        print ""
        print "'Our greed drove us to destroy everything we had, the forests. Billions of trees lost each day, nature couldn't keep up.' you can see the dread on the poor man's face."
        #time.sleep(7)
        print "'Nowadays we are strugglers to survive. Each day pains every person living here, we dream about getting out, but only the lucky ones get away.'"
        #time.sleep(7)
        conversation_2()
    elif choice_1 == "2":#my back
        #time.sleep(1)
        print ""
        print "'What happened to my back?'"
        #time.sleep(2)
        print ""
        print "'A couple days ago, an old lady found you unconcious on a pile of hay.' the man replies."
        #time.sleep(4)
        print "'You were pretty beat up, bruises and cuts all over your body. It looks like you took a fall from an air baloon.'"
        #time.sleep(4)
        print ""
        print "'An air baloon?' you question."
        #time.sleep(3)
        print ""
        print "'Right, it's a surprise to us too, air baloons don't usually fly over here. They tend to avoid us at all times.'"
        #time.sleep(5)
        print "'Nonetheless, your third vertebrae took a lot of damage, it's a miracle you won't be in a wheelchair.' the man says with a bit of disbelief."
        #time.sleep(6)
        print ""
        print "'I don't know much more than that, do you have any more questions to ask?'"
        #time.sleep(4)
        print ""
        conversation_1()
    elif choice_1 == "3":#my name
        #time.sleep(1)
        print ""
        print "'What's my name?' you ask."
        #time.sleep(2)
        print ""
        print "'You don't know your own name? This is worse than I thought.' For the first time, the man looks somewhat worried."
        #time.sleep(5)
        print ""
        print "'You see, you were wearing a uniform from a faraway land, but no nametag was found on it.' he explains."
        #time.sleep(5)
        print "'If you truely have lost all of your memory, I pray you may recover your identity someday.'"
        #time.sleep(5)
        print ""
        print "'I hope you can find out who you are at some point. Do you have any more questions to ask?'"
        #time.sleep(4)
        print ""
        conversation_1()     
    elif choice_1 == "4":#progresses
        #time.sleep(1)
        print ""
        print "'I don't have any more questions to ask.' you reply."
        #time.sleep(3)
        print ""
        print "'Well then, I suggest you go back to sleep. This must have been quite the shock to your body.' the man explains."
        #time.sleep(4)
        print "'I'll leave you to rest some mor-'"
        #time.sleep(2)
        print ""
        print "You cut him off."
        #time.sleep(1)
        print ""
        print "'I must ask, what's your name?'"
        #time.sleep(2)
        print ""
        print "'Ah!' He exclaims, 'I almost forgot to introduce myself.'"
        #time.sleep(4)
        print "'My name is Arlo Westly, the community doctor here in Pitterton.' he explains."
        #time.sleep(6)
        print "'It's nice to meet you young lad, but I think it's time for you to go back to bed. For your health of course!'"
        #time.sleep(6)
        print ""
        print "You thank the man before he exits the room, and lie on the bed pondering about everything."
        #time.sleep(5)
        print ""
        print "You try to close your eyes to get some sleep, but can't stop thinking about yourself."
        #time.sleep(4)
        print ""
        print "'Who am I?'"
        #time.sleep(2)
        return
    else:#this is for typos
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        time.sleep(2)
        print ""
        conversation_1()

def conversation_2():
    choice_2 = raw_input(" : 'How do people escape?...' [1], 'What do you do to survive?...' [2], GO BACK... [3] : ")
    if choice_2 == "1":#Pitterton escape
        #time.sleep(1)
        print ""
        print "'How do people escape?' you ask."
        #time.sleep(2)
        print ""
        print "'Leaving town is the easy part, the hard part is making the thousands of miles on foot.'"
        #time.sleep(4)
        print "'Pitterton is abandoned, we can no longer fuel any vehicals or call for help.'"
        #time.sleep(4)
        print "'But we haven't lost hope yet, we believe Pitterton can be saved. For our glory!'"
        #time.sleep(4)
        print ""
        print "'Hopefully that answers that. Do you have any more questions to ask?'"
        #time.sleep(4)
        conversation_2()
    elif choice_2 == "2":#Pitterton survival
        #time.sleep(1)
        print ""
        print "'How do the Pitterton people survive?' you inquire."
        #time.sleep(2)
        print ""
        print "'Us Pittertons are fighters, you know. We'll never give up, no matter the challenge!'"
        #time.sleep(4)
        print "'We have created large rain containters and chemical filters for our water,' he says boastfully,"
        #time.sleep(7)
        print "'and inside our old research laboratories it's clean enough to grow produce and such."
        #time.sleep(7)
        print "'But the air here is the killer. The acidity of the water vapor and the radiation will burn your retinas if you aren't wearing protection."
        #time.sleep(7)
        print "Pointing at his large goggles he jokingly says,"
        #time.sleep(3)
        print "'These bad boys are what keep me in the game!'"
        #time.sleep(3)
        print ""
        print "The man lets out a roar of a laugh and you chuckle along with him to make things a little less akward."
        #time.sleep(4)
        print ""
        print "'That's how we do it here in Pitterton. Any more questions your thinking about?'"
        #time.sleep(4)
        conversation_2()
    elif choice_2 == "3":#goes back
        time.sleep(1)
        print ""
        print ""
        conversation_1()
        time.sleep(2)
        print ""
    else:#this is for typos
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        time.sleep(2)
        print ""
        conversation_2()
conversation_1()

print ""
user_name = raw_input(" : Who are you?... : ")
#time.sleep(1)
print ""
print "'%s is a good name for now.' you think to yourself." % (user_name)
#time.sleep(3)
print "'Having a name is a bit reassuring, even if temporary.' you also think."
#time.sleep(4)
print ""
print "After a while, you eventually manage to fall asleep..."
#time.sleep(3)
print "."
#time.sleep(1)
print "."
#time.sleep(1)
print "."
#time.sleep(3)
print "A screech is heard..."
#time.sleep(2)
print ""
print "You look around, but you are only surrounded by darkness."
#time.sleep(4)
print ""
print "Thunder and lightning in the background, a boom knocks you off the edge. But you manage to hold on."
#time.sleep(6)
print ""
print "A gloved hand reaches for you. The shadowy face's only highlight is his large nose."
#time.sleep(4)
print ""
print "'Hold on! I got you!' he yells over the booming background."
#time.sleep(4)
print ""
print "You can feel the air embalming your body. Completely frigid. Your body can feel the energy being drained out of you."
#time.sleep(6)
print ""
print "You feel the grip of his hand start to loosen, 'NO!' you scream."
#time.sleep(3)
print "."
#time.sleep(1)
print "."
#time.sleep(1)
print "."
#time.sleep(3)
print "You awaken with a cold sweat and your heart beating faster than ever before."
#time.sleep(4)
print ""
print "Relieved knowing that it was just a dream, you are able to calm down."
#time.sleep(4)
print ""
print "'Ah, good morning boy, have a nice rest?' you hear from the doorway."
#time.sleep(4)
print ""
print "'Not really.' you reply, remembering your dream vividly."
#time.sleep(3)
print "'Also, you don't have to call me boy anymore, you can call me %s for now.'" %(user_name)
#time.sleep(4)
print ""
print "'I'm sorry about that, but I have good news for you %s.' he says excitedly." %(user_name)
#time.sleep(5)
print "'If you think you're up for it, I'll officially allow you to leave your bed.'"
#time.sleep(4)
print "'You can check out a little bit of Pitterton too if you'd like.'"
#time.sleep(3)
print ""
print "'What do you say? Shall I give you a tour of our fantastic town?'"
#time.sleep(3)
print ""

def conversation_3():#tour or rest
    choice_3 = raw_input(" : Go on Arlo's tour... [1], Rest a while longer... [2] : ")
    if choice_3 == "1":
        conversation_5()
    elif choice_3 == "2":
        #time.sleep(1)
        print ""
        print "'I think I want to rest a bit longer.' you explain."
        #time.sleep(3)
        print ""
        print "'Well okay %s, whenever you want to go out, just holler!'" %(user_name)
        #time.sleep(3)
        print ""
        print "Arlo walk out of the room once again and you rest your head on your pillow."
        #time.sleep(4)
        print ""
        print "'What was that dream?' you think to yourself."
        #time.sleep(2.5)
        print "'Who was that man trying to help me?'"
        #time.sleep(2.5)
        print ""
        print "You take a sip of water from a cup on the bed-side table."
        #time.sleep(3)
        print ""
        print "'I must've been in shock.'"
        #time.sleep(2)
        print ""
        print "You close your eyes and try not to think about anything."
        #time.sleep(3)
        print "."
        #time.sleep(1)
        print "."
        #time.sleep(1)
        print "."
        #time.sleep(3)
        print "Another screech, although this time much quieter and more distorted."
        #time.sleep(4)
        print "You're surrounded by guardrails and a flag, its deep blue with a white half-circle in the center and stripes radiating out of it."
        #time.sleep(6)
        print "A ladder is placed behind you, going into the unknown."
        #time.sleep(3)
        print ""
        print "'Shall I go down the ladder?' you ponder."
        #time.sleep(3)
        conversation_6()     
    else:
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        print ""
        time.sleep(2)
        conversation_3()

def conversation_4():#forced tour
    choice_3 = raw_input(" : Go on Arlo's tour... [1] : ")
    if choice_3 == "1":
        time.sleep(1)
        conversation_5()
    else:
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        print ""
        time.sleep (2)
        conversation_4()
                    
def conversation_5():#progresses##text for arlo's tour ##timer
    print ""
    print "'Well, it sounds a bit better than being cooped up in here.' you answer."
    print ""
    print "'Great, I'll be happy to show you around Pitterton.' Arlo responds."
    print "'There are three people I want you to meet.' he explains."
    print "'Buffy Aiden the shopkeep, Julius Fletcher the scientist, and Evie Rupert.'"
    print "'Evie the one who found you and called for help. You should go and thank her you know.'"
    print ""
    print "Who do you want to go see first?"
    return


def conversation_6():#ladder or flag
        choice_4 = raw_input(" : Go down the ladder... [1], Examine flag... [2] : ")
        if choice_4 == "1":#ladder choice
            #time.sleep(1)
            print ""
            print "You decide to go down the ladder."
            #time.sleep(2)
            print "The sound of polite talk gets louder and louder as you descend."
            #time.sleep(4)
            print "When you reach the bottom it becomes clear where the sound is coming from. You turn around and see them."
            #time.sleep(5.5)
            print "Hundreds of shadowy beings, both masculine and feminine, are making conversation inside a ballroom just before they all go silent."
            #time.sleep(5.5)
            print ""
            print "Your eyes are directed by two spotlights, casting your attention onto a stage."
            #time.sleep(5)
            print "Following an unintelligable but energetic announcement, a woman appears on the stage."
            #time.sleep(5)
            print "Long flowing, golden brown hair and a bright, silky smooth red dress."
            #time.sleep(4)
            print "Your heart starts pounding, unlike everything else you've seen, she is clearly human, and she is beautiful too."
            #time.sleep(6)
            print ""
            print "You catch her attention for a brief moment before she starts smiling and then winks at you."
            #time.sleep(5)
            print ""
            print "Before you can open your mouth,"
            #time.sleep(2)
            print "'CRASH!!!'"
            #time.sleep(1)
            print ""
            print "The floor of the ballroom and stage quickly comes to a slant and all of the shadowy figures fall, trying to grab hold of anything they can."
            #time.sleep(6)
            print ""
            print "The woman screams to you,"
            #time.sleep(2)
            print "'Help me, please!'"
            #time.sleep(2)
            print ""
            print "'I'm coming, don't worry!' "
            #time.sleep(2)
            print ""
            print "But just as you start to run to her aid - "
            #time.sleep(3)
            print "."
            #time.sleep(1)
            print "."
            #time.sleep(1)
            print "."
            #time.sleep(3)
            print "You awake for the third time in this bed when you hear from the doorway."
            #time.sleep(3)
            print ""
            print "'Good morning %s!' a now familiar voice appears." %(user_name)
            #time.sleep(2.5)
            print ""
            print "'Good morning to you Arlo, how are you.' you reply still a bit groggy."
            #time.sleep(3)
            print ""
            print "'I'm just here to check on how you're doing this morning.'"
            #time.sleep(3)
            print ""
            print "'Well, I'm a bit tired, but overall I guess I'm doing just fine.'"
            #time.sleep(3)
            print ""
            print "'That's fantastic! What are your thoughts about taking a trip into town today?' Arlo asks invitingly."
            #time.sleep(4.5)
            print ""
            print "'I think I need some fresh air anyways.' you think to yourself."
            #time.sleep(3)
            conversation_4()

        elif choice_4 == "2":#examine flag
            #time.sleep(1)
            print ""
            print "You look at the flag:"
            #time.sleep(1.5)
            print "A solid blue, like the ocean, with the half-circle mimicing the sun, glimmering over the water."
            #time.sleep(5)
            print "You get the feeling you've seen it before but nothing really comes to mind."
            #time.sleep(4.5)
            print "You turn your attention towards the cheerful laughter and light conversation coming from below."
            #time.sleep(5)
            print ""
            print "'What's going on down there?' you whisper to yourself."
            #time.sleep(3)
            conversation_6()
        else:#error
            time.sleep(1)
            print ""
            print ""
            time.sleep(.2)
            print (random.choice(terminal_error_response))
            print ""
            time.sleep
            conversation_6()
                         
def conversation_7():#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@LITERALLY ALL OF THE STORY
    choice_5 = raw_input(" : Buffy Aiden... [1], Julius Fletcher... [2], Evie Rupert... [3] : ")
    if choice_5 == "1":#choose Buffy
        print ""
        print "You choose Buffy Aiden"
        choice_7 = 0
        choice_8 = 0
        conversation_14(choice_5, choice_7, choice_8)
    
    elif choice_5 == "2":#choose Julius
        print ""
        print "You choose Julius Fletcher"
        choice_6 = 0
        choice_8 = 0
        conversation_15(choice_5, choice_6, choice_8)

    elif choice_5 == "3":#choose Evie
        print ""
        print "You choose Evie Rupert"
        choice_6 = 0
        choice_7 = 0
        conversation_16(choice_5, choice_6, choice_7)
                                 
    else:#error
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        print ""
        time.sleep (2)
        conversation_7()






def conversation_8():
            choice_6 = raw_input(" : Julius Fletcher... [1], Evie Rupert... [2] : ")
            if choice_6 == "1":
                print ""
                print "You choose Julius Fletcher"
                choice_5 = "1"
                choice_6 = "1"
                choice_8 = "0"
                conversation_15(choice_5, choice_6, choice_8)
                
            elif choice_6 == "2":
                print ""
                print "You choose Evie Rupert"
                choice_5 = "1"
                choice_6 = "2"
                choice_7 = "0"
                conversation_16(choice_5, choice_6, choice_7)
                
            else:
                time.sleep(1)
                print ""
                print ""
                print (random.choice(arlo_error_response))
                print ""
                time.sleep (2)
                conversation_8()
                
def conversation_9():
            choice_7 = raw_input(" : Buffy Aiden... [1], Evie Rupert... [2] : ")
            if choice_7 == "1":
                print ""
                print "You choose Buffy Aiden"
                choice_5 = "2"
                choice_7 = "1"
                choice_8 = "0"
                conversation_14(choice_5, choice_7, choice_8)
                
            elif choice_7 == "2":
                print ""
                print "You choose Evie Rupert"
                choice_5 = "2"
                choice_6 = "0"
                choice_7 = "2"
                conversation_16(choice_5, choice_6, choice_7)
                
            else:
                time.sleep(1)
                print ""
                print ""
                print (random.choice(arlo_error_response))
                print ""
                time.sleep (2)
                conversation_9()
                
def conversation_10():
            choice_8 = raw_input(" : Buffy Aiden... [1], Julius Fletcher[2] : ")
            if choice_8 == "1":
                print ""
                print "You choose Buffy Aiden"
                choice_5 = "3"
                choice_7 = "0"
                choice_8 = "1"
                conversation_14(choice_5, choice_7, choice_8)
                
            elif choice_8 == "2":
                print ""
                print "You choose Julius Fletcher"
                choice_5 = "3"
                choice_6 = "0"
                choice_8 = "2"
                conversation_15(choice_5, choice_6, choice_8)
                
            else:
                time.sleep(1)
                print ""
                print ""
                print (random.choice(arlo_error_response))
                print ""
                time.sleep (2)
                conversation_10()

def conversation_11():
    choice_9 = raw_input(" : Buffy Aiden... [1] : ")
    if choice_9 == "1":
        print ""
        print "You choose Buffy Aiden"
        choice_5 = "0"
        choice_7 = "0"
        choice_8 = "0"
        conversation_14(choice_5, choice_7, choice_8)
        
    else:
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        print ""
        time.sleep (2)
        conversation_11()

def conversation_12():
    choice_10 = raw_input(" : Julius Fletcher... [1] : ")
    if choice_10 == "1":
        print ""
        print "You choose Julius Fletcher"
        choice_5 = "0"
        choice_6 = "0"
        choice_8 = "0"
        conversation_15(choice_5, choice_6, choice_8)

    else:
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        print ""
        time.sleep (2)
        conversation_12()

def conversation_13():
    choice_11 = raw_input(" : Evie Rupert... [1] : ")
    if choice_11 == "1":
        print ""
        print "You choose Evie Rupert"
        choice_5 = "0"
        choice_6 = "0"
        choice_7 = "0"
        conversation_16(choice_5, choice_6, choice_7)
       
    else:
        time.sleep(1)
        print ""
        print ""
        print (random.choice(arlo_error_response))
        print ""
        time.sleep (2)
        conversation_13()

def conversation_14(choice_5, choice_7, choice_8):#Buffy Aiden path
    if choice_5 == "1":
        print ""
        print "First choice"
        conversation_8()
        
    elif choice_7 == "1":
        print ""
        print "Second choice"
        conversation_13()
    
    elif choice_8 == "1":
        print ""
        print "Second choice"
        conversation_12()

    else:
        print ""
        print "Final choice"
        conversation_17()
   
def conversation_15(choice_5, choice_6, choice_8):#Julius Fletcher path
    if choice_5 == "2":
        print ""
        print "First choice"
        conversation_9()
        
    elif choice_8 == "2":
        print ""
        print "Second choice"
        conversation_11()
        
    elif choice_6 == "1":
        print ""
        print "Second choice"
        conversation_13()
        
    else:
        print ""
        print "Final choice"
        conversation_17()
                        
def conversation_16(choice_5, choice_6, choice_7):#Evie Rupert path
    if choice_5 == "3":
        print ""
        print "First choice"
        conversation_10()
        
    elif choice_7 == "2":
        print ""
        print "Second choice"
        conversation_11()
        
    elif choice_6 == "2":
        print ""
        print "Second choice"
        conversation_12()

    else:
        print ""
        print "Final choice"
        conversation_17()


def conversation_17():#Progress
    print ""
    print "finished test"

conversation_3()    
conversation_7()






















