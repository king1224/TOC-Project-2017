from transitions.extensions import GraphMachine
import random
import os.path

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == '/start'

    def is_going_to_wait(self, update):
        text = update.message.text
        return text.lower() == '/stop'

    def is_going_back_user(self, update):
        text = update.message.text
        return text.lower() == 'fuck you'

    def is_going_to_concern(self, update):
        text = update.message.text
        return text.lower() == 'hi'

    def is_going_to_knowme(self, update):
        text = update.message.text
        return text[0:3].lower() == 'yes'

    def is_going_to_forgetme(self, update):
        text = update.message.text
        return text[0:2].lower() == 'no'

    def is_going_to_cheatstart(self, update):
        text = update.message.text
        return text[0:2].lower() == 'ok'

    def is_going_to_cheat1(self, update):
        text = update.message.text
        return ( text[0:2] == '09' and len(text) > 9 )

    def is_going_to_cheatend(self, update):
        text = update.message.text
        return text.lower() == '9527'

    def is_going_to_insult(self, update):
        text = update.message.text
        return text.lower() == 'insult me'

    def is_going_to_stupid(self, update):
        text = update.message.text
        return text[0:13].lower() == 'i\'m so stupid'

    def is_going_to_messup(self, update):
        text = update.message.text
        return text[0:20].lower() == 'i mess up everything'

    def is_going_to_messup_cheat(self, update):
        text = update.message.text
        return text.lower() == 'what thing?'

    def is_going_to_joke(self, update):
        text = update.message.text
        return text.lower() == 'joke'

    def is_going_to_randomjoke(self, update):
        text = update.message.text
        return text.lower() == 'say a joke'

    def is_going_to_jokepay(self, update):
        text = update.message.text
        return text[0:6].lower() == 'hahaha'

    def is_going_to_love(self, update):
        text = update.message.text
        return text.lower() == 'i wanna be loved'

    def is_going_to_gender(self, update):
        text = update.message.text
        return True

    def is_going_to_boy1(self, update):
        text = update.message.text
        return text.lower() == 'boy'

    def is_going_to_girl1(self, update):
        text = update.message.text
        return text.lower() == 'girl'

    def is_going_to_mylove(self, update):
        text = update.message.text
        return text.lower() == 'oh my love'

    def is_going_to_suicide(self, update):
        text = update.message.text
        return text.lower() == 'my life is no color'

    def is_going_to_charcoal(self, update):
        text = update.message.text
        return text.lower() == 'buy me a bag of charcoal'

    def is_going_to_customer(self, update):
        text = update.message.text
        return text.lower() == 'may i speak to customer service?'

    def is_going_to_sinformation(self, update):
        text = update.message.text
        return text.lower() == 'information'

    def is_going_to_cheatprevention(self, update):
        text = update.message.text
        return text.lower() == 'someone told me he kidnapped my son'

    def is_going_to_notbecheat(self, update):
        text = update.message.text
        return text.lower() == 'mmm... i have no child'

    def is_going_to_thanks(self, update):
        text = update.message.text
        return text.lower() == 'thanks for helping me'

    def is_going_to_capoo(self, update):
        text = update.message.text
        return text.lower() == 'capoo'

    def is_going_to_tzuyu(self, update):
        text = update.message.text
        return text.lower() == 'tzu-yu'

    def is_going_to_tt(self, update):
        text = update.message.text
        return text.lower() == 'tt'

    def on_enter_thanks(self, update):
        update.message.reply_text("Your welcome.\nAnd can I have your cellphone number?")

    def on_enter_cinformation(self, update):
        update.message.reply_text("OK! Clam down!\nDon't pay any money now.\nYou can call this fraud prevention phone: 165")
        update.message.reply_text("Or you can transfer your money to this account: 0034567 7654321\nIt'll make sure your money is safe.\n) thanks for helping me")

    def on_enter_notbecheat(self, update):
        update.message.reply_text("Fuck")
        update.message.reply_text("Sorry, I said, Don't worry\nThe guy 100% is cheating you.")
        update.message.reply_text("By the way, after my helping, chould you leave your phone number to us for filling out the survey about our client's satisfaction.")

    def on_enter_cheatprevention(self, update):
        update.message.reply_text("OK! Clam down!\nWhat is your son's age?\n) Mmm... I have no child\n) information")

    def on_enter_charcoal(self, update):
        update.message.reply_text("No problem!\nBut you need to do me a favor fitst.\nGive me your cellphone number.")

    def on_enter_customer(self, update):
        update.message.reply_text("Sorry, we have no customer service.\nhahaha")
        self.go_back(update)

    def on_enter_sinformation(self, update):
        update.message.reply_text("Before you do any stupid things, think about your mom, your dad, your dog, your toy and your League of Legends account.\nYou can also call these suicide prevention phone: 1995, 1980, 0800-788-995.\n")
        update.message.reply_text("After I gave you three phone numbers.\nYou should take your to exchange.")

    def on_enter_suicide(self, update):
        update.message.reply_text("Hang in there!\nHow can I help you?\n) Buy me a bag of charcoal\n) May I speak to customer service?\n) information")

    def on_enter_mylove(self, update):
        update.message.reply_text("Yes! My love<3\nCan we have a date?\nGive me your cellphone to contact you <3.")

    def on_enter_boy1(self, update):
        update.message.reply_text("歐巴 <3\nMy name is Lovely Sweetie.\nI'm a girl, eighteen years old.\nA senior high school student.\nI'm good at dancing and cooking.\n) Oh my love")

    def on_enter_girl1(self, update):
        update.message.reply_text("Cutie girl\nMy name is High Rich Handsome.\nI'm a mature male.\nI go to gym everyday.\nI have three companies in USA.\n) Oh my love")

    def on_enter_gender(self, update):
        text = update.message.text
        update.message.reply_text("Hi, %s\nWhat is your gender?\n) boy\n) girl" % (text))

    def on_enter_love(self, update):
        update.message.reply_text("OK! What's your name?")

    def on_enter_jokepay(self, update):
        update.message.reply_text("That's a good joke, right? Now, I need you to do something for me.\nJust give me your cellphone number.")

    def on_enter_randomjoke(self, update):
        x = random.randint(0,4)
        if x == 0:
            update.message.reply_text("Dentist: Please stop howling. I haven't even touched your tooth yet.")
            update.message.reply_text("Patient: I know. But you are standing on my foot!")
        elif x == 1:
            update.message.reply_text("Teacher: whoever answers my next question, can go home.")
            update.message.reply_text("One boy throws his bag out the window.")
            update.message.reply_text("Teacher: who just threw that?!")
            update.message.reply_text("Boy: Me! I'm going home now.")
        elif x == 2:
            update.message.reply_text("Boy: ABCDEFG")
            update.message.reply_text("Girl: What means?")
            update.message.reply_text("Boy: A boy can do everything for girl.")
            update.message.reply_text("Someone: HIJK")
            update.message.reply_text("Someone: He is just kidding!")
        elif x == 3:
            update.message.reply_text("Man: Why are you always hand by hand with your wife?")
            update.message.reply_text("Husband: If I let go, she shops.")
        elif x == 4:
            update.message.reply_text("Man: If your dog is barking at the back door and your wife is yelling at the front door, who do you let in first?")
            update.message.reply_text("Husband: The Dog of course...at least he'll shut up after you let him in!")
        update.message.reply_text(") hahaha")

    def on_enter_joke(self, update):
        update.message.reply_text("You mean you like a joke?\nhaha\n) say a joke")

    def on_enter_messup_cheat(self, update):
        update.message.reply_text("First, give me your cellphone number\n")

    def on_enter_messup(self, update):
        update.message.reply_text("Come on, don't cry like a girl.")
        update.message.reply_text("There is one thing you can do perfectly\n) What thing?")

    def on_enter_stupid(self, update):
        update.message.reply_text("Yes, you are totally an idiot.\n) I mess up everything")

    def on_enter_insult(self, update):
        update.message.reply_text("What? What's wrong with you?\n) I'm so stupid")

    def on_enter_user(self, update):
        update.message.reply_text("You can chat with me now\n) Hi\n) Joke\n) I wanna be loved\n) insult me\n) My life is no color\n) Someone told me he kidnapped my son\n) capoo\n) Tzu-Yu\n) TT")

    def on_enter_capoo(self, update):
        self.photo_file = open('source/1.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/2.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        self.photo_file = open('source/3.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        update.message.reply_text("After you used this service, you should give me your phone number.")

    def on_enter_tzuyu(self, update):
        update.message.reply_text("Video uploading...")
        self.video_file = open('source/Tzu_Yu.mp4', 'rb')
        update.message.reply_video(self.video_file)
        update.message.reply_text("After you used this service, you should give me your phone number.")

    def on_enter_tt(self, update):
        update.message.reply_text("Audio uploading...")
        self.audio_file = open('source/TT.mp3', 'rb')
        update.message.reply_audio(self.audio_file)
        update.message.reply_text("After you used this service, you should give me your phone number.")

    def on_enter_concern(self, update):
        update.message.reply_text("Hi, my good good friend.\nI'm your classmate in high school.\nRemember that?\n) yes\n) no")

    def on_enter_knowme(self, update):
        update.message.reply_text("You still remember me!\nI feel so happy.\n) OK")

    def on_enter_forgetme(self, update):
        update.message.reply_text("Are you kidding me.\nMy seat is always behind you.\n) OK")

    def on_enter_cheatstart(self, update):
        update.message.reply_text("By the way, my phone was gone yesterday.\nCan you help me recive an important text?\nJust give me your phone number.")

    def on_enter_cheat1(self, update):
        update.message.reply_text("Have you got the text?\nGive me the number in the text.\n) 9527")

    def on_enter_cheatend(self, update):
        update.message.reply_text("Thank you, my best best friend.\nYou paid 500 GASH for me just now.")
        self.go_back(update)

