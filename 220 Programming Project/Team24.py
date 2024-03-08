import tkinter as tk

info = {}
# All of the hitter_info functions contain the player name and bio for each team
def orioles_hitter_info(name):
    player_info = {
        "Adley Rutschman": "Name: Adley Rutschman \nPosition: C \nNumber: 35 \nB/T: S/R \nAge: 26 \n2023 Stats: .277/.371/.809 20 HR 80 RBI",
        "Ryan Mountcastle": "Name: Ryan Mountcastle \nPosition: 1B \nNumber: 6 \nB/T: R/R \nAge: 27 \n2023 Stats: .289/.302/.802 14 HR 60 RBI",
        "Jackson Holliday": "Name: Jackson Holliday \nPosition: 2B \nNumber: 87 \nB/T: L/R \nAge: 19 \n2023 Stats: DNP (Rookie Season)",
        "Jordan Westburg": "Name: Jordan Westburg \nPosition: 3B\nNumber: 11\nB/T R/R: \nAge: 25\n2023 Stats: .260/.311/.715 3 HR 23 RBI",
        "Gunnar Henderson": "Name: Gunnar Henderson \nPosition: Ss\nNumber: 2\nB/T: L/R\nAge: 22 \n2023 Stats: .255/.325/.814 28 HR 82 RBI",
        "Austin Hays": "Name: Austin Hays \nPosition: LF\nNumber: 21\nB/T: R/R\nAge: 28\n2023 Stats: .275/.325/.769 16 HR 67 RBI",
        "Cedric Mullins": "Name: Cedric Mullins \nPosition: CF\nNumber: 31\nB/T: L/L\nAge: 29\n2023 Stats: .233/.305/.721 15 HR 74 RBI",
        "Anthony Santander": "Name: Anthony Santander \nPosition: RF\nNumber: 25\nB/T: S/R\nAge: 29\n2023 Stats: .257/.325/.797 28 HR 95 RBI",
        "Ryan O'Hearn": "Name: Ryan O'Hearn \nPosition: DH\nNumber: 32\nB/T: L/L\nAge: 30\n2023 Stats: .289/.322/.802 14 HR 60 RBI",

    }
    return player_info.get(name)

def display_info(name):
    global info
    info = orioles_hitter_info(name)

    root = tk.Tk()
    root.title("Player Information")

    label = tk.Label(root, text=info)
    label.pack()

    root.mainloop()

def yankees_hitter_info(name):
    player_info = {
        "Jose Trevino": "Name: Jose Trevino \nPosition: C\nNumber: 39\nB/T: R/R\nAge: 31\n2023 Stats: .210/.257/.569 4 HR 15 RBI",
        "Anthony Rizzo": "Name: Anthony Rizzo \nPosition: 1B\nNumber: 48\nB/T: L/L\nAge: 34\n2023 Stats: .244/.328/.706 12 HR 41 RBI",
        "Gleyber Torres": "Name: Gleyber Torres \nPosition: 2B \nNumber: 25\nB/T: R/R\nAge: 27\n2023 Stats: .273/.347/.800 25 HR 68 RBI",
        "DJ LeMahieu": "Name: DJ LeMahieu \nPosition: 3B\nNumber: 26\nB/T: R/R\nAge: 35\n2023 Stats: .243/.327/.717 15 HR 44 RBI",
        "Anthony Volpe": "Name: Anthony Volpe \nPosition: SS\nNumber: 11\nB/T: R/R\nAge: 22\n2023 Stats: .209/.283/.666 21 HR 60 RBI",
        "Alex Verdguo": "Name: Alex Verdugo \nPosition: LF\nNumber: 24\nB/T: L/L\nAge: 27\n2023 Stats: .264/.324/.745 13 HR 54 RBI",
        "Juan Soto": "Name: Juan Soto \nPosition: CF\nNumber: 22\nB/T: L/L\nAge: 25\n2023 Stats: .275/.410/.929 35 HR 109 RBI",
        "Aaron Judge": "Name: Aaron Judge \nPosition: RF\nNumber: 99\nB/T: R/R\nAge: 31\n2023 Stats: .267/.406/1.019 37 HR 75 RBI",
        "Giancarlo Stanton": "Name: Giancarlo Stanton \nPosition: DH\nNumber: 27\nB/T: R/R\nAge: 34\n2023 Stats: .191/.275/.695 24 HR 60 RBI"
    }
    return player_info.get(name)

     
      

def brewers_hitter_info(name):
    player_info = {
        "William Contreras": "Name: William Contreras \nPosition: C\nNumber: 24\nB/T: R/R\nAge: 26\n2023 Stats: .289/.367/.824 17 HR 78 RBI",
        "Rhys Hoskins": "Name: Rhys Hoskins \nPosition: 1B\nNumber: 12\nB/T: R/R\nAge: 30\n2023 Stats: DNP (Injured)",
        "Brice Turang": "Name: Brice Turang \nPosition: 2B\nNumber: 2\nB/T: L/R\nAge: 24\n2023 Stats: .218/.285/.585 6 HR 34 RBI",
        "Owen Miller": "Name: Owen Miller \nPosition: 3B\nNumber: 6\nB/T: R/R\nAge: 27\n2023 Stats: .261/.303/.674 5 HR 27 RBI",
        "Willy Adames": "Name: Willy Adames \nPosition: SS\nNumber: 27\nB/T: R/R\nAge: 28\n2023 Stats: .217/.310/.717 24 HR 80 RBI",
        "Christian Yelich": "Name: Christian Yelich \nPosition: LF\nNumber: 22\nB/T: L/R\nAge: 32\n2023 Stats: .278/.370/.817 19 HR 76 RBI",
        "Jackson Chourio": "Name: Jackson Chourio \nPosition: CF\nNumber: 11\nB/T: R/R\nAge: 19\n2023 Stats: DNP(Rookie Season)",
        "Sal Frelick": "Name: Sal Frelick \nPosition: RF\nNumber: 10\nB/T: L/R\nAge: 23\n2023 Stats: .246/.341/.694 3 HR 24 RBI",
        "Gary Sánchez": "Name: Gary Sánchez \nPosition: DH\nNumber: 99\nB/T: R/R\nAge: 31\n2023 Stats: .217/.288./780 19 HR 47 RBI"
    }
    return player_info.get(name)


     
      

def bluejays_hitter_info(name):
    player_info = {
        "ALejandro Kirk": "Name: Alejandro Kirk \nPosition: C \nNumber: 30\nB/T: R/R\nAge: 25\n2023 Stats: .250/.334/.692 8 HR 43 RBI",
        "Vladimir Guerrero Jr.": "Name: Vladimir Guerrero Jr. \nPosition: 1B\nNumber: 27\nB/T: R/R\nAge: 24\n2023 Stats: .264/.345/.789 26 HR 94 RBI",
        "Cavan Biggio": "Name: Cavan Biggio \nPosition: 2B\nNumber: 8\nB/T: L/R\nAge: 28\n2023 Stats: .235/.340/.710 9 HR 40 RBI",
        "Isiah Kiner-Falefa": "Name: Isiah Kiner-Falefa \nPosition: 3B \nNumber: 7\nB/T: R/R\nAge: 7\n2023 Stats: .242/.306/.646 6 HR 37 RBI",
        "Bo Bichette": "Name: Bo Bichette \nPosition: SS\nNumber: 11\nB/T: R/R\nAge: 25\n2023 Stats: .306/.339/.814 20 HR 73 RBI",
        "George Springer": "Name: George Springer \nPosition: LF: \nNumber: 4\nB/T: R/R\nAge: 34\n2023 Stats: .258/.327/.732 21 HR 72 RBI",
        "Kevin Kiermaier": "Name: Kevin Kiermaier \nPosition: CF\nNumber: 39\nB/T: L/R\nAge: 33\n2023 Stats: .265/.322/.741 8 HR 36 RBI",
        "Daulton Varsho": "Name: Daulton Varsho \nPosition: RF\nNumber: 25\nB/T: L/R\nAge: 27\n2023 Stats: .220/.285/.674 20 HR 61 RBI",
        "Justin Turner": "Name: Justin Turner \nPosition: DH\nNumber: 2\nB/T: R/R\nAge: 39\n2023 Stats: .276/.345/.800 23 HR 96 RBI"
    }
    return player_info.get(name)

      

     
      

def redsox_hitter_info(name):
    player_info = {
        "Reese McGuire": "Name: Reese McGuire\nPosition: C\nNumber: 3\nB/T: L/R\nAge: 28\n2023 Stats: .267/310./688 1 HR 16 RBI",
        "Triston Casas": "Name: Triston Casas\nPosition: 1B\nNumber: 36\nB/T: L/R\nAge: 24\n2023 Stats: .263/.367/.857 24 HR 65 RBI",
        "Enmanuel Valdez": "Name: Enmanuel Valdez\nPosition: 2B\nNumber: 47\nB/T: L/R\nAge: 25\n2023 Stats: .266/.311/.764 6 HR 19 RBI",
        "Rafael Devers": "Name: Rafael Devers\nPosition: 3B\nNumber: 11\nB/T: L/R\nAge: 27\n2023 Stats: .271/.351/.851 33 HR 100 RBI",
        "Trevor Story": "Name: Trevor Story\nPosition: SS\nNumber: 10\nB/T: R/R\nAge: 31\n2023 Stats: .203/.250/.566 3 HR 14 RBI",
        "Masataka Yoshida": "Name: Masataka Yoshida\nPosition: LF\nNumber: 7\nB/T: L/R\nAge: 30\n2023 Stats: .289/.338/.783 15 HR 72 RBI",
        "Jarren Duran ": "Name: Jarren Duran\nPosition: CF\nNumber: 16\nB/T: L/R\nAge: 27\n2023 Stats: .295/.346/.828 8 HR 40 RBI",
        "Tyler O'Neill": "Name: Tyler O'Neill\nPosition: RF\nNumber: 17\nB/T: R/R\nAge: 28\n2023 Stats: .231/.312/.715 9 HR 21 RBI",
        "Bobby Dalbec": "Name: Bobby Dalbec\nPosition: DH\nNumber: 29\nB/T: R/R\nAge: 28\n2023 Stats: .204/.264/.570 1 HR 1 RBI"
    }
    return player_info.get(name)

       
     
      

def rays_hitter_info(name):
    player_info = {
        "René Pinto": "Name: René Pinto\nPosition: C\nNumber: 50\nB/T: R/R\nAge: 27\n2023 Stats: .252/.267/.723 6 HR 16 RBI",
        "Yandy Díaz": "Name: Yandy Díaz\nPosition: 1B\nNumber: 2\nB/T: R/R\nAge: 32\n2023 Stats: .330/.410/.932 22 HR 78 RBI",
        "Brandon Lowe": "Name: Brandon Lowe\nPosition: 2B\nNumber: 8\nB/T: L/R\nAge: 29\n2023 Stats: .231/.328/.771 21 HR 68 RBI",
        "Junior Caminero": "Name: Junior Caminero\nPosition: 3B\nNumber: 13\nB/T: R/R\nAge: 20\n2023 Stats: DNP(Rookie Season)",
        "Taylor Walls": "Name: Taylor Walls\nPosition: SS\nNumber: 6\nB/T: S/R\nAge: 27\n2023 Stats: .201/.305/.638 8 HR 36 RBI",
        "Randy Arozarena": "Name: Randy Arozarena\nPosition: LF\nNumber: 56\nB/T: R/R\nAge: 29\n2023 Stats: .254/.364/.789/.23 HR 83 RBI",
        "Jose Siri": "Name: Jose Siri\nPosition: CF\nNumber: 22\nB/T: R/R\nAge: 28\n2023 Stats: .222/.267/.761 25 HR 56 RBI",
        "Josh Lowe": "Name: Josh Lowe\nPosition: RF\nNumber: 15\nB/T: L/R\nAge: 26\n2023 Stats: .292/.335/.835 20 HR 83 RBI",
        "Harold Ramirez": "Name: Harold Ramirez\nPosition: DH\nNumber: 43\nB/T: R/R\nAge: 29\n2023 Stats: .313/.353/.813 12 HR 68 RBI"

    }
    return player_info.get(name)

      

     
      

def tigers_hitter_info(name):
    player_info = {
        "Carson Kelly": "Name: Carson Kelly\nPosition: C\nNumber: 15\nB/T: R/R\nAge: 29\n2023 Stats: .206/.278/.565 2 HR 13 RBI",
        "Spencer Torkleson": "Name: Spencer Torkleson\nPosition: 1B\nNumber: 20\nB/T: R/R\nAge: 24\n2023 Stats: .233/.313/.759 31 HR 94 RBI",
        "Colt Keith": "Name: Colt Keith\nPosition: 2B\nNumber: 33\nB/T: L/R\nAge: 22\n2023 Stats: DNP(Rookie Season)",
        "Gio Urshela": "Name: Gio Urshela\nPosition: 3B\nNumber: 13\nB/T: R/R\nAge: 32\n2023 Stats: .299/.329/.703 2 HR 24 RBI",
        "Javier Báez": "Name: Javier Báez\nPosition: SS\nNumber: 28\nB/T: R/R\nAge: 31\n2023 Stats: .222/.267/.592 9 HR 59 RBI",
        "Akil Baddoo": "Name: Akil Baddoo\nPosition: LF\nNumber: 60\nB/T: L/L\nAge: 25\n2023 Stats: .218/.310/.682 11 HR 34 RBI",
        "Riley Greene": "Name: Riley Greene\nPosition: CF\nNumber: 31\nB/T: L/L\nAge: 23\n2023 Stats: .288/.349/.796 11 HR 37 RBI",
        "Matt Vierling": "Name: Matt Vierling\nPosition: RF\nNumber: 8\nB/T: R/R\nAge: 27\n2023 Stats: .261/.329/.717 10 HR 44 RBI",
        "Mark Canha": "Name: Mark Canha\nPosition: DH\nNumber: 21\nB/T: R/R\nAge: 35\n2023 Stats: .262/.355/.755 11 HR 62 RBI"
    }
      

     
      
def indians_hitter_info(name):
    player_info = {
        "Austin Hedges": "Name: Austin Hedges\nPosition: C\nNumber: 27\nB/T: R/R\nAge: 31\n2023 Stats: .184/.234/.461 1 HR 16 RBI",
        "Josh Naylor": "Name: Josh Naylor\nPosition: 1B\nNumber: 22\nB/T: L/L\nAge: 26\n2023 Stats: .308/.354/.843 17 HR 97 RBI",
        "Andrés Giménez": "Name: Andrés Giménez\nPosition: 2B\nNumber: 0\nB/T: L/R\nAge: 25\n2023 Stats: .251/.314/.713 15 HR 62 RBI",
        "José Ramírez": "Name: José Ramírez\nPosition: 3B\nNumber: 11\nB/T: S/R\nAge: 31\n2023 Stats: .282/.356/.831 24 HR 80 RBI",
        "Juan Brito": "Name: Juan Brito\nPosition: SS\nNumber: 74\nB/T: S/R\nAge: 22\n2023 Stats: DNP(Rookie Season)",
        "Steven Kwan": "Name: Steven Kwan\nPosition: LF\nNumber: 38\nB/T: L/L\nAge: 26\n2023 Stats: .268/.340/.710 5 HR 54 RBI",
        "Myles Straw": "Name: Myles Straw\nPosition: CF\nNumber: 7\nB/T: R/R\nAge: 29\n2023 Stats: .238/.301/.598 1 HR 29 RBI",
        "Ramón Laureano": "Name: Ramón Laureano\nPosition: RF\nNumber: 10\nB/T: R/R\nAge: 29\n2023 Stats: .224/.304/.675 9 HR 35 RBI",
        "Bo Naylor": "Name: Bo Naylor\nPosition: DH\nNumber: 23\nB/T: L/R\nAge: 24\n2023 Stats: .237/.339/.809 11 HR 32 RBI"
    }
    return player_info.get(name)

      
     
      

def whitesox_hitter_info(name):
    player_info = {
        "Martín Maldonado": "Name: Martín Maldonado\nPosition: C\nNumber: 15\nB/T: R/R\nAge: 37\n2023 Stats: .191/.258/.606 15 HR 36 RBI",
        "Andrew Vaughn": "Name: Andrew Vaughn\nPosition: 1B\nNumber: 25\nB/T: R/R\nAge: 25\n2023 Stats: .258/.314/.743 21 HR 80 RBI",
        "Nicky Lopez": "Name: Nicky Lopez\nPosition: 2B\nNumber: 8\nB/T: L/R\nAge: 28\n2023 Stats: .231/.326/.633 1 HR 25 RBI",
        "Yoán Moncada": "Name: Yoán Moncada\nPosition: 3B\nNumber: 10\nB/T: S/R\nAge: 28\n2023 Stats: .260/.305/.730 11 HR 40 RBI",
        "Paul DeJong": "Name: Paul DeJong\nPosition: SS\nNumber: 29\nB/T: R/R\nAge: 30\n2023 Stats: .207/.258/.613 14 HR 38 RBI",
        "Andrew Benintendi": "Name: Andrew Benintendi\nPosition: LF\nNumber: 23\nB/T: L/L\nAge: 29\n2023 Stats: .262/.326/.682 5 HR 45 RBI",
        "Luis Robert Jr.": "Name: Luis Robert Jr.\nPosition: CF\nNumber: 88\nB/T: R/R\nAge: 26\n2023 Stats: .264/.315/.857 38 HR 80 RBI",
        "Gavin Sheets": "Name: Gavin Sheets\nPosition: RF\nNumber: 32\nB/T: L/L\nAge: 27\n2023 Stats: .203/.267/.598 10 HR 43 RBI",
        "Eloy Jiménez": "Name: Eloy Jiménez\nPosition: DH\nNumber: 74\nB/T: R/R\nAge: 27\n2023 Stats: .272/.317/.758 18 HR 64 RBI"
    }
    return player_info.get(name)

      
     
      

def royals_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

      
     
      

def twins_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def marlins_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def rangers_hitter_info(name):
    player_info = {
       "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def nationals_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def braves_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def diamondbacks_hitter_info(name):
    player_info = {
        "Gabriel Moreno": "Name: Gabriel Moreno\nPosition: C\nNumber: 14\nB/T: R/R\nAge: 24\n2023 Stats: .284/.339/.747 7 HR 50 RBI",
        "Christian Walker": "Name: Christian Walker\nPosition: 1B\nNumber: 53\nB/T: R/R\nAge: 32\n2023 Stats: .258/.333/.830 33 HR 103 RBI",
        "Ketel Marte": "Name: Ketel Marte\nPosition: 2B\nNumber: 4\nB/T: S/R\nAge: 30\n2023 Stats: .276/.358/.843 25 HR 82 RBI",
        "Eugenio Suárez": "Name: Eugenio Suárez\nPosition: 3B\nNumber: 28\nB/T: R/R\nAge: 32\n2023 Stats: .232/.323/.714 22 HR 96 RBI",
        "Geraldo Perdomo": "Name: Geraldo Perdomo\nPosition: SS\nNumber: 2\nB/T: S/R\nAge: 24\n2023 Stats: .246/.353/.712 6 HR 47 RBI",
        "Lourdes Gurriel Jr.": "Name: Lourdes Gurriel Jr.\nPosition: LF\nNumber: 12\nB/T: R/R\nAge: 30\n2023 Stats: .261/.309/.772 24 HR 82 RBI",
        "Alek Thomas": "Name: Alek Thomas\nPosition: CF\nNumber: 5\nB/T: L/L\nAge: 23\n2023 Stats: .230/.273/.647 9 HR 39 RBI",
        "Corbin Carroll": "Name: Corbin Carroll\nPosition: RF\nNumber: 7\nB/T: L/L\nAge: 23\n2023 Stats: .285/.362/.868 25 HR 76 RBI",
        "Joc Pederson": "Name: Joc Pederson\nPosition: DH\nNumber: 3\nB/T: L/L\nAge: 31\n2023 Stats: .235/.348/.764 15 HR 51 RBI"
    }
    return player_info.get(name)

     
     
      

def phillies_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def mets_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def angels_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def astros_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def mariners_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def athletics_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def padres_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def dodgers_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def rockies_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def giants_hitter_info(name):
    player_info = {
        "Patrick Bailey": "Name: Patrick Bailey\nPosition: C\nNumber: 14\nB/T: S/R\nAge: 24\n2023 Stats: .233/.285/.644 7 HR 48 RBI",
        "Lamonte Wade Jr.": "Name: Lamonte Wade Jr.\nPosition: 1B\nNumber: 31\nB/T: L/L\nAge: 30\n2023 Stats: .256/.373/.790 17 HR 45 RBI",
        "Thairo Estrada": "Name: Thairo Estrada\nPosition: 2B\nNumber: 39\nB/T: R/R\nAge: 28\n2023 Stats: .271/.315/.732 14 HR 49 RBI",
        "Wilmer Flores": "Name: Wilmer Flores\nPosition: 3B\nNumber: 41\nB/T: R/R\nAge: 32\n2023 Stats: .284/.355/.864 23 HR 60 RBI",
        "Marco Luciano": "Name: Marco Luciano\nPosition: SS\nNumber: 37\nB/T: R/R\nAge: 22\n2023 Stats: .231/.333/.641 0 HR 0 RBI",
        "Jung Hoo Lee": "Name: Jung Hoo Lee\nPosition: LF\nNumber: 51\nB/T: L/R\nAge: 25\n2023 Stats: DNP(Rookie Season)",
        "Michael Conforto": "Name: Michael Conforto\nPosition: CF\nNumber: 8\nB/T: L/R\nAge: 31\n2023 Stats: .239/.334/.718 15 HR 58 RBI",
        "Mike Yastrzemski": "Name: Mike Yastrzemski\nPosition: RF\nNumber: 5\nB/T: L/L\nAge: 33\n2023 Stats: .233/.330/.775 15 HR 43 RBI",
        "Jorge Soler": "Name: Jorge Soler\nPosition: DH\nNumber: 2\nB/T: R/R\nAge: 32\n2023 Stats: .250/.341/.853 36 HR RBI 75"
    }
    return player_info.get(name)

     
     
      

def pirates_hitter_info(name):
    player_info = {
        "Yasmani Grandal": "Name: Yasmani Grandal\nPosition: C\nNumber: 6\nB/T: S/R\nAge: 35\n2023 Stats: .234/.309/.648 8 HR 33 RBI",
        "Rowdy Tellez": "Name: Rowdy Tellez\nPosition: 1B\nNumber: 44\nB/T: L/L\nAge: 28\n2023 Stats: .215/.291/.667 13 HR 47 RBI",
        "Ji Hwan Bae": "Name: Ji Hwan Bae\nPosition: 2B\nNumber: 3\nB/T: L/R\nAge: 24\n2023 Stats: .231/.296/.607 2 HR 32 RBI",
        "Ke’Bryan Hayes": "Name: Ke’Bryan Hayes\nPosition: 3B\nNumber: 13\nB/T: R/R\nAge: 27\n2023 Stats: .271/.309/.762 15 HR 61 RBI",
        "Oneil Cruz": "Name: Oneil Cruz\nPosition: SS\nNumber: 15\nB/T: L/R\nAge: 25\n2023 Stats: .250/.375/.750 1 HR 4 RBI",
        "Connor Joe": "Name: Connor Joe\nPosition: LF\nNumber: 2\nB/T: R/R\nAge: 31\n2023 Stats: .247/.339/.760 11 HR 42 RBI",
        "Bryan Reynolds": "Name: Bryan Reynolds\nPosition: CF\nNumber: 10\nB/T: S/R\nAge: 29\n2023 Stats: .263/.330/.790 24 HR 84 RBI",
        "Henry Davis": "Name: Henry Davis\nPosition: RF\nNumber: 32\nB/T: R/R\nAge: 24\n2023 Stats: .213/.302/.653 7 HR 24 RBI",
        "Andrew McCutchen": "Name: Andrew McCutchen\nPosition: DH\nNumber: 22\nB/T: R/R\nAge: 37\n2023 Stats: .256/.378/.775 12 HR 43 RBI"
    }
    return player_info.get(name)

     
     
      

def cubs_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def reds_hitter_info(name):
    player_info = {
        "": "Name: \nPosition: C\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 1B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 2B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: 3B\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: SS\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: LF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: CF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: RF\nNumber: \nB/T: \nAge: \n2023 Stats: ",
        "": "Name: \nPosition: DH\nNumber: \nB/T: \nAge: \n2023 Stats: "
    }
    return player_info.get(name)

     
     
      

def cardinals_hitter_info(name):
    player_info = {
        "Willson Contreras": "Name: Willson Contreras\nPosition: C\nNumber: 40\nB/T: R/R\nAge: 31\n2023 Stats: .264/.358/.825 20 HR 67 RBI",
        "Paul Goldschmidt": "Name: Paul Goldschmidt\nPosition: 1B\nNumber: 46\nB/T: R/R\nAge: 36\n2023 Stats: .268/.363/.810 25 HR 80 RBI",
        "Tommy Edman": "Name: Tommy Edman\nPosition: 2B\nNumber: 19\nB/T: S/R\nAge: 28\n2023 Stats: .248/.307/.706 13 HR 47 RBI",
        "Nolan Arenado": "Name: Nolan Arenado\nPosition: 3B\nNumber: 28\nB/T: R/R\nAge: 32\n2023 Stats: .266/.315/.774 26 HR 93 RBI",
        "Brandon Crawford": "Name: Brandon Crawford\nPosition: SS\nNumber: 35\nB/T: L/R\nAge: 37\n2023 Stats: .194/.273/.587 7 HR 38 RBI",
        "Dylan Carlson": "Name: Dylan Carlson\nPosition: LF\nNumber: 3\nB/T: S/L\nAge: 25\n2023 Stats: .219/.318/.651 5 HR 27 RBI",
        "Lars Nootbaar": "Name: Lars Nootbaar\nPosition: CF\nNumber: 21\nB/T: L/R\nAge: 26\n2023 Stats: .261/.367/.785 14 HR 46 RBI",
        "Jordan Walker": "Name: Jordan Walker\nPosition: RF\nNumber: 18\nB/T: R/R\nAge: 21\n2023 Stats: .276/.342/.787 16 HR 51 RBI",
        "Matt Carpenter": "Name: Matt Carpenter\nPosition: DH\nNumber: 13\nB/T: L/R\nAge: 38\n2023 Stats: .176/.322/.641 5 HR 31 RBI"
    }
    return player_info.get(name)

     
     
# This function contains a dictionary with all 30 MLB team names    
def team_names():
    teams = [
        "Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles", "Boston Red Sox",
        "Chicago White Sox", "Chicago Cubs", "Cincinnati Reds", "Cleveland Indians",
        "Colorado Rockies", "Detroit Tigers", "Houston Astros", "Kansas City Royals",
        "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins", "Milwaukee Brewers",
        "Minnesota Twins", "New York Yankees", "New York Mets", "Oakland Athletics",
        "Philadelphia Phillies", "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants",
        "Seattle Mariners", "St. Louis Cardinals", "Tampa Bay Rays", "Texas Rangers",
        "Toronto white Jays", "Washington Nationals"
    ]

    teams_window = tk.Toplevel()
    teams_window.title("Baseball Teams")

    for team in teams:
        label = tk.Label(teams_window, text=team, fg="white", cursor="hand2")
        label.bind("<Button-1>", lambda event, team=team: hitters(team))
        label.pack()
# This function makes the opening GUI page, the welcome screen
def welcome():
    welcome_window = tk.Tk()
    welcome_window.title("Welcome")

    welcome_button = tk.Button(welcome_window, text="Welcome to Team24, an interactive program made with Python \nthat allows you to look at the starting lineup \nof all 30 MLB teams for the 2024 season. \nClick this text to begin!", command=team_names)
    welcome_button.pack()
    welcome_window.geometry("400x400")
    welcome_window.mainloop()

# This section allows the program to match the name selected by the user to a name defined in team_names() on line 241
def hitters(team_name):
    if team_name == "Baltimore Orioles":
        orioles_hitters()
    elif team_name == "New York Yankees":
        yankees_hitters()
    elif team_name == "Tampa Bay Rays":
        rays_hitters()
    elif team_name == "Toronto white Jays":
        bluejays_hitters()
    elif team_name == "Boston Red Sox":
        redsox_hitters()
    elif team_name == "Cleveland Indians":
        indians_hitters()
    elif team_name == "Detroit Tigers":
        tigers_hitters()
    elif team_name == "Chicago White Sox":
        whitesox_hitters()
    elif team_name == "Kansas City Royals":
        royals_hitters()
    elif team_name == "Minnesota Twins":
        twins_hitters()
    elif team_name == "Houston Astros":
        astros_hitters()
    elif team_name == "Los Angeles Angels":
        angels_hitters()
    elif team_name == "Oakland Athletics":
        athletics_hitters()
    elif team_name == "Seattle Mariners":
        mariners_hitters()
    elif team_name == "Texas Rangers":
        rangers_hitters()
    elif team_name == "Atlanta Braves":
        braves_hitters()
    elif team_name == "Miami Marlins":
        marlins_hitters()
    elif team_name == "New York Mets":
        mets_hitters()
    elif team_name == "Philadelphia Phillies":
        phillies_hitters()
    elif team_name == "Washington Nationals":
        nationals_hitters()
    elif team_name == "Cincinnatti Reds":
        reds_hitters()
    elif team_name == "Chicago Cubs":
        cubs_hitters()
    elif team_name == "Milwaukee Brewers":
        brewers_hitters()
    elif team_name == "Pittsburgh Pirates":
        pirates_hitters()
    elif team_name == "St. Louis Cardinals":
        cardinals_hitters()
    elif team_name == "Los Angeles Dodgers":
        dodgers_hitters()
    elif team_name == "San Diego Padres":
        padres_hitters()
    elif team_name == "San Fransisco Giants":
        giants_hitters()
    elif team_name == "Arizona Diamondbacks":
        diamondbacks_hitters()
    elif team_name == "Colorado Rockies":
        rockies_hitters()
    elif team_name == "Cincinatti Reds":
        reds_hitters()
    else:
        print("Oops!")
    
# This section has all of the hitters functions 
# This is where each team's individual hitter page is formed

def orioles_hitters():
    orioles_window = tk.Tk()
    orioles_window.title("Baltimore Orioles Hitters")

    names = [
        "Adley Rutschman", "Ryan Mountcastle", "Jackson Holliday",
        "Jordan Westburg", "Gunnar Henderson", "Austin Hays",
        "Cedric Mullins", "Anthony Santander", "Ryan O'Hearn"
    ]

    for name in names:
        label = tk.Label(orioles_window, text=name, fg="white", cursor="hand2")
        label.bind("<Button-1>", lambda event, name=name: display_info(name))
                   
        label.pack()

    orioles_window.mainloop()

def yankees_hitters():
    yankees_window = tk.Tk()
    yankees_window.title("New York Yankees Hitters")

    names = [
        "Jose Trevino", "Anthony Rizzo", "Gleyber Torres", "DJ LeMahieu",
        "Anthony Volpe", "Alex Verdugo", "Juan Soto", "Aaron Judge",
        "Giancarlo Stanton"
    ]

    for name in names:
        label = tk.Label(yankees_window, text=name, fg="white", cursor="hand2")
        label.bind("<Button-1>", lambda event, name=name: display_info(name))
        label.pack()

    yankees_window.mainloop()

def bluejays_hitters():
   bluejays_window = tk.Tk()
   bluejays_window.title("Toronto Blue Jays Hitters")


   names = [
       "Alejandro Kirk", "Vladimir Guerrero Jr.", "Cavan Biggio", "Isiah Kiner-Falefa",
       "Bo Bichette", "George Springer", "Kevin Kiermaier", "Daulton Varsho", "Justin Turner"
   ]


   for name in names:
       label = tk.Label(bluejays_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   bluejays_window.mainloop()

def rays_hitters():
   rays_window = tk.Tk()
   rays_window.title("Tampa Bay Rays Hitters")


   names = [
       "René Pinto", "Yandy Diaz", "Brandon Lowe", "Junior Caminero",
       "Taylor Walls", "Randy Arozarena", "Jose Siri", "Josh Lowe", "Harold Ramirez"
   ]


   for name in names:
       label = tk.Label(rays_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   rays_window.mainloop()

def redsox_hitters():
   redsox_window = tk.Tk()
   redsox_window.title("Boston Red Sox Hitters")


   names = [
       "Reese McGuire", "Triston Casas", "Emmanuel Valdez", "Rafael Devers", "Trevor Story", "Masataka Yoshida", 
       "Jarren Duran", "Tyler O’Neill", "Bobby Dalbec"
   ]


   for name in names:
       label = tk.Label(redsox_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   redsox_window.mainloop()

def whitesox_hitters():
   whitesox_window = tk.Tk()
   whitesox_window.title("Chicago White Sox Hitters")


   names = [
       "Martín Maldonado", "Andrew Vaughn", "Nicky Lopez", "Yoán Moncada", "Paul DeJong", "Andrew Benintendi", "Luis Robert Jr.", "Gavin Sheets", "Eloy Jiménez"
   ]


   for name in names:
       label = tk.Label(whitesox_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   whitesox_window.mainloop()

def indians_hitters():
   indians_window = tk.Tk()
   indians_window.title("Cleveland Indians Hitters")


   names = [
       "Austin Hedges", "Josh Naylor", "Andrés Giménez", "José Ramírez", "Juan Brito", "Steven Kwan", "Myles Straw", "Ramón Laureano", "Bo Naylor"
   ]


   for name in names:
       label = tk.Label(indians_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   indians_window.mainloop()

def tigers_hitters():
   tigers_window = tk.Tk()
   tigers_window.title("Detroit Tigers Hitters")


   names = [
       "Carson Kelly", "Spencer Torkelson", "Colt Keith", "Gio Urshela", "Javier Báez", "Akil Baddoo", "Riley Greene", "Matt Vierling", "Mark Canha"
   ]


   for name in names:
       label = tk.Label(tigers_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   tigers_window.mainloop()

def diamondbacks_hitters():
   diamondbacks_window = tk.Tk()
   diamondbacks_window.title("Arizona Diamondbacks Hitters")


   names = [
       "Gabriel Moreno", "Christian Walker",  "Ketel Marte", "Eugenio Suárez", "Geraldo Perdomo", "Lourdes Gurriel Jr.", "Alek Thomas", "Corbin Carroll", "Joc Pederson"
   ]


   for name in names:
       label = tk.Label(diamondbacks_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   diamondbacks_window.mainloop()

def braves_hitters():
   braves_window = tk.Tk()
   braves_window.title("Atlanta Braves Hitters")


   names = [
       "Sean Murphy", "Matt Olson",  "Ozzie Albies", "Austin Riley", "Orlando Arcia", "Jarred Kelenic", "Michael Harris II", "Ronald Acuña Jr.", "Marcell Ozuna"
   ]


   for name in names:
       label = tk.Label(braves_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   braves_window.mainloop()

def cubs_hitters():
   cubs_window = tk.Tk()
   cubs_window.title("Chicago Cubs Hitters")


   names = [
       "Yan Gomes", "Patrick Wisdom",  "Nick Madrigal", "Nico Hoerner", "Dansby Swanson", "Ian Happ", "Pete Crow-Armstrong", "Seiya Suzuki", "Cody Bellinger"
   ]


   for name in names:
       label = tk.Label(cubs_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   cubs_window.mainloop()

def reds_hitters():
   reds_window = tk.Tk()
   reds_window.title("Cincinnati Reds Hitters")


   names = [
       "Tyler Stephenson", "Christian Encarnacion-Strand",  "Johnathan India", "Elly de la Cruz", "Noelvi Marte", "Jake Fraley", "T.J. Friedl", "Will Benson", "Jeimer Candelario"
   ]


   for name in names:
       label = tk.Label(reds_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   reds_window.mainloop()

def rockies_hitters():
   rockies_window = tk.Tk()
   rockies_window.title("Colorado Rockies Hitters")


   names = [
       "Elias Diáz", "Michael Toglia",  "Brendan Rogers", "Ryan McMahon", "Ezequiel Tovar", "Kris Bryant", "Brenton Doyle", "Nolan Jones", "Charlie Blackmon"
   ]


   for name in names:
       label = tk.Label(rockies_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   rockies_window.mainloop()

def astros_hitters():
   astros_window = tk.Tk()
   astros_window.title("Houston Astros Hitters")


   names = [
       "Yanier Diaz", "José Abreu",  "Jose Altuve", "Alex Bregman", "Jeremy Peña", "Yordan Alvarez", "Chas McCormick", "Kyle Tucker", "Victor Caratini"
   ]


   for name in names:
       label = tk.Label(astros_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   astros_window.mainloop()

def royals_hitters():
   royals_window = tk.Tk()
   royals_window.title("Kansas City Royals Hitters")


   names = [
       "Salvador Perez", "Vinnie Pasquantino",  "Michael Massey", "Maikel Garcia", "Bobby Witt Jr.", "Kyle Isbel", "MJ Melendez", "Hunter Renfroe", "Adam Frazier"
   ]


   for name in names:
       label = tk.Label(royals_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   royals_window.mainloop()

def angels_hitters():
   angels_window = tk.Tk()
   angels_window.title("Los Angeles Angels Hitters")


   names = [
       "Logan O’Hoppe", "Nolan Schaunel",  "Luis Rengifo", "Anthony Rendon", "Zach Neto", "Jo Adell", "Mike Trout", "Mickey Moniak", "Brandon Drury"
   ]


   for name in names:
       label = tk.Label(angels_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   angels_window.mainloop()

def dodgers_hitters():
   dodgers_window = tk.Tk()
   dodgers_window.title("Los Angeles Dodgers Hitters")


   names = [
       "Will Smith", "Freddie Freeman",  "Enrique Hernández", "Max Muncy", "Gavin Lux", " Teoscar Hernandez", "James Outman", "Mookie Betts", "Shohei Ohtani"
   ]


   for name in names:
       label = tk.Label(dodgers_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   dodgers_window.mainloop()

def marlins_hitters():
   marlins_window = tk.Tk()
   marlins_window.title("Miami Marlins Hitters")


   names = [
       "Christian Bethancourt", "Josh Bell",  "Luis Arraez", "Jon Berti", "Tim Anderson", "Bryan de la Cruz", "Jazz Chisholm Jr.", "Jesús Sanchez", "Avisaíl García"
   ]


   for name in names:
       label = tk.Label(marlins_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   marlins_window.mainloop()

def brewers_hitters():
   brewers_window = tk.Tk()
   brewers_window.title("Milwaukee Brewers Hitters")


   names = [
       "William Contreras", "Rhys Hoskins",  "Brice Turang", "Owen Miller", "Willy Adames", "Christian Yelich", "Jackson Chourio", "Sal Frelick", "Gary Sánchez"
   ]


   for name in names:
       label = tk.Label(brewers_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   brewers_window.mainloop()

def twins_hitters():
   twins_window = tk.Tk()
   twins_window.title("Minnesota Twins Hitters")


   names = [
       "Christian Vázquez", "Carlos Santana",  "Royce Lewis", "Kyle Farmer", "Carlos Correa", "Alex Kirillof", "Manuel Margot", "Max Kepler", "Byron Buxton"
   ]


   for name in names:
       label = tk.Label(twins_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   twins_window.mainloop()

def mets_hitters():
   mets_window = tk.Tk()
   mets_window.title("New York Mets Hitters")


   names = [
       "Francisco Alvarez", "Pete Alonso",  "Jeff McNeil", "Brett Baty", "Francisco Lindor", "Starling Marte", "Harrison Bader", "Brandon Nimmo", "Joey Wendle"
   ]


   for name in names:
       label = tk.Label(mets_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   mets_window.mainloop()

def athletics_hitters():
   athletics_window = tk.Tk()
   athletics_window.title("Oakland Athletics Hitters")


   names = [
       "Shea Langeliers", "Ryan Noda",  "Abraham Toro", "Nick Allen", "Aledmys Díaz", "Miguel Andujar", "Esteury Ruiz", "JJ Bleday", "Brent Rooker"
   ]


   for name in names:
       label = tk.Label(athletics_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   athletics_window.mainloop()

def phillies_hitters():
   phillies_window = tk.Tk()
   phillies_window.title("Philadelphia Phillies Hitters")


   names = [
       "J.T. Realmuto", "Bryce Harper",  "Bryson Stott", "Alec Bohm", "Trea Turner", "Brandon Marsh", "Johan Rojas", "Nick Castellanos", "Kyle Schwarber"
   ]


   for name in names:
       label = tk.Label(phillies_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   phillies_window.mainloop()

def pirates_hitters():
   pirates_window = tk.Tk()
   pirates_window.title("Pittsburgh Pirates Hitters")


   names = [
       "Yasmani Grandal", "Rowdy Tellez",  "Ji Hwan Bae", "Ke’Bryan Hayes", "Oneil Cruz", "Connor Joe", "Bryan Reynolds", "Henry Davis", "Andrew McCutchen"
   ]


   for name in names:
       label = tk.Label(pirates_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   pirates_window.mainloop()

def padres_hitters():
   padres_window = tk.Tk()
   padres_window.title("San Diego Padres Hitters")


   names = [
       "Luis Campusano", "Jake Cronenworth",  "Ha-Seong Kim", "Manny Machado", "Xander Bogaerts", "Jurickson Profar", "José Azocar", "Fernando Tatis Jr.", "Tucupita Marcano"
   ]


   for name in names:
       label = tk.Label(padres_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   padres_window.mainloop()

def giants_hitters():
   giants_window = tk.Tk()
   giants_window.title("San Francisco Giants Hitters")


   names = [
       "Patrick Bailey", "Lamonte Wade Jr.",  "Thairo Estrada", "Wilmer Flores", "Marco Luciano", "Jung Hoo Lee", "Michael Conforto", "Mike Yastrzemski", "Jorge Soler"
   ]


   for name in names:
       label = tk.Label(giants_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   giants_window.mainloop()

def mariners_hitters():
   mariners_window = tk.Tk()
   mariners_window.title("Seattle Mariners Hitters")


   names = [
       "Cal Raleigh", "Ty France",  "Luis Urías", "Josh Rojas", "J.P. Crawford", "Dylan Moore", "Julio Rodríguez", "Mitch Haniger", "Luke Raley"
   ]


   for name in names:
       label = tk.Label(mariners_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   mariners_window.mainloop()

def cardinals_hitters():
   cardinals_window = tk.Tk()
   cardinals_window.title("St. Louis Cardinals Hitters")


   names = [
       "Wilson Contreras", "Paul Goldschmidt",  "Tommy Edman", "Nolan Arenado", "Brandon Crawford", "Dylan Carlson", "Jordan Walker", "Lars Nootbaar", "Matt Carpenter"
   ]


   for name in names:
       label = tk.Label(cardinals_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   cardinals_window.mainloop()

def rangers_hitters():
   rangers_window = tk.Tk()
   rangers_window.title("Texas Rangers Hitters")


   names = [
       "Jonah Heim", "Nathaniel Lowe",  "Marcus Semien", "Josh Jung", "Corey Seager", "Evan Carter", "Leody Taveras", "Adolis Garcia", "Sam Huff"
   ]


   for name in names:
       label = tk.Label(rangers_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   rangers_window.mainloop()

def nationals_hitters():
   nationals_window = tk.Tk()
   nationals_window.title("Washington Nationals Hitters")


   names = [
       "Keibert Ruiz", "Ildemaro Vargas",  "Luis García Jr.", "Nick Senzel", "CJ Abrams", "Lane Thomas", "Victor Robles", "Joey Gallo", "Joey Meneses"
   ]


   for name in names:
       label = tk.Label(nationals_window, text=name, fg="white", cursor="hand2")
       label.bind("<Button-1>", lambda event, name=name: display_info(name))
       label.pack()


   nationals_window.mainloop()

welcome()


# This project was completed with the assistance of my peer Branson Bailey (sharing code ideas), search engines and AI (seeing what types of code might run correctly), and Dr. Brandon Grech (assistance in troubleshooting). 
# I give myself credit for this project
