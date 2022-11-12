#!/usr/bin/python3

import random
import pdb
import time

import tkinter as tk

from PIL import ImageTk, Image
import threading


def MiseWindow(joueur,chiffre,couleur):
    newWindow = tk.Toplevel(root)
    newWindow.geometry("500x300")
    textvar = joueur + " " + str(chiffre) + "  " + str(couleur)
    l = tk.Label(newWindow, text = textvar)
    l.config(font =("Courier", 20))
    l.place(x=100,y=100)
    buttonOK = tk.Button(newWindow, text="OK")
    buttonOK.place(x=200, y=250)
    buttonOK.config(
        width=10,
        height = 2,
        text = 'OK',
        command = lambda: newWindow.destroy()
    )
    return newWindow

def Score(gagner,score,mise):
    newWindow = tk.Toplevel(root)
    newWindow.geometry("500x300")
    if gagner == 0:
        text_script = str(score) + "/" + str(mise) + "\n Contrat Echoué"
    else:
        text_script = str(score) + "/" + str(mise) + "\n Contrat Réussit"

    l = tk.Label(newWindow, text = text_script)
    l.config(font =("Courier", 20))
    l.place(x=100,y=100)
    buttonOK = tk.Button(newWindow, text="OK")
    buttonOK.place(x=200, y=250)
    buttonOK.config(
        width=10,
        height = 2,
        text = 'OK',
        command = lambda: newWindow.destroy()
    )
    TKV_Modifier2 = tk.StringVar (master= newWindow ,value='rr')
    return newWindow


class ClassToStoreReturnedVariable:
    def __init__(self):
        self.returned_variable = 0

    def return_variable(self, xxz):
        self.returned_variable = xxz



class ajoutBouton:
    WIDTH = 100
    HEIGHT = 190

    def __init__(self,ImageNom, x_pos, y_pos):
        self.nom = ImageNom
        ImageNom = "images/" + ImageNom + ".png"
        image = Image.open(ImageNom)
        image = image.resize((self.WIDTH, self.HEIGHT), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        image.close()



        self.bouton = tk.Button(root, text = self.nom , command = lambda: self.JouerCarte(self.nom) )
        self.bouton.config(image=self.photo, width=self.WIDTH, height=self.HEIGHT)
        self.bouton.place(x=x_pos, y=y_pos)


    def JouerCarte(self,nom):
        TKV_Modifier.set(nom)
        self.bouton.destroy()


class ajoutImage:
    WIDTH = 150
    HEIGHT = 150

    WIDTH_png = 100
    HEIGHT_png = 190

    def __init__(self,  ImageNom, x_pos, y_pos, anglerotation):
        ImageNom = "images/" + ImageNom
        self.path = ImageNom
        self.image = Image.open(ImageNom)
        self.image = self.image.rotate(anglerotation)
        if ImageNom[-3:] == "png":
            self.image = self.image.resize((self.WIDTH_png, self.HEIGHT_png), Image.ANTIALIAS)
        elif ImageNom[-4:] == 'JPEG':
            self.image = self.image.resize((self.WIDTH, self.HEIGHT), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(self.image)

        self.bouton = tk.Label(root,  compound='center', image=self.photo  )
        self.bouton.place(x=x_pos, y=y_pos)

    def __del__(self):
        pass
    #    print('Destructor called, Employee deleted.')


    def detruire(self):
        self.bouton.destroy()



####################################################
class Listejoueur:
    def __init__(self, J0, J1, J2, J3):
        self.listejoueur = [J0, J1, J2, J3]

class joueur:
    def __init__(self, ijoueur):
        # pdb.set_trace
        self.nom = "J" + str(ijoueur)
        coep = ijoueur + 2
        if coep > 3:
            coep -= 4
        self.coequipier = "J" + str(coep)
        self.cartes = []
        self.score = 0
        self.point = 0


class ListeCarte:

    LISTE_CATRE = []

    def __init__(self, valeur, couleur, point, ordre, nom):
        self.valeur = valeur
        self.couleur = couleur
        self.point = point
        self.ordre = ordre
        self.nom = nom

    @classmethod
    def creerCarte(clc):
        for iCouleur in ["Co", "Ca", "Pi", "Tr"]:
            for iValeur in range(6, 14):
                couleur = iCouleur
                if iValeur == 6:
                    valeur = "A"
                    point = 11
                    ordre = 8
                elif iValeur == 11:
                    valeur = "J"
                    point = 2
                    ordre = 4
                elif iValeur == 12:
                    valeur = "Q"
                    point = 3
                    ordre = 5
                elif iValeur == 13:
                    valeur = "K"
                    point = 4
                    ordre = 6
                else:
                    valeur = str(iValeur)
                    if (iValeur == 7) or (iValeur == 8) or (iValeur == 9):
                        point = 0
                        ordre = iValeur - 6
                    elif iValeur == 10:
                        point = 10
                        ordre = 7
                nomCarte = valeur + "_" + couleur
                nvCarte = ListeCarte(valeur, couleur, point, ordre, nomCarte)
                clc.LISTE_CATRE.append(nvCarte)

    def longueur(self):
        return len(self.LISTE_CATRE)


#############################################

#############################################
#############################################
class Parti:
    def __init__(self, liste_carte, joueur_0, joueur_1, joueur_2, joueur_3):
        self.listeCarte = liste_carte
        self.listejoueur = [joueur_0, joueur_1, joueur_2, joueur_3]


    def jouer(self, premierjoueur, atout):

        cate_J0_p = ajoutImage(
            'Q_Co' + ".png", 10, 10, 0
        )

        cate_J1_p = ajoutImage(
            'Q_Co' + ".png", 90, 10, 0
        )

        cate_J2_p = ajoutImage(
            'Q_Co' + ".png", 170, 10, 0
        )

        cate_J3_p = ajoutImage(
            'Q_Co' + ".png", 250, 10, 0
        )


        cate_J0_p.bouton.config(image='', compound='top', text = 'J0',font=("Arial", 20, "bold"))
        cate_J1_p.bouton.config(image='', compound='top', text = 'J1',font=("Arial", 20, "bold"))
        cate_J2_p.bouton.config(image='', compound='top', text = 'J2',font=("Arial", 20, "bold"))
        cate_J3_p.bouton.config(image='', compound='top', text = 'J3',font=("Arial", 20, "bold"))







        for ijoueur in self.listejoueur:
            if ijoueur == J0:


                listeCarte = [ajoutBouton(ijoueur.cartes[i_carte].nom, xpos, 550) for i_carte,xpos in zip(range(8),range(200,1200,125))]

                for i_carte in listeCarte:
                    i_carte.bouton.config(state="disabled")



            #    bt1.bouton.config(state="normal")
            #    bt1.bouton.config(state="disabled")



                for i_tour in range(8):
                    print('tour ',i_tour + 1)

                    plis = []

                    if i_tour == 7:
                        point_plis = 10
                    else:
                        point_plis = 0

                    temp_tot = 0
                    temp_anim = 3000

                    root.update()




                    for ijoueur in self.listejoueur:

                        carte_jouable = self.listecarte_jouable(ijoueur, plis, atout)
                        random.shuffle(carte_jouable)
                        Cartejouee = carte_jouable[0]

                        if ijoueur == J0:

                            carte_jouable_nom = [i_carte.nom for i_carte in carte_jouable]
                            carte_main = [listeCarte[i_carte].nom for i_carte in  range(len(listeCarte))]

                            for i_carte in carte_main:
                                if i_carte in carte_jouable_nom:
                                    indice = carte_main.index(i_carte)
                                    listeCarte[indice].bouton.config(state="normal")





                            carte_choisi,carte_jouer_J0 = self.CarteJouerJoueur()
                            root.update()
                            temp_tot = 0
                            print('la carte jouer est : ',carte_choisi)





                            if carte_choisi in carte_jouable_nom:

                                indice = carte_jouable_nom.index(carte_choisi)
                                Cartejouee =  carte_jouable[indice]

                                indice = carte_main.index(carte_choisi)
                                listeCarte.pop(indice)
                                for i_carte in listeCarte:
                                    i_carte.bouton.config(state="disabled")
                                print(len(listeCarte))





                            else:
                                print('MAUVAISE CARTE')

                        else:
                            if ijoueur == J1:
                                x_pos = 200
                                y_pos = 300
                                Obj_Xpos = 530
                                Obj_Ypos = 300
                                carte_jouer_ordi_j1 = ajoutImage(
                                    Cartejouee.nom + ".png", x_pos, y_pos, 0
                                )
                                self.animation(ijoueur,
                                carte_jouer_ordi_j1,
                                x_pos,
                                y_pos,
                                Obj_Xpos,
                                Obj_Ypos
                                )
                                temp_tot += temp_anim

                            elif ijoueur == J2:
                                x_pos = 637.5
                                y_pos = 0
                                Obj_Xpos = 637.5
                                Obj_Ypos = 150

                                carte_jouer_ordi_j2 = ajoutImage(
                                    Cartejouee.nom + ".png", x_pos , y_pos, 0
                                )

                                self.animation(ijoueur,
                                carte_jouer_ordi_j2,
                                x_pos,
                                y_pos,
                                Obj_Xpos,
                                Obj_Ypos,
                                )
                                root.update()
                                temp_tot += temp_anim

                            elif ijoueur == J3:
                                x_pos = 1000
                                y_pos = 300
                                Obj_Xpos = 750
                                Obj_Ypos = 300
                                carte_jouer_ordi_j3 = ajoutImage(
                                    Cartejouee.nom + ".png", x_pos, y_pos, 0
                                )

                                self.animation(ijoueur,
                                carte_jouer_ordi_j3,
                                x_pos,
                                y_pos,
                                Obj_Xpos,
                                Obj_Ypos
                            )

                                temp_tot += temp_anim


                        point_plis += Cartejouee.point
                        ijoueur.cartes.remove(Cartejouee)

                        if plis == []:
                            couleur_plis = Cartejouee.couleur
                            main_gagnante = True
                        else:
                            main_gagnante = self.testMainGagnante(Cartejouee, plis, atout)

                        if main_gagnante == True:
                            CarteMaitre = Cartejouee
                            plis = [ijoueur, couleur_plis, CarteMaitre]
                        print(ijoueur.nom, Cartejouee.valeur, Cartejouee.couleur)

                    if (plis[0].nom == "J0") or (plis[0].nom == "J2"):
                        J0.point += point_plis
                        J2.point += point_plis
                    else:
                        J1.point += point_plis
                        J3.point += point_plis

                    self.defListeJoueur(plis[0])

                    #carte_jouer_ordi_j2.bouton.descarte_jouer_ordi_j3troy()
                    #carte_jouer_ordi_j3.bouton.destroy()
                    time.sleep(1)
                    print('tt')
                    self.supprimerCate(carte_jouer_ordi_j3,cate_J3_p)
                    self.supprimerCate(carte_jouer_ordi_j2,cate_J2_p)
                    self.supprimerCate(carte_jouer_ordi_j1,cate_J1_p)
                    self.supprimerCate(carte_jouer_J0,cate_J0_p)




                    root.update()



                    print('fin tour---', plis[0].nom, '----',point_plis , ' Pts')

    def attributionScore(self, Mise, JoeurMisant, joueur_0, joueur_1, joueur_2, joueur_3):

        if JoeurMisant.point >= Mise:
            if (JoeurMisant == joueur_0) or  (JoeurMisant == joueur_2):
                joueur_0.score += Mise
                joueur_2.score += Mise
            else:
                joueur_1.score += Mise
                joueur_2.score += Mise
        else:
            if (JoeurMisant == joueur_1) or (JoeurMisant == joueur_3):
                joueur_0.score += Mise
                joueur_2.score += Mise
            else:
                joueur_1.score += Mise
                joueur_2.score += Mise

        for ijoueur in self.listejoueur:
            ijoueur.point = 0

        return joueur_0, joueur_1, joueur_2, joueur_3


    def supprimerCate(self,carte,carte_p):

        img2 = ImageTk.PhotoImage(Image.open(carte.path))
        carte_p.path = carte.path
        carte_p.image = Image.open(carte.path)
        carte_p.image = carte_p.image.resize((70, 133), Image.ANTIALIAS)
        carte_p.photo = ImageTk.PhotoImage(carte_p.image)


        carte_p.bouton.config(image= carte_p.photo  )

        root.after(10,carte.bouton.config(image=''))



    def testMainGagnante(self, Cartejouee, plis, atout):
        if Cartejouee.couleur == atout:
            if plis[2].couleur == atout:
                if Cartejouee.ordre > plis[2].ordre:
                    main_gagnante = True
                else:
                    main_gagnante = False
            else:
                main_gagnante = True
        elif plis[2].couleur == atout:
            main_gagnante = False
        elif plis[2].couleur == Cartejouee.couleur:
            if Cartejouee.ordre > plis[2].ordre:
                main_gagnante = True
            else:
                main_gagnante = False
        else:
            main_gagnante = False
        return main_gagnante


    def CarteJouerJoueur ( self) :
        root.wait_variable ( TKV_Modifier )
        carte_choisi=TKV_Modifier.get()
        carte_choisi_im = ajoutImage(
            carte_choisi + ".png", 637.5, 350, 0)
        return(carte_choisi, carte_choisi_im)

    def animation ( self, ijoueur,  carteJouerOrdi, x_pos, y_pos, Obj_Xpos, Obj_Ypos):

        pasX = 10
        dx = x_pos + pasX
        #carteJouerOrdi.bouton.pack()
        carteJouerOrdi.bouton.place(x=x_pos, y=y_pos)
        div = 20
        tt = 30

        if x_pos < Obj_Xpos and ijoueur == J1:

            for compt in range(div):
                if compt == 0:
                    pasX = (Obj_Xpos - x_pos)/div
                x_pos += pasX
                root.after(tt,carteJouerOrdi.bouton.place(x=x_pos, y=y_pos))
                root.update()
                tt+=1

        elif x_pos > Obj_Xpos and ijoueur == J3:

            for compt in range(div):
                if compt == 0:
                    pasX = (Obj_Xpos - x_pos)/div
                x_pos += pasX
                root.after(tt,carteJouerOrdi.bouton.place(x=x_pos, y=y_pos))
                root.update()
                tt+=1

        elif y_pos < Obj_Ypos and ijoueur == J2:

            for compt in range(div):
                if compt == 0:
                    pasX = (Obj_Ypos - y_pos)/div

                y_pos += pasX


                root.after(tt,carteJouerOrdi.bouton.place(x=x_pos, y=y_pos))
                root.update()

                tt+=1
        else :
            print('TT2')
            #root.after(1000,carteJouerOrdi.bouton.config(image=''))






    def defListeJoueur(self, premierjoueur):

        ordrejoueur = self.listejoueur
        pos = ordrejoueur.index(premierjoueur)
        toto = [ordrejoueur[pos]] + ordrejoueur[(pos + 1) :] + ordrejoueur[:(pos)]
        self.listejoueur = toto

    def distribuer(self, premierjoueur):
        random.shuffle(self.listeCarte)
        mains = []
        for i_tour in range(3):
            for ijoueur in self.listejoueur:
                if i_tour == 1:
                    nbcarte = 2
                else:
                    nbcarte = 3
                for ii in range(nbcarte):
                    adistribuer = self.listeCarte.pop(0)

                    ijoueur.cartes.append(adistribuer)
                #                    ijoueur.cartes.append(self.listeCarte.pop(0))
                ijoueur = self.trierCarte(ijoueur)

        return (J0, J1, J2, J3)

    def trierCarte(self, ijoueur):
        cartesvaleurs = []
        cartes_tier_valeur = []
        cartesTier = [[], [], [], []]

        for i_carte in ijoueur.cartes:
            cartesvaleurs.append(i_carte.ordre)

        for i_carte in ijoueur.cartes:
            posMin = cartesvaleurs.index(min(cartesvaleurs))
            cartesvaleurs[posMin] = 99
            cartes_tier_valeur.append(ijoueur.cartes[posMin])

        ijoueur.cartes = cartes_tier_valeur
        for i_carte in ijoueur.cartes:
            if i_carte.couleur == "Co":
                cartesTier[0].append(i_carte)
            elif i_carte.couleur == "Tr":
                cartesTier[1].append(i_carte)
            elif i_carte.couleur == "Ca":
                cartesTier[2].append(i_carte)
            elif i_carte.couleur == "Pi":
                cartesTier[3].append(i_carte)

        cartes_tier_valeur = cartesTier[0] + cartesTier[1] + cartesTier[2] + cartesTier[3]
        ijoueur.cartes = cartes_tier_valeur

        return ijoueur

    def listecarte_jouable(self, joueur, plis, atout):
        # je suis le premier a jouer
        if plis == []:
            carte_jouable = joueur.cartes

        else:
            # je note les couleurs dans le deck
            couleurDispo = []
            for i_carte in joueur.cartes:
                if not i_carte.couleur in couleurDispo:
                    couleurDispo.append(i_carte.couleur)

            # j'ai la couleur
            if plis[1] in couleurDispo:
                carte_jouable = self.eleminationParCouleur(joueur.cartes, plis[1])

                # si la couleur est de l'Atout
                if plis[1] == atout:

                    carte_jouable = self.eleminationParNombre(
                        carte_jouable, plis[2].ordre
                    )
            # Mon partenaire est maitre
            elif plis[0].nom == joueur.coequipier:
                carte_jouable = joueur.cartes

            elif atout in couleurDispo:
                carte_jouable = self.eleminationParCouleur(joueur.cartes, atout)
                if plis[2].couleur == atout:
                    carte_jouable = self.eleminationParNombre(
                        carte_jouable, plis[2].ordre
                    )
            else:
                carte_jouable = joueur.cartes
            main_gagnante = False
        return carte_jouable


    def eleminationParCouleur(self, cartes, couleurImp):
        carte_jouable = []
        for i_carte in cartes:
            if i_carte.couleur == couleurImp:
                carte_jouable.append(i_carte)
        return carte_jouable

    def eleminationParNombre(self, cartes, ValeurMin):
        carte_jouable = []
        for i_carte in cartes:
            if i_carte.ordre > ValeurMin:
                carte_jouable.append(i_carte)
        if carte_jouable == []:
            carte_jouable = cartes
        return carte_jouable


    ### attribution des points
    def attibuerPoint(self, atout):
        for ijoueur in self.listejoueur:
            for i_carte in range(8):
                if ijoueur.cartes[i_carte].couleur == atout:
                    if ijoueur.cartes[i_carte].valeur == "9":
                        ijoueur.cartes[i_carte].point = 14
                        ijoueur.cartes[i_carte].ordre = 7
                    elif ijoueur.cartes[i_carte].valeur == "J":
                        ijoueur.cartes[i_carte].point = 20
                        ijoueur.cartes[i_carte].ordre = 8
                    elif ijoueur.cartes[i_carte].valeur == "A":
                        ijoueur.cartes[i_carte].ordre = 6
                    elif ijoueur.cartes[i_carte].valeur == "10":
                        ijoueur.cartes[i_carte].ordre = 5
                    elif ijoueur.cartes[i_carte].valeur == "K":
                        ijoueur.cartes[i_carte].ordre = 4
                    elif ijoueur.cartes[i_carte].valeur == "Q":
                        ijoueur.cartes[i_carte].ordre = 3
                    elif ijoueur.cartes[i_carte].valeur == "8":
                        ijoueur.cartes[i_carte].ordre = 2
                    elif ijoueur.cartes[i_carte].valeur == "7":
                        ijoueur.cartes[i_carte].ordre = 1

        for ijoueur in self.listejoueur:
            ijoueur = self.trierCarte(ijoueur)

        return (J0, J1, J2, J3)




#############################################
#############################################



if __name__ == "__main__":


    J0 = joueur(0)
    J1 = joueur(1)
    J2 = joueur(2)
    J3 = joueur(3)
    listejoueur = Listejoueur(J0, J1, J2, J3)
    TOUR_JOUEUR = [J0, J1, J2, J3]
    LISTE_CARTE = ListeCarte(1, 1, 1, 1, 1)


    ### je distribue
    scoreFinal = 300
    premierTour = True
    root = tk.Tk ( )
    root.geometry("1375x800")

    while (J0.score < scoreFinal) and (J1.score < scoreFinal):



        text_script = "J0/J2 : " + str(J0.score) + "  ----  J1/J3 : " + str(J1.score)
        score_script =  tk.Label(root, text = text_script, font=("Arial", 15, "bold"))
        score_script.place(x=950, y=100)

        LISTE_CARTE.creerCarte()

        partie = Parti(LISTE_CARTE.LISTE_CATRE, J0, J1, J2, J3)

        if premierTour == True:
            premierjoueur = random.choice(partie.listejoueur)
            premierTour = False
        else:
            if premierjoueur == J3:
                premierjoueur = J0
            else:
                pos = TOUR_JOUEUR.index(premierjoueur)
                premierjoueur = TOUR_JOUEUR[1 + pos]

        print("le premier jouerur est ", premierjoueur.nom)

        partie.defListeJoueur(premierjoueur)

        J0, J1, J2, J3 = partie.distribuer(premierjoueur)



        ############################################################################""


        variable = ClassToStoreReturnedVariable()

        TKV_Modifier = tk.StringVar (master= root ,value='rr')

        #TKV_Modifier = tk.IntVar (master= root ,value=1)


        Im_bt1 = ajoutImage( J0.cartes[0].nom + ".png", 200, 550, 0)
        Im_bt2 = ajoutImage( J0.cartes[1].nom + ".png", 325, 550, 0)
        Im_bt3 = ajoutImage( J0.cartes[2].nom + ".png", 450, 550, 0)
        Im_bt4 = ajoutImage( J0.cartes[3].nom + ".png", 575, 550, 0)
        Im_bt5 = ajoutImage( J0.cartes[4].nom + ".png", 700, 550, 0)
        Im_bt6 = ajoutImage( J0.cartes[5].nom + ".png", 825, 550, 0)
        Im_bt7 = ajoutImage( J0.cartes[6].nom + ".png", 950, 550, 0)
        Im_bt8 = ajoutImage( J0.cartes[7].nom + ".png", 1075, 550, 0)

        J1_im = ajoutImage( "doscarte.JPEG", 20, 300, 270)
        J2_im = ajoutImage( "doscarte.JPEG", 600, 20, 180)
        J3_im = ajoutImage( "doscarte.JPEG", 1200, 300, 90)

        J1_im.bouton.config(text = "J1", font=("Arial", 60, "bold"),fg= "gray51")
        J2_im.bouton.config(text = "J2", font=("Arial", 60, "bold"),fg= "gray51")
        J3_im.bouton.config(text = "J3", font=("Arial", 60, "bold"),fg= "gray51")


        Atout = random.choice(["Co", "Ca", "Pi", "Tr"])
        Mise = random.choice(range(80, 160, 10))
        JoeurMisant = random.choice(partie.listejoueur)

        miseW = MiseWindow(JoeurMisant.nom,Mise,Atout)
        root.wait_window ( miseW )

        print("La mise est ", JoeurMisant.nom, Mise, Atout)

        Im_bt1.bouton.destroy()
        Im_bt2.bouton.destroy()
        Im_bt3.bouton.destroy()
        Im_bt4.bouton.destroy()
        Im_bt5.bouton.destroy()
        Im_bt6.bouton.destroy()
        Im_bt7.bouton.destroy()
        Im_bt8.bouton.destroy()

        text_script = JoeurMisant.nom + ' : ' + str(Mise) + '  ' + Atout
        anonce_script =  tk.Label(root, text = text_script, font=("Arial", 20, "bold"))
        anonce_script.place(x=1000, y=30)





        # attribution des points en fonction de l'atout choisi
        J0, J1, J2, J3 = partie.attibuerPoint(Atout)


        partie.jouer(premierjoueur, Atout)

        if JoeurMisant.point >= Mise:
            Gain = 1
        else:
            Gain = 0


        ReussitWindow=Score(Gain,JoeurMisant.point,Mise )

        root.wait_window ( ReussitWindow)

        print(
            "Equipe 1  ",
            J0.point,
            "// Equipe 2  :",
            J1.point,
            " sur  ",
            J0.point + J1.point,
        )

        J0, J1, J2, J3 = partie.attributionScore(Mise, JoeurMisant, J0, J1, J2, J3)

        print(
            "Equipe 1  ",
            J0.score,
            "// Equipe 2  :",
            J1.score,
            " sur  ",
            J0.point + J1.point,
        )







    root.mainloop()
