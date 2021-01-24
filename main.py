import names
import random

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
        worker = "No worker"
    else:
        worker = "Worker"
    number = random.randint(0,4)
    areas = ["Information Technology", "Admin", "Human Resources", "Accountancy", "Manofacture"]
    number = random.randint(0,1)
    if number == 0:
        bool_clearance = False
    else:
        bool_clearance = True
    return Credential(names.get_full_name(),worker,areas[number], bool_clearance)

def assignCovid():
    last_check = random.randint(1, 31)
    number = random.randint(0, 1)
    if number == 0:
        mask = "No"
    else:
        mask = "Yes"
    return COVID(last_check ,mask)

def access():



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
            print("Dia " + str(i+1))
            if i == 0:
                for i in range(0, 3):
                    person = assignCredential()
                    print(person)
                    user_answer = input("Give access to the person? (Y)es, (N)o\n")
                    if user_answer == "Y":
                        
                    else:

                    print("\n")
            elif i == 1:
                for i in range(0, 4):
                    pass
            elif i == 2:
                for i in range(0, 5):
                    pass
    else:
        break



