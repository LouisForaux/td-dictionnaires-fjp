from random import randint
helmut = {'nom':'Helmut','vie':100,'force':6,'adresse':75,'nb_coups':3,'armure':30}
olga = {'nom':'Olga','vie':98,'force':8,'adresse':90,'nb_coups':2,'armure':35}
irina = {'nom':'Irina','vie':100,'force':2,'adresse':55,'nb_coups':2,'armure':20}
boris = {'nom':'Boris','vie':100,'force':3,'adresse':30,'nb_coups':3,'armure':15}

def est_vivant(user):
    get=user
    if get['vie']>0:
        return True
    else :
        return False

def donne_un_coup(user):
    if est_vivant(user)==False:
        return 0
    reussi=randint(0,100)
    if reussi<=user['adresse']:
        return user['force']
    else :
        return 0
def prend_un_coup(user,force):
    get=user
    value=force*(get['armure']/100)
    if get['vie']-force-value>=0:
        get['vie']-=round(force-value)
    else:
        get['vie']=0
def attaque(user1,user2):
    for i in range(user1['nb_coups']):
        prend_un_coup(user2,donne_un_coup(user1))
    if user2['vie']!=0:
        prend_un_coup(user1,donne_un_coup(user2))


equipe_1=[helmut,olga]
equipe_2=[irina,boris]

def calc_moy_trait(equipe,trait):
    value=0
    for i in range(len(equipe)):
        value+=equipe[i][trait]
    return (value)/(len(equipe))

def les_plus(equipe,trait):
    for i in range(1,len(equipe)):
        if equipe[i][trait]>equipe[i-1][trait]:
            win=equipe[i]['nom']
        else :
            win=equipe[i-1]['nom']
    return win

#Def Bataille



def nettoie(equipe):
    for i in range(len(equipe)):
        if equipe[i]['vie']<=0:
            del equipe[i]
def repose(equipe):
    for i in range(len(equipe)):
        if equipe[i]['vie']<100:
            equipe[i]['vie']+=2