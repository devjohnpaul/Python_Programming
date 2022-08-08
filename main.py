import pyfiglet

ascii_banner = pyfiglet.figlet_format("Quiz Me")
print(ascii_banner)

score = 0


class Main:
    def final_score():
        print("---------------------")
        print("| Your score:", str(score), "pts |")
        print("---------------------")

    def correct():
        print("-----------")
        print("√ Correct!")
        print("-----------")

    def wrong():
        print("-----------")
        print("X Wrong!")
        print("-----------")

    def question_level_one():
        global score
        score = 0
        q = input("1.What does CPU stand for? ")
        if q.lower() == "central processing unit":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("2.What does GPU stand for? ")
        if q.lower() == "graphics processing unit":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("3.What does RAM stand for? ")
        if q.lower() == "random access memory":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("4.What does ROM stand for? ")
        if q.lower() == "read only memory":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("5.What does SD Card stand for? ")
        if q.lower() == "secure digital card":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("6.What does USB stand for? ")
        if q.lower() == "universal serial bus":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("7.What does PSU stand for? ")
        if q.lower() == "power supply":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("8.What does AVR stand for? ")
        if q.lower() == "automatic voltage regulator":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("9.What does UPS stand for? ")
        if q.lower() == "uninterruptible power supply":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("10.What does LCD stand for? ")
        if q.lower() == "liquid crystal display":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        Main.final_score()

    def question_level_two():
        global score
        score = 0
        q = input("1.The discovery of Internet started in the year ____. ")
        if q.lower() == "1960":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("2.A network made by ARPA wherein if one section is damaged could not affect other computer. ")
        if q.lower() == "arpanet":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("3.It is an information highway that links billions of computer all over the world. ")
        if q.lower() == "internet":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("4.The person behind the development of World Wide Web. ")
        if q.lower() == "tim berners lee":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("5.The CEO and co-founder of Facebook. ")
        if q.lower() == "mark zuckerberg":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("6.The chairman and co-founder of Microsoft Corporation. ")
        if q.lower() == "bill gates":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("7.An open source operating system developed by Google powering billions of smartphones worldwide. ")
        if q.lower() == "android":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("8.An OS used for Smart TVs ")
        if q.lower() == "webos":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("9.A mobile operating system for Apple Devices. ")
        if q.lower() == "ios":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("10.The original smartphone OS used by Nokia devices. ")
        if q.lower() == "symbian":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("11.LTE stands for ____. ")
        if q.lower() == "long term evolution":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("12.IT stands for ____. ")
        if q.lower() == "information technology":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("13.Unwanted email mostly from bots ")
        if q.lower() == "spam":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("14.Disguised as a useful program but is not ")
        if q.lower() == "trojan":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("15.Designed to send you advertisements ")
        if q.lower() == "adware":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("16.Exploits the DNS system ")
        if q.lower() == "pharming":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("17.Runs in the background and monitors what you are doing ")
        if q.lower() == "spyware":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("18.A browser feature synonymous to private browsing ")
        if q.lower() == "incognito":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("19.ARPA ")
        if q.lower() == "advance research projects agency ":
            Main.correct()
            score += 1
        else:
            Main.wrong()
        
        q = input("20.CERN ")
        if q.lower() == "european center and nuclear research ":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("21.W3C ")
        if q.lower() == "world wide web consurtion ":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("22.HTTP ")
        if q.lower() == "hypertext transfer protocol ":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("23.HTML ")
        if q.lower() == "hypertext markup language ":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("24.CSS ")
        if q.lower() == "cascading stylesheet ":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("25.PHP ")
        if q.lower() == "hypertext preprocessor ":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("26.COMPUTER ")
        if q.lower() == " common operating machine particularly used for technical education and research.":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("27.Stands for malicious software.")
        if q.lower() == "malware":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("28.VPN ")
        if q.lower() == "virtual private network":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("29.VPS ")
        if q.lower() == "virtual private server":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        q = input("30.TCP ")
        if q.lower() == "transmission control protocol":
            Main.correct()
            score += 1
        else:
            Main.wrong()

        # q = input("")
        # if q.lower() == "":
        #     Main.correct()
        #     score += 1
        # else:
        #     Main.wrong()

        Main.final_score()


print("------------------------")
print("A Computer Quiz Game")
print("------------------------")
print("1.Easy - 10 items")
print("2.Medium - 30 items")
print("3.Hard - 60 items")
print("0.Exit")

print("------------------------")
user = input("Choose a difficulty: ")
print("------------------------")

# Main Function
while user != "0":
    if user == "1":
        Main.question_level_one()
        break
    elif user == "2":
        Main.question_level_two()
        break
    elif user == "3":
        Main.question_level_three()
        break
    else:
        print("Invalid Input, Try Again!")
        print("------------------------")
        user = input("Choose a difficulty: ")
        print("------------------------")
