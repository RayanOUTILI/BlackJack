import random
import time
def scoreC(carte) :
    if carte=='0' :
        return int(0)
    elif carte=='AS' :
        return int(11)
    elif carte=='1':
        return int(1)
    elif carte=='2':
        return int(2)
    elif carte=='3':
        return int(3)
    elif carte=='4':
        return int(4)
    elif carte=='5':
        return int(5)
    elif carte=='6':
        return int(6)
    elif carte=='7':
        return int(7)
    elif carte=='8':
        return int(8)
    elif carte=='9':
        return int(9)
    else:
        return int(10)

def score(carte) :
    if carte=='0' :
        return int(0)
    elif carte=='AS' :
        AS=input("Quelle valeur souhaitez-vous attribuer à votre AS: 1 ou 11?")
        if AS=='1' :
            return int(1)
        else :
            return int(11)
    elif carte=='1':
        return int(1)
    elif carte=='2':
        return int(2)
    elif carte=='3':
        return int(3)
    elif carte=='4':
        return int(4)
    elif carte=='5':
        return int(5)
    elif carte=='6':
        return int(6)
    elif carte=='7':
        return int(7)
    elif carte=='8':
        return int(8)
    elif carte=='9':
        return int(9)
    else:
        return int(10)

def BlackJack():
    jouer=True
    carte = [ 'AS', '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' ,'Valet','Dame','Roi']
    rejouer=True
    print("Bienvenue dans le jeu du BlackJack")
    règles=input("Connaissez vous les règles du jeu ?")
    if règles=="oui" or règles=="Oui":
        print("Très bien.")
    else:
        for i in range(10):
            print(" ")
        print("Voici les règles du jeu:")
        time.sleep(1)
        print(" ")
        print("Après avoir reçu deux cartes, le joueur tire des cartes pour s’approcher de la valeur 21 sans la dépasser.")
        time.sleep(5)
        print(" ")
        print("Le but du joueur est de battre le croupier en obtenant un total de points supérieur à celui-ci ou en voyant ce dernier dépasser 21.")
        time.sleep(5)
        print(" ")
        print("Le Croupier tirera une carte tant qu'il aura un score inférieur ou égal à 16.")
        time.sleep(5)
        print(" ")
        print("Chaque carte numérotée de 2 à 10 a sa valeur nominale,les figures ont une valeur de 10 points tandis que l'as vaut 1 point ou 11 points, selon le choix du joueur")
        time.sleep(5)
        print(" ")
        print("A chaque partie vous débutez avec 1000 euros, faites en bon usage et surtout ne doubler pas de l'argent que vous ne possédez pas !")
        time.sleep(5)
        print("")
    argent=1000
    while jouer:
        print("La distribution des cartes va commencer.")
        time.sleep(2)
        print(" ")
        print("Vous avez",argent,"euros")
        mise = int(input("Combien souhaitez-vous miser? "))
        if mise>argent:
            mise=argent
            argent-=mise
            print("Vous n'avez pas assez d'argent vous parirez donc",mise)
        else:
            print("D'accord, vous jouez",mise)
        print()
        jouer1=True
        Crcarte1=random.choice(carte)
        if Crcarte1=="Dame":
            print("La 1ère carte du croupier est une",Crcarte1)
        else:
            print("La 1ère carte du croupier est un",Crcarte1)
        Crcarte2 =random.choice(carte)
        if Crcarte2=="Dame":
            print("La 2ème carte du croupier est une",Crcarte2)
        else:
            print("La 2ème carte du croupier est un",Crcarte2)
        Cpoints=[]
        Cpoints=scoreC(Crcarte1) + scoreC(Crcarte2)
        time.sleep(1)
        print("")
        print("Le Croupier a donc",Cpoints)
        print()
        time.sleep(2)
        if Cpoints == 21 :
            print()
            print('Blackjack!, ce fut rapide, mais le Croupier gagne !')
            jouer1=False
            rejouer=False
        elif Cpoints > 21 :
            print()
            print("Pas de chance,c'est perdu !")
            jouer1=False
            rejouer=False
        while jouer1:
            Jcarte1=random.choice(carte)
            if Jcarte1=="Dame":
                print("La 1ère carte du joueur est une",Jcarte1)
            else:
                print("La 1ère carte du joueur est un",Jcarte1)
            Jcarte2 =random.choice(carte)
            if Jcarte2=="Dame":
                print("La 2ème carte du joueur est une",Jcarte2)
            else:
                print("La 2ème carte du joueur est un",Jcarte2)
            Jpoints=score(Jcarte1) + score(Jcarte2)
            time.sleep(1)
            print("")
            print("Vous avez donc",Jpoints,"et le croupier",Cpoints)
            time.sleep(1)
            jouer1=False
            if Jpoints == 21 :
                print()
                print('Blackjack!, ce fut rapide, mais vous avez gagné !')
                rejouer=False
                jouer1=False
            elif Jpoints > 21 :
                print()
                print("Malheureusement, le croupier gagne !")
                rejouer=False
                jouer1=False
        jouer=False
        print()
        while rejouer:
            tirercarte=input("Tirer,garder,doubler?")
            compte=2
            compte+=1
            print()
            tirerinput=["tirer","Tirer"]
            if tirercarte in tirerinput:
                Jcarte3=random.choice(carte)
                print("Votre",compte,"ème carte :",Jcarte3)
                Jpoints += score(Jcarte3)
                print("Voici votre nouveau score:",Jpoints)
                time.sleep(2)
                if Jpoints > 21 :
                    print('Vous avez dépassé 21, vous avez perdu..')
                    print("Le croupier gagne", mise, "euros")
                    argent-=mise
                    rejouer=False
            elif tirercarte == "garder" or tirercarte =="Garder" :
                print("D'accord votre score ne change pas: ",Jpoints)
                print()
                time.sleep(2)
                if Cpoints < Jpoints:
                    while Cpoints <= 16:
                        Crcarte3 = random.choice(carte)
                        print("Le croupier tire une nouvelle carte :",Crcarte3)
                        Cpoints += scoreC(Crcarte3)
                        print("Croupier, voici le nouveau score :" ,Cpoints)
                        print()
                        rejouer=False
                        time.sleep(2)
                        if Cpoints > 21:
                            print("Le croupier a dépassé 21.")
                            print("Vous gagnez, voici votre mise:",mise)
                            argent+=mise
                        elif Jpoints < Cpoints:
                            print()
                            print("Le Croupier a",Cpoints, "et vous",Jpoints)
                            print("Le Croupier a donc gagné",mise)
                            argent-=mise
                    # if Jpoints ==  Cpoints :
                    #     print()
                    #     print("Il n'y a aucun gagnant")
                    if Jpoints > Cpoints:
                        print()
                        print("Vous avec",Jpoints," alors que le croupier a", Cpoints)
                        print("Vous gagnez, voici votre mise:",mise)
                        argent+=mise
                        break
                        rejouer=False
                else:
                    print("Il n'y a aucun gagnant")
                    break
                    rejouer=False
            elif tirercarte == "doubler" or tirercarte =="Doubler" :
                Jcarte3 = random.choice(carte)
                if Jcarte3=="Dame":
                    print("Votre carte est une",Jcarte2)
                else:
                    print("Votre carte est un",Jcarte2)
                mise = mise*2
                Jpoints += score(Jcarte3)
                print()
                print("Voici votre nouveau score:",Jpoints)
                time.sleep(2)
                if Jpoints > 21 :
                    print('Vous avez dépassé 21, vous avez perdu..')
                    print("Le croupier gagne",mise, "euros")
                    argent-=mise
                    rejouer=False
                    break
                elif Cpoints <= 16:
                    Crcarte3 = random.choice(carte)
                    print("Le croupier tire une nouvelle carte :",Crcarte3)
                    Cpoints += scoreC(Crcarte3)
                    print()
                    print("Croupier, voici le nouveau score :" ,Cpoints)
                    print()
                    rejouer=False
                elif Cpoints > 21:
                    print('Le croupier a perdu,vous avez donc gagné !')
                    print("Voici votre mise",mise)
                    argent+=mise
                    rejouer=False
                elif Cpoints == 21 :
                            print()
                            print('Blackjack!, Le Croupier gagne !')
                            print("Le croupier gagne",mise, "euros")
                            argent-=mise
                            rejouer=False
                            break
                elif Jpoints ==  Cpoints :
                    print()
                    print("Il n'y a aucun gagnant")
                    rejouer=False
                elif Jpoints < 21 and Cpoints < 21:
                    if Cpoints <= 16:
                        Crcarte3 = random.choice(carte)
                        print("Le croupier tire une nouvelle carte :",Crcarte3)
                        Cpoints += score(Crcarte3)
                        print("Croupier, voici le nouveau score :",Cpoints)
                        print()
                        rejouer=False
                    elif Jpoints < Cpoints:
                        print()
                        print("Le croupier a",Cpoints, "et vous",Jpoints)
                        print("Le croupier a donc gagné!")
                        argent-=mise
                        rejouer=False
                    elif Jpoints > Cpoints:
                        print()
                        print("Vous avec",Jpoints," alors que le croupier a", Cpoints)
                        print("Vous gagnez, voici votre mise",mise)
                        argent=mise+argent
                        rejouer=False
        if argent<=0:
            print("Vous n'avez plus d'argent,vous avez perdu la partie")
            jouer=False
            break
        rejouer=input("Souhaitez-vous rejouer")
        print("")
        if rejouer=="Non" or rejouer=="non":
            jouer=False
        else:
            jouer=True