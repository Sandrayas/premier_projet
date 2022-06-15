#fonction qui compte le nombre de parametres 
def count_char(password):
    i = 0 
    for letter in password: 
        i = i+1 #i+=1
    return i 

#verifier s il y a une majuscule dans un mot de passe 
def check_if_maj(password):
    upper = False 
    for letter in password: 
        if letter.isupper():
            upper = True 
    return upper 

#regarder s il y a des caracteres speciaux 
def check_if_special(password):
    result = False
    special = ['!', '*', '-']
    for letter in password: 
        if letter in special: 
            result = True
    return result 
#les tests unitaires portent sur les fonctions du haut 


def check_if_valid_password(password):
    password_len = 10
    if count_char(password) < password_len:
        return False 
    if check_if_special(password) == False:
        return False 
    return True #ie mdp valide 

result = check_if_valid_password("Bonjour")
if result == True:
    print("password is valid")
else : 
    print("password is not valid")