#PARAMATERS#----------------------------------------------------------------------------------------

#Filename
FN = "password.txt"

#Salt (Bash your keyboard)
salt = "egrrhguidsrhgliuydrsjgeruysgw4ayiegreyusfgw"

#Paste (Find something from the internet or use an essay)
paste = '''         Another one got caught today, it's all over the papers.  "Teenager
Arrested in Computer Crime Scandal", "Hacker Arrested after Bank Tampering"...
        Damn kids.  They're all alike.

        But did you, in your three-piece psychology and 1950's technobrain,
ever take a look behind the eyes of the hacker?  Did you ever wonder what
made him tick, what forces shaped him, what may have molded him?
        I am a hacker, enter my world...
        Mine is a world that begins with school... I'm smarter than most of
the other kids, this crap they teach us bores me...
        Damn underachiever.  They're all alike.

        I'm in junior high or high school.  I've listened to teachers explain
for the fifteenth time how to reduce a fraction.  I understand it.  "No, Ms.
Smith, I didn't show my work.  I did it in my head..."
        Damn kid.  Probably copied it.  They're all alike.

        I made a discovery today.  I found a computer.  Wait a second, this is
cool.  It does what I want it to.  If it makes a mistake, it's because I
screwed it up.  Not because it doesn't like me...
                Or feels threatened by me...
                Or thinks I'm a smart ass...
                Or doesn't like teaching and shouldn't be here...
        Damn kid.  All he does is play games.  They're all alike.

        And then it happened... a door opened to a world... rushing through
the phone line like heroin through an addict's veins, an electronic pulse is
sent out, a refuge from the day-to-day incompetencies is sought... a board is
found.
        "This is it... this is where I belong..."
        I know everyone here... even if I've never met them, never talked to
them, may never hear from them again... I know you all...
        Damn kid.  Tying up the phone line again.  They're all alike...

        You bet your ass we're all alike... we've been spoon-fed baby food at
school when we hungered for steak... the bits of meat that you did let slip
through were pre-chewed and tasteless.  We've been dominated by sadists, or
ignored by the apathetic.  The few that had something to teach found us will-
ing pupils, but those few are like drops of water in the desert.

        This is our world now... the world of the electron and the switch, the
beauty of the baud.  We make use of a service already existing without paying
for what could be dirt-cheap if it wasn't run by profiteering gluttons, and
you call us criminals.  We explore... and you call us criminals.  We seek
after knowledge... and you call us criminals.  We exist without skin color,
without nationality, without religious bias... and you call us criminals.
You build atomic bombs, you wage wars, you murder, cheat, and lie to us
and try to make us believe it's for our own good, yet we're the criminals.

        Yes, I am a criminal.  My crime is that of curiosity.  My crime is
that of judging people by what they say and think, not what they look like.
My crime is that of outsmarting you, something that you will never forgive me
for.

        I am a hacker, and this is my manifesto.  You may stop this individual,
but you can't stop us all... after all, we're all alike. '''
#PARAMATERS#----------------------------------------------------------------------------------------
import hashlib
def opt1():
    file = open(FN, "w")
    text = input("Input your text here: ")
    enc = text + salt + paste
    h = hashlib.sha512()
    h.update(enc.encode('utf-8'))
    print(h.hexdigest())
    file.write(h.hexdigest())
def opt2():
    file = open(FN, "r")
    text = input("Input your text here: ")
    enc = text + salt + paste
    h = hashlib.sha512()
    h.update(enc.encode('utf-8'))
    hash = h.hexdigest()
    phash = file.read()
    if hash == phash:
        print("Success, the password is: " + text)
    else:
        print("Incorrect Text")
def main():
    options = ["[1] Encode Text", "[2] Match Text"]
    optionsIn = [0,1,25]
    a = optionsIn[1]
    b = optionsIn[2]
    print(options)
    input1 = input("Slect an option: ")
    if optionsIn[int(input1)] == a:
        opt1()
    elif optionsIn[int(input1)] == b:
        opt2()
    else:
        print("Exit Code 1")
        exit()
main()