# Rony Josue Granados Iquique  201020874

# importaciones
import ast 
import random

# Extraemos el los parametros

adata=open("/home/rony/Desktop/data")
adatax=open("/home/rony/Desktop/xs")
adatay=open("/home/rony/Desktop/ys")

# Declaramos nuestras variables
m=0
n=0

#Extraccion
lin_data=adata.readline().strip()# limpiamos la linea
datos=lin_data.split(",") # linea con alpha,iteraciones,tolerancia
if(len(datos)==3):
	alfa=ast.literal_eval(datos[0]) # var alpha
	iteraciones=ast.literal_eval(datos[1]) #var ite
	tolerancia=ast.literal_eval(datos[2]) # var tol

	# sacamos los valores de X0
	m=0
	n=0
	linea=adatax.readline().strip()
	if (linea!=""):
		
		while linea!="":	
			m=m+1;
			linea=adatax.readline().strip()
			t0=linea.split(",")
			if m==1:
				n=len(t0)
		
		print m # var m
		print n	# var n
		# validar mismos valores en ys

		#matriz x		
		
		matrix=[[None] * n for i in range(m)]
		adatax.close()
		adatax=open("/home/rony/Desktop/xs")
		# Llenamos la matriz x
		linea=""
		linea=adatax.readline().strip()
		temp0=0		
		while linea!="":	
			t0=linea.split(",")
			cont=0
			while cont<n:
				matrix[temp0][cont]=ast.literal_eval(t0[cont])
				cont=cont+1				
			temp0=temp0+1
			linea=adatax.readline().strip()
		#----------------------------------------------------------
		# Matriz de y
		matriy=[[None] * 1 for i in range(m)]	
		# Llenamos la matriz x
		linea=""
		linea=adatay.readline().strip()
		temp0=0		
		while linea!="":	
			matriy[temp0][0]=ast.literal_eval(linea)				
			temp0=temp0+1
			linea=adatay.readline().strip()
		# Matriz de tetas
		matte=[[None] * 1 for i in range(n)]	
		# Llenamos la matriz tetas
		temp0=0		
		while temp0<n:	
			matte[temp0][0]=random.randrange(1,10,1)				
			temp0=temp0+1
		print "matriz teta random"
		print matte

		## Comenzamos el algoritmo
		costo=0
		contit=0
		banderacosto=True
		asalida=open("/home/rony/Desktop/salida","a")
		while contit<iteraciones and banderacosto:
			cont11=0
			while cont11<n: # numero de tetas es igual a n
				
				valt=0				
				cont12=0
				while cont12<m: # sumatoria interna por cada teta
					valh=0
					cont13=0
					while cont13<n:# sumamos h(x)
						valh=valh+(matte[cont13][0]*matrix[cont12][cont13])						
						cont13=cont13+1					
					valt=valh-matriy[cont12][0]
					valt=valt*matrix[cont11][cont12]
					cont12=cont12+1
				valt=valt*alfa
				valt=valt/m
				matte[cont11][0]=matte[cont11][0]-valt
				cont11=cont11+1	# fin iteracino teta
			# escribimos la salida
			cont35=0			
			while(cont35<n):
				asalida.write("teta :"+str(cont35)+" = "+str(matte[cont35][0])+"/n")
				cont35=cont35+1
				
			print "matriz tetas"
			print matte

			# Calculamos costos
			costototal=0
			
			cont55=0
			while cont55<m:# calculamos costo 
				
				cont65=0
				canth=0
				while cont65<n:
					canth=canth+(matte[cont65][0]*matrix[cont55][cont65])
					cont65=cont65+1
				canth=canth-matriy[cont55][0]
				canth=canth*canth
				canth=canth*m
				canth=canth/2
				costototal=costototal+canth
				cont55=cont55+1
			print "costo iteracion"
			print costototal
			asalida.write("Costo iteracion "+str(costototal))
			if costototal<tolerancia:#Comparamos tolerancia
				banderacosto=False
				
			contit=contit+1
		asalida.close()
		

		## Comenzamos el algoritmo

		print "matriz xs:"
		print matrix
		print "matriz ys:"
		print matriy
		
		


	else:
		print "Archivo xs.py vacio"		

else:
	print "Archivo data incompleto"

print "Programa Terminado"
#Cerramos archivos
adatax.close()
adatay.close()
adata.close()



