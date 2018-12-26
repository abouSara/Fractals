import matplotlib.pyplot as plt
import numpy as np
import math

'''	
Fonction qui affiche le polygone défini par 
les sommets d'affixe a	'''

def affiche(a):
	plt.fill(a.real, a.imag)
	#plt.plot(a.real, a.imag,'o')
	plt.axis('equal')
	


# initialisation du vecteur position/angle/taille 
pat0 = np.zeros([1,3], dtype=complex)
# la position est le centre du côté horizontal
# l'angle initial est 0 = horizontal
# la taille est 1
pat0[0, :] = [0*np.exp(1j*0), 0, 1 ]

# nombre de récurrences
rec = 0

def layer(pat0): 
	global rec
	# nombre de positions de départ
	n = pat0.shape[0] 
	print('recurrence execution', rec)
	print('initial positions number', n)

	# chaque position de départ créé 3 nouvelles positions
	pat = np.zeros([3*n, 3], dtype = complex)
	# affixes des sommets intermédiaires
	s = np.zeros([n, 3], dtype = complex)
	
	# on itère sur les positions de départs
	for i in range(n):
		position = pat0[i, 0]
		angle = pat0[i, 1]
		taille = pat0[i, 2]

		# chacune crée 3 sommets à partir du milieu de la base du triangle
		# l'écriture d'Euler est privilégiée 		
		s[i, 0] = position + (taille/2)*np.exp(1j*math.pi*angle/180) 
		s[i, 1] = position + (math.sqrt(3)*taille/2)*np.exp(1j*math.pi*(angle+90)/180) 
		s[i, 2] = position - (taille/2)*np.exp(1j*math.pi*angle/180) 
		# on termine la liste des sommets par le premier pour fermer le polygone
		#s[i, 3] = s[i, 0]		

		# on génère 3 nouvelles positions pour chaque position
		# le milieu de chaque côté devient position
		pat[3*i+0, 0] = (s[i, 0] + s[i, 1])/2
		# l'angle est donnée par le vecteur s0s1
		pat[3*i+0, 1] = np.angle(s[i, 0] - s[i, 1], deg=True)
		# la taille du prochain triangle est divisée par 2
		pat[3*i+0, 2] = taille/2

		pat[3*i+1, 0] = (s[i, 1] + s[i, 2])/2
		pat[3*i+1, 1] = np.angle(s[i, 1] - s[i, 2], deg=True)
		pat[3*i+1, 2] = taille/2

		'''pat[3*i+2, 0] = (s[i, 2] + s[i, 3])/2
		pat[3*i+2, 1] = np.angle(s[i, 2] - s[i, 3], deg=True)
		pat[3*i+2, 2] = taille/2'''

		#print('output pat :' , pat.shape[0])

		affiche(s[i, :])
	rec = rec +1
	if rec <=6:		
		layer(pat)
	else:
		return

layer(pat0)
filename = '/Users/salim/PycharmProjects/untitled/Fractals/'+str(6)+'.png'
plt.savefig(filename)
plt.show()

