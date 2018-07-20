# Map Of Burkina Faso 
#V.1.0
#By ____Zcorp_____
# issoufzanne52@gmail.com
# Licence : Libre === M.F.C.I.Y.F.C 
# Le texte pour le traçage est join avec le code ci ! 



# IMPORT OF MODULES 

import turtle


# Variables globales pour la carte 
POS_DEPART_H = -600,300     # Ici pour aller horizontale , on decremente le 2e membre de 45
POS_DEPART_V = -600,-300
LABEL_CADRE = turtle.Turtle() # La tortue principale ou crayon de dessin 

# Coordonnées de tous les points 
COORDONNE_POINTS = [(-180,225),(-45,225),(-45,135),(0,90),(0,45),(90,45),(90,-90),(45,-90),(0,-135),(-315,-135),(-315,-270),(-360,-225),(-360,-270),(-495,-270),(-585,-180),(-540,-45),(-495,-45),(-450,90),(-405,90),(-180,225)]
LETTRE = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
CHIFFRE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


# Fonctions principales

def CadrePrincipale(cadre):
	""" Le cadre principale et les graduations du plan  """
	global LABEL_CADRE
	cadre = LABEL_CADRE
	cadre.up()
	cadre.speed('slow')
	cadre.goto(POS_DEPART_H)
	cadre.down()
	cadre.color('blue')
	cadre.width(5)
	for i in range(2):
		cadre.fd(800)
		cadre.right(90)
		cadre.fd(600)
		cadre.right(90)
	GraduerLettre(cadre)
	GraduerChiffre(cadre)
	TraitVertical(cadre)
	TraitHorizontal(cadre)
	Pointer(cadre)
	TracerCarte(cadre)
	cadre.hideturtle()
	Zcorp(cadre)
	turtle.mainloop()	


def GraduerLettre(cadre):
	""" La graduation des lettres sur le plan du cadre à gauche à l'externe   """
	cadre.up()
	cadre.color('grey')
	cadre.goto(-630,270)
	cadre.right(90)
	tail = len(LETTRE)
	j = 0
	while(j<tail):
		cadre.down()
		cadre.write(LETTRE[j],font=('times',15))
		cadre.up()
		cadre.fd(45)
		j+=1
		
	    

def GraduerChiffre(cadre):
	""" La graduation des chiifres sur le cadre dans le plan en dessus à l'externe """
	cadre.up()
	cadre.color('grey')
	cadre.goto(-585,315)
	cadre.lt(90)
	tail = len(CHIFFRE)
	j=0
	while(j<tail):
		cadre.down()
		cadre.write(CHIFFRE[j],font=('times',15))
		cadre.up()
		cadre.fd(45)
		j+=1




def TraitHorizontal(cadre):
    """ Les lignes horizontales pour le plan """
    cadre.up()
    cadre.goto(-600,270)
    for k in range(7):
    	cadre.down()
    	cadre.fd(800)
    	cadre.right(90)
    	cadre.up()
    	cadre.fd(45)
    	cadre.right(90)
    	cadre.down()
    	cadre.fd(800)
    	cadre.lt(90)
    	cadre.up()
    	cadre.fd(45)
    	cadre.lt(90)	




def TraitVertical(cadre):
	""" Dessin des traits verticaux sur le plan  """
	cadre.up()
	cadre.color('brown')
	cadre.width(1)
	cadre.shape("turtle")
	cadre.goto(-585,315)
	for i in range(9):
		cadre.down()
		cadre.right(90)
		cadre.fd(600)
		cadre.up()
		cadre.lt(90)
		cadre.fd(45)
		cadre.lt(90)
		cadre.down()
		cadre.fd(600)
		cadre.right(90)
		cadre.up()
		cadre.fd(45)

    

def Pointer(cadre):
	""" Les points sur les coordonnées sur le plan  """
	cadre.up()
	cadre.color('green')
	cadre.speed('slowest')
	j = 0
	tail = len(COORDONNE_POINTS)
	for i in range(tail):
		cadre.goto(COORDONNE_POINTS[j])
		cadre.down()
		cadre.dot(10)
		cadre.up()
		j+=1

def TracerCarte(cadre):
	""" Le traçage des segments de la carte  """
	cadre.up()
	cadre.color('purple')
	cadre.width(7)
	cadre.speed('slowest')
	cadre.goto(COORDONNE_POINTS[0])
	cadre.down()
	i = 0
	tail = len(COORDONNE_POINTS)
	while(i<tail):
		cadre.goto(COORDONNE_POINTS[i])
		i+=1


def Zcorp(cadre):
	""" Ici c'est M.P.D.S === Mon Putain De Spitch """
	cadre.up()
	cadre.goto(300,300)
	cadre.down()
	cadre.color('teal')
	cadre.write('____By___Zcorp____',font=('times',20,('bold')))
	cadre.up()	
	cadre.goto(300,250)
	cadre.down()
	cadre.write('issoufzanne52@gmail.com',font=('times',20,('bold')))
	cadre.up()	
	cadre.goto(300,200)
	cadre.down()
	cadre.write('Version : 1.0',font=('times',30,('bold')))



if __name__ == '__main__':
	CadrePrincipale(LABEL_CADRE)

  





   