import urllib.request
from bs4 import BeautifulSoup
nacional='https://www.nacionalquiniela.com/quiniela-nacional.php?del-dia='
provincia='https://www.nacionalquiniela.com/quiniela-de-la-provincia.php?del-dia='
tucuman='https://www.nacionalquiniela.com/quiniela-tucuman.php?del-dia='
cordoba='https://www.nacionalquiniela.com/quiniela-cordoba.php?del-dia='
sanluis='https://www.nacionalquiniela.com/quiniela-san-luis.php?del-dia='
santafe='https://www.nacionalquiniela.com/quiniela-santa-fe.php?del-dia='

años=[2019]		#se recomienda dejar la lista años con un solo año cargado para evitar una sobrecarga en el sitio (supongo)
resultados=[]	
for aa in años:
	for mm in range(1,13):
		for dd in range(1,32):
			urlCode = urllib.request.urlopen(nacional + str(aa)+'-'+str(mm)+'-'+str(dd)+'').read()
			sopaFria=BeautifulSoup(urlCode)
			etiquetasTr=sopaFria('tr')
			contador=1
			for i in etiquetasTr:
				tagTr=str(i)
				if '<tr class="danger"> <th class="res-sm text-center" colspan="2">' in tagTr and '</th> </tr>'in tagTr:
					#es la linea correspondiente a los encabezados de las tablas (podemos verla haciendo print(tagTr))
					#print(tagTr)
					#cuando se encuentra esta linea se resetea a 1 el contador 
					contador=1
				elif '<tr> <td class="res-sm text-center"> 'in tagTr or 'tr class="info"> <td class="res-sm text-center"> 'in tagTr:
					#esta linea contiene la posicion y el numero ganador. La posicion queda establecida por el contador
					#y solo se extrae el numero ganador
					try:
						#en caso de que no haya habido sorteo se capturará un error evitando que se intente cargar algo en la lista resultados
						numero=int(tagTr[len(tagTr)-14:len(tagTr)-10])
						resultados.append((contador,numero))
						contador+=1
					except ValueError:
						contador+=1
guardar=open("salidaDatos.txt",'w',encoding="utf-8")
guardar.write(str(resultados))
guardar.close()
