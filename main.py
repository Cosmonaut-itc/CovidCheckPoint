import names
import random

class Player:
    health = 3
    def __init__(self, points):
        self.points = points
    def health_r():
        health = health - 1
    def points_change(add_or_sub, streak):
        if add_or_sub == "add":
            self.points = (self.points + 100) * streak
        else
            self.points = self.points - 100

class Credential:
    def __init__(self, name, status, area, clearance):
        self.name = name
        self.status = status
        self.area = area
        self.clearance = clearance
    def __str__(self):
        return f"name: {self.name}\nstatus: {self.status}\narea: {self.area}\nclearance: {self.clearance}"

class COVID:
    def __init__(self, last_check,mask):
        self.last_check = last_check
        self.mask = mask
    def __str__(self):
        return f"Last Coronavirus Checkout: {self.last_check}\nWearing Mask: {self.mask}"

def assignCredential():
    number = random.randint(0,1)
    if number == 0:
        worker = "Fired"
    else:
        worker = "Worker"
    number = random.randint(0,4)
    areas = ["Information Technology", "Admin", "Human Resources", "Accountancy", "Manofacture"]
    clearance_number = random.randint(0,3)
    return Credential(names.get_full_name(),worker,areas[number], clearance_number)

def assignCovid():
    last_check = random.randint(1, 30)
    number = random.randint(0, 1)
    if number == 0:
        mask = "No"
    else:
        mask = "Yes"
    return COVID(last_check ,mask)

def access(status, clearance, last_check, mask):
    if status == "Worker" and clearance != 0 and mask == true:
        last_check = last_check - 18
        if last_check > 0:
            last_check = last_check * 5
            random_number = random.randint(0, 100)
            if (random_number <= last_check):
                return False
            else
                return True
        else
            return True
    else
        return False




while True:
    print('''
                                                                                                                                                                                ,----, 
               ,----..                                                               ,--,                            ,--.,-.----.       ,----..                    ,--.      ,/   .`| 
  ,----..     /   /   \                 ,---,    ,---,              ,----..        ,--.'|    ,---,.  ,----..     ,--/  /|\    /  \     /   /   \     ,---,       ,--.'|    ,`   .'  : 
 /   /   \   /   .     :        ,---.,`--.' |  .'  .' `\           /   /   \    ,--,  | :  ,'  .' | /   /   \ ,---,': / '|   :    \   /   .     : ,`--.' |   ,--,:  : |  ;    ;     / 
|   :     : .   /   ;.  \      /__./||   :  :,---.'     \         |   :     :,---.'|  : ',---.'   ||   :     ::   : '/ / |   |  .\ : .   /   ;.  \|   :  :,`--.'`|  ' :.'___,/    ,'  
.   |  ;. /.   ;   /  ` ; ,---.;  ; |:   |  '|   |  .`\  |        .   |  ;. /|   | : _' ||   |   .'.   |  ;. /|   '   ,  .   :  |: |.   ;   /  ` ;:   |  '|   :  :  | ||    :     |   
.   ; /--` ;   |  ; \ ; |/___/ \  | ||   :  |:   : |  '  |        .   ; /--` :   : |.'  |:   :  |-,.   ; /--` '   |  /   |   |   \ :;   |  ; \ ; ||   :  |:   |   \ | :;    |.';  ;   
;   | ;    |   :  | ; | '\   ;  \ ' |'   '  ;|   ' '  ;  :        ;   | ;    |   ' '  ; ::   |  ;/|;   | ;    |   ;  ;   |   : .   /|   :  | ; | ''   '  ;|   : '  '; |`----'  |  |   
|   : |    .   |  ' ' ' : \   \  \: ||   |  |'   | ;  .  |        |   : |    '   |  .'. ||   :   .'|   : |    :   '   \  ;   | |`-' .   |  ' ' ' :|   |  |'   ' ;.    ;    '   :  ;   
.   | '___ '   ;  \; /  |  ;   \  ' .'   :  ;|   | :  |  '        .   | '___ |   | :  | '|   |  |-,.   | '___ |   |    ' |   | ;    '   ;  \; /  |'   :  ;|   | | \   |    |   |  '   
'   ; : .'| \   \  ',  /    \   \   '|   |  ''   : | /  ;         '   ; : .'|'   : |  : ;'   :  ;/|'   ; : .'|'   : |.  \:   ' |     \   \  ',  / |   |  ''   : |  ; .'    '   :  |   
'   | '/  :  ;   :    /      \   `  ;'   :  ||   | '` ,/          '   | '/  :|   | '  ,/ |   |    \'   | '/  :|   | '_\.':   : :      ;   :    /  '   :  ||   | '`--'      ;   |.'    
|   :    /    \   \ .'        :   \ |;   |.' ;   :  .'            |   :    / ;   : ;--'  |   :   .'|   :    / '   : |    |   | :       \   \ .'   ;   |.' '   : |          '---'      
 \   \ .'      `---`           '---" '---'   |   ,.'               \   \ .'  |   ,/      |   | ,'   \   \ .'  ;   |,'    `---'.|        `---`     '---'   ;   |.'                     
  `---`                                      '---'                  `---`    '---'       `----'      `---`    '---'        `---`                          '---' 
  ''')
    print('''
    __     _____       _      _            
 /_ |   |_   _|     (_)    (_)           
  | |     | |  _ __  _  ___ _  __ _ _ __ 
  | |     | | | '_ \| |/ __| |/ _` | '__|                               
  | |_   _| |_| | | | | (__| | (_| | |                 
  |_(_) |_____|_| |_|_|\___|_|\__,_|_|   


  
  ___       _____       _ _      
 |__ \     / ____|     | (_)     
    ) |   | (___   __ _| |_ _ __ 
   / /     \___ \ / _` | | | '__|1
  / /_ _   ____) | (_| | | | |   
 |____(_) |_____/ \__,_|_|_|_|   
                                 
                        
    ''')
    user_input = int(input("Select an option: "))
    print ("\n")
    if user_input == 1:
        for i in range(0,3):
            print("Day " + str(i+1))
            streak = 1
            if i == 0:
                for i in range(0, 3):
                    person_credential = assignCredential()
                    person_covid = assignCovid()
                    print(person_credential)
                    print(person_covid)
                    print("\n")
                    user_answer = input("Give access to the person? (Y)es, (N)o\n")
                    while True:
                        if user_answer == "Y":
                            access_answer = access(person_credential.status, person_credential.clearance, person_covid.last_check, person_covid.mask)
                            if access_answer == False:
                                #quitar vida y quitar racha de puntos
                                streak = 1
                            else:
                                #Subir puntos y aumentar racha de puntos
                                pass
                            break
                        elif user_answer == "N":
                            access_answer = access(person_credential.status, person_credential.clearance, person_covid.last_check, person_covid.mask)
                            if access_answer == True:
                                #quitar vida y quitar racha de puntos
                                streak = 1
                            else:
                                #Subir puntos y aumentar racha de puntos 
                                pass
                            break
                        else:
                            print("Invalid character, try again!\n")

                    print("\n")
            elif i == 1:
                for i in range(0, 4):
                    pass
            elif i == 2:
                for i in range(0, 5):
                    pass
    else:
        break



