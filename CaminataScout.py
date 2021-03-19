# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading
import random
import time
import os
import shutil

class CaminataScout:
	def __init__(self):
		self.ventana2=Tk()
		self.ventana2.title("Panel de Control")
		self.ventana2.geometry("320x341+1030+210")
		self.ventana2.configure(background='light green')
		self.ventana2.resizable(0,0)
		self.ventana=Toplevel()
		self.ventana.protocol("WM_DELETE_WINDOW",self.cerrar)
		self.ventana.title("Caminata Scout OGSL® y BBSV")
		self.ventana.geometry("1024x640+0+27")
		self.ventana.resizable(0,0)
		self.image0=PhotoImage(file=".imagenes/bosque1.png")#bosque
		self.image1=PhotoImage(file=".imagenes/cs46.png")#espacio carnita
		self.image2=PhotoImage(file=".imagenes/cs9b.png")#baston carnita
		self.image3=PhotoImage(file=".imagenes/cs17.png")#persona amarillo
		self.image4=PhotoImage(file=".imagenes/cs45.png")#espacio amarillo
		self.image5=PhotoImage(file=".imagenes/cs47.png")#flecha baja amarillo
		self.image6=PhotoImage(file=".imagenes/cs48.png")#giro arriba-izquierdo amarillo
		self.image7=PhotoImage(file=".imagenes/cs28.png")#carta 4 amarillo
		self.image8=PhotoImage(file=".imagenes/cs49.png")#flecha izquierdo amarillo
		self.image9=PhotoImage(file=".imagenes/cs51.png")#Final
		self.image10=PhotoImage(file=".imagenes/cs42.png")#guerra amarillo
		self.image11=PhotoImage(file=".imagenes/cs52.png")#giro abajo izquierdo amarillo
		self.image12=PhotoImage(file=".imagenes/cs44.png")#punto de reunion amarillo
		self.image13=PhotoImage(file=".imagenes/cs9.png")#baston amarillo
		self.image14=PhotoImage(file=".imagenes/cs53.png")#giro derecha arriba amarillo
		self.image15=PhotoImage(file=".imagenes/cs54.png")#giro derecha abajo amarillo
		self.image16=PhotoImage(file=".imagenes/cs55.png")#giro izquierdo abajo amarillo
		self.image17=PhotoImage(file=".imagenes/cs34.png")#peligro amarillo
		self.image18=PhotoImage(file=".imagenes/cs56.png")#giro arriba derecha amarillo
		self.image19=PhotoImage(file=".imagenes/cs40.png")#paz amarillo
		self.image20=PhotoImage(file=".imagenes/cs26.png")#carta 2 amarillo
		self.image21=PhotoImage(file=".imagenes/cs30.png")#flanquear amarillo
		self.image22=PhotoImage(file=".imagenes/cs57.png")#flecha arriba amarillo
		self.image23=PhotoImage(file=".imagenes/cs13.png")#machete amarillo
		self.image24=PhotoImage(file=".imagenes/cs15.png")#aprisa amarillo
		self.image25=PhotoImage(file=".imagenes/cs27.png")#carta 3 amarillo
		self.image26=PhotoImage(file=".imagenes/cs21.png")#bolas amarillo
		self.image27=PhotoImage(file=".imagenes/cs36.png")#escalar amarillo
		self.image28=PhotoImage(file=".imagenes/cs38.png")#leña amarillo
		self.image29=PhotoImage(file=".imagenes/cs58.png")#giro izquierdo arriba amarillo
		self.image30=PhotoImage(file=".imagenes/cs59.png")#giro abajo derecha amarillo
		self.image31=PhotoImage(file=".imagenes/cs32.png")#agua amarillo
		self.image32=PhotoImage(file=".imagenes/cs11.png")#tarjeta 2 grado amarillo
		self.image33=PhotoImage(file=".imagenes/cs25.png")#carta 1 amarillo
		self.image34=PhotoImage(file=".imagenes/cs21b.png")#bolas carnita
		self.image35=PhotoImage(file=".imagenes/cs19b.png")#rayas carnita
		self.image36=PhotoImage(file=".imagenes/cs23.png")#esconderse amarillo
		self.image37=PhotoImage(file=".imagenes/cs3.png")#brujula amarillo
		self.image38=PhotoImage(file=".imagenes/cs50.png")#inicio
		#--1 fase--138
		self.paisa1=Label(self.ventana,bd=0,image=self.image0)
		self.paisa1.place(x=0,y=0)
		self.final1=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image7).place(x=153,y=221)
		Label(self.ventana,bd=0,image=self.image14).place(x=113,y=221)
		Label(self.ventana,bd=0,image=self.image4).place(x=113,y=181)
		Label(self.ventana,bd=0,image=self.image17).place(x=73,y=181)
		Label(self.ventana,bd=0,image=self.image10).place(x=33,y=181)
		self.final1.place(x=33,y=221)
		#--2 fase--133
		self.paisa2=Label(self.ventana,bd=0,image=self.image0)
		self.paisa2.place(x=0,y=0)
		self.final2=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image13).place(x=273,y=141)		
		Label(self.ventana,bd=0,image=self.image12).place(x=273,y=101)
		Label(self.ventana,bd=0,image=self.image4).place(x=273,y=61)
		Label(self.ventana,bd=0,image=self.image11).place(x=273,y=21)		
		Label(self.ventana,bd=0,image=self.image10).place(x=233,y=21)
		Label(self.ventana,bd=0,image=self.image3).place(x=193,y=21)
		Label(self.ventana,bd=0,image=self.image4).place(x=193,y=61)
		Label(self.ventana,bd=0,image=self.image1).place(x=153,y=21)
		Label(self.ventana,bd=0,image=self.image5).place(x=193,y=101)
		Label(self.ventana,bd=0,image=self.image2).place(x=113,y=21)
		Label(self.ventana,bd=0,image=self.image4).place(x=193,y=141)
		Label(self.ventana,bd=0,image=self.image1).place(x=73,y=21)
		Label(self.ventana,bd=0,image=self.image4).place(x=193,y=181)
		Label(self.ventana,bd=0,image=self.image1).place(x=73,y=61)
		Label(self.ventana,bd=0,image=self.image1).place(x=73,y=101)
		Label(self.ventana,bd=0,image=self.image1).place(x=113,y=101)
		Label(self.ventana,bd=0,image=self.image2).place(x=153,y=101)
		Label(self.ventana,bd=0,image=self.image6).place(x=193,y=221)
		self.final2.place(x=153,y=221)
		#--3 fase--123
		self.paisa3=Label(self.ventana,bd=0,image=self.image0)
		self.paisa3.place(x=0,y=0)
		self.final3=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image4).place(x=393,y=21)
		Label(self.ventana,bd=0,image=self.image15).place(x=353,y=21)
		Label(self.ventana,bd=0,image=self.image19).place(x=353,y=61)
		Label(self.ventana,bd=0,image=self.image18).place(x=353,y=101)
		Label(self.ventana,bd=0,image=self.image17).place(x=393,y=101)
		Label(self.ventana,bd=0,image=self.image16).place(x=433,y=101)
		Label(self.ventana,bd=0,image=self.image4).place(x=433,y=141)
		Label(self.ventana,bd=0,image=self.image6).place(x=433,y=181)
		Label(self.ventana,bd=0,image=self.image15).place(x=393,y=181)
		Label(self.ventana,bd=0,image=self.image6).place(x=393,y=221)
		Label(self.ventana,bd=0,image=self.image10).place(x=353,y=221)
		Label(self.ventana,bd=0,image=self.image4).place(x=313,y=221)
		Label(self.ventana,bd=0,image=self.image14).place(x=273,y=221)
		Label(self.ventana,bd=0,image=self.image4).place(x=273,y=181)
		Label(self.ventana,bd=0,image=self.image13).place(x=273,y=141)
		self.final3.place(x=273,y=101)
		#--4 fase--108
		self.paisa4=Label(self.ventana,bd=0,image=self.image0)
		self.paisa4.place(x=0,y=0)
		self.final4=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image4).place(x=593,y=301)
		Label(self.ventana,bd=0,image=self.image4).place(x=593,y=341)
		Label(self.ventana,bd=0,image=self.image5).place(x=593,y=381)
		Label(self.ventana,bd=0,image=self.image4).place(x=593,y=421)
		Label(self.ventana,bd=0,image=self.image6).place(x=593,y=461)
		Label(self.ventana,bd=0,image=self.image25).place(x=553,y=461)
		Label(self.ventana,bd=0,image=self.image14).place(x=513,y=461)
		Label(self.ventana,bd=0,image=self.image24).place(x=513,y=421)
		Label(self.ventana,bd=0,image=self.image4).place(x=513,y=381)
		Label(self.ventana,bd=0,image=self.image22).place(x=513,y=341)
		Label(self.ventana,bd=0,image=self.image4).place(x=513,y=301)
		Label(self.ventana,bd=0,image=self.image23).place(x=513,y=261)
		Label(self.ventana,bd=0,image=self.image4).place(x=513,y=221)
		Label(self.ventana,bd=0,image=self.image22).place(x=513,y=181)
		Label(self.ventana,bd=0,image=self.image4).place(x=513,y=141)
		Label(self.ventana,bd=0,image=self.image21).place(x=513,y=101)
		Label(self.ventana,bd=0,image=self.image4).place(x=513,y=61)
		Label(self.ventana,bd=0,image=self.image11).place(x=513,y=21)
		Label(self.ventana,bd=0,image=self.image4).place(x=473,y=21)
		Label(self.ventana,bd=0,image=self.image20).place(x=433,y=21)
		self.final4.place(x=393,y=21)
		#--5 fase--89
		self.paisa5=Label(self.ventana,bd=0,image=self.image0)
		self.paisa5.place(x=0,y=0)
		self.final5=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image27).place(x=913,y=221)
		Label(self.ventana,bd=0,image=self.image4).place(x=913,y=181)
		Label(self.ventana,bd=0,image=self.image30).place(x=913,y=141)
		Label(self.ventana,bd=0,image=self.image29).place(x=953,y=141)
		Label(self.ventana,bd=0,image=self.image28).place(x=953,y=101)
		Label(self.ventana,bd=0,image=self.image4).place(x=953,y=61)
		Label(self.ventana,bd=0,image=self.image11).place(x=953,y=21)
		Label(self.ventana,bd=0,image=self.image4).place(x=913,y=21)
		Label(self.ventana,bd=0,image=self.image24).place(x=873,y=21)
		Label(self.ventana,bd=0,image=self.image15).place(x=833,y=21)
		Label(self.ventana,bd=0,image=self.image4).place(x=833,y=61)
		Label(self.ventana,bd=0,image=self.image4).place(x=833,y=101)
		Label(self.ventana,bd=0,image=self.image6).place(x=833,y=141)
		Label(self.ventana,bd=0,image=self.image27).place(x=793,y=141)
		Label(self.ventana,bd=0,image=self.image26).place(x=753,y=141)
		Label(self.ventana,bd=0,image=self.image4).place(x=713,y=141)
		Label(self.ventana,bd=0,image=self.image4).place(x=753,y=101)
		Label(self.ventana,bd=0,image=self.image6).place(x=673,y=141)
		Label(self.ventana,bd=0,image=self.image11).place(x=753,y=61)
		Label(self.ventana,bd=0,image=self.image4).place(x=633,y=141)
		Label(self.ventana,bd=0,image=self.image23).place(x=713,y=61)
		Label(self.ventana,bd=0,image=self.image15).place(x=593,y=141)
		Label(self.ventana,bd=0,image=self.image15).place(x=673,y=61)
		Label(self.ventana,bd=0,image=self.image17).place(x=593,y=181)
		Label(self.ventana,bd=0,image=self.image4).place(x=673,y=101)
		Label(self.ventana,bd=0,image=self.image5).place(x=593,y=221)
		Label(self.ventana,bd=0,image=self.image13).place(x=593,y=261)
		self.final5.place(x=593,y=301)
		#--6 fase--64
		self.paisa6=Label(self.ventana,bd=0,image=self.image0)
		self.paisa6.place(x=0,y=0)
		self.final6=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image32).place(x=633,y=581)
		Label(self.ventana,bd=0,image=self.image29).place(x=673,y=581)
		Label(self.ventana,bd=0,image=self.image4).place(x=673,y=541)
		Label(self.ventana,bd=0,image=self.image31).place(x=673,y=501)
		Label(self.ventana,bd=0,image=self.image4).place(x=673,y=461)
		Label(self.ventana,bd=0,image=self.image22).place(x=673,y=421)
		Label(self.ventana,bd=0,image=self.image23).place(x=673,y=381)
		Label(self.ventana,bd=0,image=self.image4).place(x=673,y=341)
		Label(self.ventana,bd=0,image=self.image26).place(x=673,y=301)
		Label(self.ventana,bd=0,image=self.image4).place(x=713,y=301)
		Label(self.ventana,bd=0,image=self.image4).place(x=673,y=261)
		Label(self.ventana,bd=0,image=self.image26).place(x=753,y=301)
		Label(self.ventana,bd=0,image=self.image30).place(x=673,y=221)
		Label(self.ventana,bd=0,image=self.image4).place(x=753,y=341)
		Label(self.ventana,bd=0,image=self.image4).place(x=713,y=221)
		Label(self.ventana,bd=0,image=self.image21).place(x=753,y=381)
		Label(self.ventana,bd=0,image=self.image16).place(x=753,y=221)
		Label(self.ventana,bd=0,image=self.image4).place(x=753,y=421)
		Label(self.ventana,bd=0,image=self.image17).place(x=753,y=261)
		Label(self.ventana,bd=0,image=self.image5).place(x=753,y=461)
		Label(self.ventana,bd=0,image=self.image13).place(x=753,y=501)
		Label(self.ventana,bd=0,image=self.image4).place(x=753,y=541)
		Label(self.ventana,bd=0,image=self.image18).place(x=753,y=581)
		Label(self.ventana,bd=0,image=self.image4).place(x=793,y=581)
		Label(self.ventana,bd=0,image=self.image23).place(x=833,y=581)
		Label(self.ventana,bd=0,image=self.image17).place(x=873,y=581)
		Label(self.ventana,bd=0,image=self.image29).place(x=913,y=581)
		Label(self.ventana,bd=0,image=self.image30).place(x=913,y=541)
		Label(self.ventana,bd=0,image=self.image29).place(x=953,y=541)
		Label(self.ventana,bd=0,image=self.image4).place(x=953,y=501)
		Label(self.ventana,bd=0,image=self.image11).place(x=953,y=461)
		Label(self.ventana,bd=0,image=self.image3).place(x=913,y=461)
		Label(self.ventana,bd=0,image=self.image4).place(x=913,y=421)
		Label(self.ventana,bd=0,image=self.image1).place(x=873,y=461)
		Label(self.ventana,bd=0,image=self.image23).place(x=913,y=381)
		Label(self.ventana,bd=0,image=self.image1).place(x=833,y=461)
		Label(self.ventana,bd=0,image=self.image22).place(x=913,y=341)
		Label(self.ventana,bd=0,image=self.image1).place(x=833,y=421)
		Label(self.ventana,bd=0,image=self.image4).place(x=913,y=301)
		Label(self.ventana,bd=0,image=self.image2).place(x=833,y=381)
		Label(self.ventana,bd=0,image=self.image17).place(x=913,y=261)
		Label(self.ventana,bd=0,image=self.image1).place(x=833,y=341)
		Label(self.ventana,bd=0,image=self.image1).place(x=833,y=301)
		Label(self.ventana,bd=0,image=self.image2).place(x=833,y=261)
		Label(self.ventana,bd=0,image=self.image1).place(x=833,y=221)
		Label(self.ventana,bd=0,image=self.image1).place(x=873,y=221)
		self.final6.place(x=913,y=221)
		#--7 fase--35
		self.paisa7=Label(self.ventana,bd=0,image=self.image0)
		self.paisa7.place(x=0,y=0)
		self.final7=Label(self.ventana,bd=0,image=self.image9)
		Label(self.ventana,bd=0,image=self.image38).place(x=33,y=581)
		Label(self.ventana,bd=0,image=self.image37).place(x=33,y=541)
		Label(self.ventana,bd=0,image=self.image4).place(x=33,y=501)
		Label(self.ventana,bd=0,image=self.image22).place(x=33,y=461)
		Label(self.ventana,bd=0,image=self.image4).place(x=33,y=421)
		Label(self.ventana,bd=0,image=self.image4).place(x=33,y=381)
		Label(self.ventana,bd=0,image=self.image4).place(x=33,y=341)
		Label(self.ventana,bd=0,image=self.image30).place(x=33,y=301)
		Label(self.ventana,bd=0,image=self.image4).place(x=73,y=301)
		Label(self.ventana,bd=0,image=self.image13).place(x=113,y=301)
		Label(self.ventana,bd=0,image=self.image16).place(x=153,y=301)
		Label(self.ventana,bd=0,image=self.image4).place(x=153,y=341)
		Label(self.ventana,bd=0,image=self.image4).place(x=153,y=381)
		Label(self.ventana,bd=0,image=self.image32).place(x=153,y=421)
		Label(self.ventana,bd=0,image=self.image4).place(x=153,y=461)
		Label(self.ventana,bd=0,image=self.image23).place(x=153,y=501)
		Label(self.ventana,bd=0,image=self.image18).place(x=153,y=541)
		Label(self.ventana,bd=0,image=self.image4).place(x=193,y=541)
		Label(self.ventana,bd=0,image=self.image4).place(x=233,y=541)
		Label(self.ventana,bd=0,image=self.image24).place(x=273,y=541)
		Label(self.ventana,bd=0,image=self.image4).place(x=313,y=541)
		Label(self.ventana,bd=0,image=self.image29).place(x=353,y=541)
		Label(self.ventana,bd=0,image=self.image4).place(x=353,y=501)
		Label(self.ventana,bd=0,image=self.image4).place(x=353,y=461)
		Label(self.ventana,bd=0,image=self.image3).place(x=353,y=421)
		Label(self.ventana,bd=0,image=self.image36).place(x=393,y=421)
		Label(self.ventana,bd=0,image=self.image35).place(x=353,y=381)
		Label(self.ventana,bd=0,image=self.image16).place(x=433,y=421)
		Label(self.ventana,bd=0,image=self.image1).place(x=353,y=341)
		Label(self.ventana,bd=0,image=self.image1).place(x=313,y=381)
		Label(self.ventana,bd=0,image=self.image4).place(x=433,y=461)
		Label(self.ventana,bd=0,image=self.image34).place(x=353,y=301)
		Label(self.ventana,bd=0,image=self.image1).place(x=273,y=381)
		Label(self.ventana,bd=0,image=self.image33).place(x=433,y=501)
		Label(self.ventana,bd=0,image=self.image1).place(x=393,y=301)
		Label(self.ventana,bd=0,image=self.image2).place(x=273,y=341)
		Label(self.ventana,bd=0,image=self.image18).place(x=433,y=541)
		Label(self.ventana,bd=0,image=self.image34).place(x=433,y=301)
		Label(self.ventana,bd=0,image=self.image1).place(x=273,y=301)
		Label(self.ventana,bd=0,image=self.image21).place(x=473,y=541)
		Label(self.ventana,bd=0,image=self.image2).place(x=433,y=341)
		Label(self.ventana,bd=0,image=self.image1).place(x=313,y=301)
		Label(self.ventana,bd=0,image=self.image4).place(x=513,y=541)
		Label(self.ventana,bd=0,image=self.image1).place(x=433,y=381)
		Label(self.ventana,bd=0,image=self.image13).place(x=553,y=541)
		Label(self.ventana,bd=0,image=self.image16).place(x=593,y=541)
		Label(self.ventana,bd=0,image=self.image18).place(x=593,y=581)
		self.final7.place(x=633,y=581)
		Label(self.ventana2,text="Bienvenido, eres un elemento de las ramas intermedias, en\nel cual estas dentro de la patrulla cuervos. El jefe de la rama\nenvio a la patrulla cuervos a un recorrido de pistas de 3ra\nclase, sin embargo, mientras el jefe hacia el recorrido, se le\ncayeron algunos objetos, los cuales puedes usar durante el\nrecorrido para ayudarte.\n\nLa patrulla esta conformada entre 2-8 elementos (numero\nde jugadores) los cuales competiran para ver quien llega al\nfinal del recorrido primero. Durante el trayecto, el jefe puso\nalgunas pistas que pueden afectar tanto positiva como\n\
negativamente tu recorrido.\n\nEn el recorrido hay algunas casillas con personas quienes\npor accidente destruyeron la pista, por ende para seguir\navanzando por el camino amarillo necesitas sacar los\nsiguientes numeros: 1, 3, 5; si no es asi seguiras por el\ncamino color carnita.",background='light green').place(x=0,y=10)
		self.image47=PhotoImage(file=".imagenes/paisaje1.png")
		self.paisaje1=Label(self.ventana,bd=0,image=self.image47)
		self.paisaje1.place(x=0,y=0)
		self.image39=PhotoImage(file=".imagenes/sco1.png")#scout1
		self.image40=PhotoImage(file=".imagenes/sco2.png")#scout2
		self.image41=PhotoImage(file=".imagenes/sco3.png")#scout3
		self.image42=PhotoImage(file=".imagenes/sco4.png")#scout4
		self.image43=PhotoImage(file=".imagenes/sco5.png")#scout5
		self.image44=PhotoImage(file=".imagenes/sco6.png")#scout6
		self.image45=PhotoImage(file=".imagenes/sco7.png")#scout7
		self.image46=PhotoImage(file=".imagenes/sco8.png")#scout8
		self.comenzarPartida()
		self.ventana.mainloop()
	def comenzarPartida(self):
		Button(self.ventana2,command=self.iniciar,height=2,width=18,background="white",text="Comenzar partida").place(x=95,y=290)
		self.ventana.iconbitmap(".imagenes/venado.ico")#Cambiar el icono
		self.ventana2.iconbitmap(".imagenes/leon.ico")#Cambiar el icono
		self.fondo=Label(self.ventana2, height=23, width=45, background="light green")
		self.escogen=Label(self.ventana2, background="light green", text="   Escoge el numero de elementos (jugadores) y si deseas\n  aumentar o disminuir el numero seleccionado, selecciona\n la cantidad correcta.")
		self.ele2=Button(self.ventana2,command=lambda a=2:self.jugadores(a),height=1,width=9,background="white",text="2 jugadores")
		self.ele3=Button(self.ventana2,command=lambda a=3:self.jugadores(a),height=1,width=9,background="white",text="3 jugadores")
		self.ele4=Button(self.ventana2,command=lambda a=4:self.jugadores(a),height=1,width=9,background="white",text="4 jugadores")
		self.ele5=Button(self.ventana2,command=lambda a=5:self.jugadores(a),height=1,width=9,background="white",text="5 jugadores")
		self.ele6=Button(self.ventana2,command=lambda a=6:self.jugadores(a),height=1,width=9,background="white",text="6 jugadores")
		self.ele7=Button(self.ventana2,command=lambda a=7:self.jugadores(a),height=1,width=9,background="white",text="7 jugadores")
		self.ele8=Button(self.ventana2,command=lambda a=8:self.jugadores(a),height=1,width=9,background="white",text="8 jugadores")
		self.nicknames=Label(self.ventana2, background="light green", text="        Ingresa el NickName de cada uno de los jugadores:")
		self.uno=Label(self.ventana2, background="red", text="1:", font=("Arial",8))
		self.jug1=Entry(self.ventana2,width=11, font=("Arial",10))
		self.dos=Label(self.ventana2, background="green", text="2:", font=("Arial",8))
		self.jug2=Entry(self.ventana2,width=11, font=("Arial",10))
		self.tres=Label(self.ventana2, background="blue", text="3:", font=("Arial",8))
		self.jug3=Entry(self.ventana2,width=11, font=("Arial",10))
		self.cuatro=Label(self.ventana2, background="yellow", text="4:", font=("Arial",8))
		self.jug4=Entry(self.ventana2,width=11, font=("Arial",10))
		self.cinco=Label(self.ventana2, background="cyan", text="5:", font=("Arial",8))
		self.jug5=Entry(self.ventana2,width=11, font=("Arial",10))
		self.seis=Label(self.ventana2, background="magenta", text="6:", font=("Arial",8))
		self.jug6=Entry(self.ventana2,width=11, font=("Arial",10))
		self.siete=Label(self.ventana2, background="orange", text="7:", font=("Arial",8))
		self.jug7=Entry(self.ventana2,width=11, font=("Arial",10))
		self.ocho=Label(self.ventana2, background="aquamarine", text="8:", font=("Arial",8))
		self.jug8=Entry(self.ventana2,width=11, font=("Arial",10))
		self.elementos=(self.jug2,self.jug3,self.jug4,self.jug5,self.jug6,self.jug7,self.jug8)
		self.chequear=Button(self.ventana2,command=self.checar,height=2,width=17,background="white",text="Comenzar")
		self.fondoso=Label(self.ventana2, height=23, width=45, background="light green")
	def iniciar(self):
		self.fondo.place(x=0,y=0)
		self.escogen.place(x=0,y=15)
		self.ele2.place(x=5,y=80)
		self.ele3.place(x=84,y=80)
		self.ele4.place(x=163,y=80)
		self.ele5.place(x=242,y=80)
		self.ele6.place(x=24,y=112)
		self.ele7.place(x=123,y=112)
		self.ele8.place(x=222,y=112)
	def jugadores(self,a):
		self.jug3.configure(state="disabled")
		self.jug4.configure(state="disabled")
		self.jug5.configure(state="disabled")
		self.jug6.configure(state="disabled")
		self.jug7.configure(state="disabled")
		self.jug8.configure(state="disabled")
		self.tres.place(x=600,y=600)
		self.jug3.place(x=600,y=600)
		self.cuatro.place(x=600,y=600)
		self.jug4.place(x=600,y=600)
		self.cinco.place(x=600,y=600)
		self.jug5.place(x=600,y=600)
		self.seis.place(x=600,y=600)
		self.jug6.place(x=600,y=600)
		self.siete.place(x=600,y=600)
		self.jug7.place(x=600,y=600)
		self.ocho.place(x=600,y=600)
		self.jug8.place(x=600,y=600)
		self.nicknames.place(x=0,y=155)
		self.uno.place(x=5,y=190)
		self.jug1.place(x=20,y=190)
		self.dos.place(x=110,y=190)
		self.jug2.place(x=125,y=190)
		self.chequear.place(x=98,y=290)
		self.a=a
		self.ele2.configure(background="white")
		self.ele3.configure(background="white")
		self.ele4.configure(background="white")
		self.ele5.configure(background="white")
		self.ele6.configure(background="white")
		self.ele7.configure(background="white")
		self.ele8.configure(background="white")
		self.cortar2()
		if(a==2):
			self.ele2.configure(background="khaki")
		elif(a==3):
			self.ele3.configure(background="khaki")
		elif(a==4):
			self.ele4.configure(background="khaki")
		elif(a==5):
			self.ele5.configure(background="khaki")
		elif(a==6):
			self.ele6.configure(background="khaki")
		elif(a==7):
			self.ele7.configure(background="khaki")
		elif(a==8):
			self.ele8.configure(background="khaki")
		self.colores=["red","green","blue","yellow","cyan","magenta","orange","aquamarine"]
		#self.jug1.insert(0,self.elementos[0].get())
		if(a>2):
			self.tres.place(x=215,y=190)
			self.jug3.place(x=230,y=190)
			self.jug3.configure(state="normal")
		if(a>3):
			self.cuatro.place(x=5,y=217)
			self.jug4.place(x=20,y=217)
			self.jug4.configure(state="normal")
		if(a>4):
			self.cinco.place(x=110,y=217)
			self.jug5.place(x=125,y=217)
			self.jug5.configure(state="normal")
		if(a>5):
			self.seis.place(x=215,y=217)
			self.jug6.place(x=230,y=217)
			self.jug6.configure(state="normal")
		if(a>6):
			self.siete.place(x=40,y=244)
			self.jug7.place(x=55,y=244)
			self.jug7.configure(state="normal")
		if(a>7):
			self.ocho.place(x=180,y=244)
			self.jug8.place(x=195,y=244)
			self.jug8.configure(state="normal")
	def cerrar(self):
		self.ventana2.destroy()
	def checar(self):
		self.cortar2()
		a=8
		for i in range(0,8):
			if(len(self.elementos[i].get())==0):
				a=i;break
		if(a<self.a):
			messagebox.showinfo("¡¡Alto!!","Todos los jugadores deben de tener un NickName")
		else:
			self.jugar()
	def cortar2(self):
		self.jug1=self.cortar(self.jug1)
		self.jug2=self.cortar(self.jug2)
		self.jug3=self.cortar(self.jug3)
		self.jug4=self.cortar(self.jug4)
		self.jug5=self.cortar(self.jug5)
		self.jug6=self.cortar(self.jug6)
		self.jug7=self.cortar(self.jug7)
		self.jug8=self.cortar(self.jug8)
		self.elementos=(self.jug1,self.jug2,self.jug3,self.jug4,self.jug5,self.jug6,self.jug7,self.jug8)
	def cortar(self,a):
		while(len(a.get())>0 and a.get()[len(a.get())-1]==' '):
			a.delete(len(a.get())-1,END)
		while(len(a.get())>0 and a.get()[0]==' '):
			a.delete(0,1)
		if(len(a.get())>25):
			a.delete(25,END)
		return a
	def jugar(self):
		if(self.a<8):
			self.final7.place(x=1050,y=1050)
			self.paisa7.place(x=1050,y=1050)
			if(self.a<7):
				self.final6.place(x=1050,y=1050)
				self.paisa6.place(x=1050,y=1050)
				if(self.a<6):
					self.final5.place(x=1050,y=1050)
					self.paisa5.place(x=1050,y=1050)
					if(self.a<5):
						self.final4.place(x=1050,y=1050)
						self.paisa4.place(x=1050,y=1050)
						if(self.a<4):
							self.final3.place(x=1050,y=1050)
							self.paisa3.place(x=1050,y=1050)
							if(self.a<3):
								self.final2.place(x=1050,y=1050)
								self.paisa2.place(x=1050,y=1050)
		if(self.a==8):
			self.limx=633
			self.limy=581
		elif(self.a==7):
			self.limx=913
			self.limy=221
		elif(self.a==6):
			self.limx=593
			self.limy=301
		elif(self.a==5):
			self.limx=393
			self.limy=21
		elif(self.a==4):
			self.limx=273
			self.limy=101
		elif(self.a==3):
			self.limx=153
			self.limy=221
		else:
			self.limx=33
			self.limy=221
		self.sco1=Label(self.ventana,bd=0,image=self.image39)
		self.sco1.place(x=37,y=585)
		self.sco2=Label(self.ventana,bd=0,image=self.image40)
		self.sco2.place(x=55,y=585)
		self.turno=[[self.sco1,37,585,0,1,0,0,0,0,0,1],[self.sco2,55,585,0,1,0,0,0,0,0,1]]
		if(self.a>2):
			self.sco3=Label(self.ventana,bd=0,image=self.image41)
			self.sco3.place(x=37,y=603)
			self.turno.append([self.sco3,37,603,0,1,0,0,0,0,0,1])
			if(self.a>3):
				self.sco4=Label(self.ventana,bd=0,image=self.image42)
				self.sco4.place(x=55,y=603)
				self.turno.append([self.sco4,55,603,0,1,0,0,0,0,0,1])
				if(self.a>4):
					self.sco5=Label(self.ventana,bd=0,image=self.image43)
					self.sco5.place(x=37,y=585)
					self.turno.append([self.sco5,37,585,0,1,0,0,0,0,0,1])
					if(self.a>5):
						self.sco6=Label(self.ventana,bd=0,image=self.image44)
						self.sco6.place(x=55,y=585)
						self.turno.append([self.sco6,55,585,0,1,0,0,0,0,0,1])
						if(self.a>6):
							self.sco7=Label(self.ventana,bd=0,image=self.image45)
							self.sco7.place(x=37,y=603)
							self.turno.append([self.sco7,37,603,0,1,0,0,0,0,0,1])
							if(self.a>7):
								self.sco8=Label(self.ventana,bd=0,image=self.image46)
								self.sco8.place(x=55,y=603)
								self.turno.append([self.sco8,55,603,0,1,0,0,0,0,0,1])#btn, x, y, tur.per, carril, posi, mache, bruju, segun.cla, paz
		Label(self.ventana2, height=23, width=45, background="light green").place(x=0,y=0)
		self.lbl1=Label(self.ventana2,font=("Arial",26),background="white",text=" 1 ")
		self.lbl1.place(x=12,y=40)
		self.lbl2=Label(self.ventana2,font=("Arial",26),background="white",text=" 2 ")
		self.lbl2.place(x=62,y=40)
		self.lbl3=Label(self.ventana2,font=("Arial",26),background="white",text=" 3 ")
		self.lbl3.place(x=112,y=40)
		self.lbl4=Label(self.ventana2,font=("Arial",26),background="white",text=" 4 ")
		self.lbl4.place(x=162,y=40)
		self.lbl5=Label(self.ventana2,font=("Arial",26),background="white",text=" 5 ")
		self.lbl5.place(x=212,y=40)
		self.lbl6=Label(self.ventana2,font=("Arial",26),background="white",text=" 6 ")
		self.lbl6.place(x=262,y=40)
		Label(self.ventana2,font=("Arial",13),background="light green",text="Velocidad:").place(x=20,y=100)
		self.velo1=Button(self.ventana2,command=lambda a=1:self.velocidad(a),font=("Arial",10),background="khaki",state="disabled",text="x1",height=1,width=5)
		self.velo1.place(x=110,y=100)
		self.velo2=Button(self.ventana2,command=lambda a=2:self.velocidad(a),font=("Arial",10),background="white",text="x2",height=1,width=5)
		self.velo2.place(x=170,y=100)
		self.velo3=Button(self.ventana2,command=lambda a=4:self.velocidad(a),font=("Arial",10),background="white",text="x4",height=1,width=5)
		self.velo3.place(x=230,y=100)
		self.intento=Button(self.ventana2,command=self.tirar,font=("Arial",10),background="white",text="Tirar",height=2,width=16)
		self.intento.place(x=91,y=140)
		self.intengratis=Button(self.ventana2,command=self.tirarpremium,font=("Arial",10),background="white",text="Tirar",height=2,width=16)
		self.intengratis.place(x=91,y=500)
		self.usarmache=Button(self.ventana2,command=self.siusar,font=("Arial",10),background="white",text="Usar el machete",height=2,width=16)
		self.usarmache.place(x=91,y=600)
		self.nousarmache=Button(self.ventana2,command=self.nousar,font=("Arial",10),background="white",text="Dejarlo para despues",height=2,width=16)
		self.nousarmache.place(x=91,y=600)
		self.numturno=0
		Label(self.ventana2,font=("Arial",13),background="light green",text="Turno: ").place(x=5,y=10)
		self.numcolor=Label(self.ventana2,font=("Arial",13),background="red",text="   ")
		self.numcolor.place(x=65,y=10)
		self.nickname=Label(self.ventana2,font=("Arial",13),background="light green",text=self.elementos[0].get())
		self.nickname.place(x=80,y=10)
		self.mensaje=Label(self.ventana2,font=("Arial",15),background="light green",text="")
		self.mensaje.place(x=5,y=200)
		self.casi=[[0,0],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[40,0],[40,0],[40,0],[0,40],[0,40],[0,40],[0,40],[0,40],[0,40],[40,0],[40,0],[40,0],[40,0],[40,0],[0,-40],[0,-40],[0,-40],[40,0,0,-40],[40,0,-40,0,0,-40,],[0,40,-40,0,0,-40,],[0,40,0,-40,40,0,],[0,40,0,-40,40,0,],[40,0,40,0,0,40],[40,0,40,0,0,40],[40,0,40,0,0,40],[40,0,40,0,-6,-6],[0,40,0,40],[40,0,0,40],[40,0,0,40],[0,-40,-10,-10],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[40,0,0,-40],[40,0,0,-40],[0,40,40,0],[0,40,40,0],[0,40,0,40],[0,40,0,40],[0,40,-4,-4],[0,40],[0,40],[40,0],[40,0],[40,0],[40,0],[0,-40],[40,0],[0,-40],[0,-40],
				   [-40,0],[0,-40,-40,0],[0,-40,-40,0],[0,-40,0,-40],[0,-40,0,-40],[0,-40,0,-40],[0,-40,0,-40],[0,-40,0,-40],[0,-40,0,-40],[40,0,40,0],[0,-40,40,0],[0,-40,-4,-4],[0,-40],[-40,0],[-40,0],[-40,0],[0,40],[0,40],[0,40],[-40,0],[-40,0],[-40,0,0,-40],[-40,0,0,-40],[-40,0,-40,0],[-40,0,-40,0],[0,40,0,40],[0,40,0,40],[0,40,-4,-4],[0,40],[0,40],[0,40],[0,40],[0,40],[-40,0],[-40,0],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[0,-40],[-40,0],[-40,0],[-40,0],[-40,0],[0,40],[0,40],[40,0],[40,0],[0,40],[0,40],[-40,0],[0,40],[-40,0],[-40,0],[-40,0],[0,-40],[0,-40],[0,-40],[0,-40],
				   [0,-40],[-40,0],[-40,0],[0,40,-40,0],[0,40,-40,0],[0,40,-40,0],[0,40,0,40],[0,40,0,40],[-40,0,40,0],[-40,0,40,0],[0,-40,40,0],[-40,0,-6,-6],[-40,0],[0,40],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
		#self.mensaje.cget("text") cget para obtener los componentes en un Label  0-138
		self.mensajes=["","Hallaste una de las brujulas que se\nle cayeron al jefe, ahora seguiras\nsiempre por el camino mas corto.","","","","","","","","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.","","","","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.","","Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.","","","","Llegaste en una casilla de \"Mas a\nPrisa\" (Avanzas 2 casillas).","","","","",
					  "Desde tu posicion actual observas\n2 caminos, si posees 1 brujula u\nobtienes los numeros \"1, 3, 5\"\nseguiras por el camino mas corto,\nde lo contrario seguiras por el\ncamino mas largo.",["Debes esconderte ante un peligro\ninminente (Pierdes el siguiente\nturno).","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase."],["","",""],["","","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase."],["Llegaste a una casilla \"Espera\naqui\" (el numero dentro marca el\nnumero de turnos que perderas).",
					  "Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.",""],["","","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase."],["Tienes frente de ti un obstaculo\nque debes flanquear (Pierdes 2\nturnos).","","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis."],["","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.",""],
					  ["Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.","",""],["","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.",""],["","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis."],["Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.",""],["",""],["",""],"Debes llevar agua al campamento\n(Pierdes un turno).","","",
					  "Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.","","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.",["",""],["Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.",""],["",""],["Tienes frente de ti un obstaculo\nque debes flanquear (Pierdes 2\nturnos).",""],["","Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas)."],["","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase."],
					  ["Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.",""],"","","","Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.","Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas).","","","","","","Desde tu posicion actual observas\n2 caminos, si posees 1 brujula u\nobtienes los numeros \"1, 3, 5\"\nseguiras por el camino mas corto,\nde lo contrario seguiras por el\ncamino mas largo.",["",""],
					  ["Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.",""],["",""],["","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis."],["Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas).",""],["Debes escalar un obstaculo\ninevitable (Pierdes dos turnos).",""],["","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis."],["",""],["",""],
					  ["Debes llevar leña al campamento\n(Pierdes un turno).","Debes escalar un obstaculo\ninevitable (Pierdes dos turnos)."],["",""],"","","Llegaste en una casilla de \"Mas a\nPrisa\" (Avanzas 2 casillas).","","","","","Debes escalar un obstaculo\ninevitable (Pierdes dos turnos).","Conseguiste una cartilla de 2da\nclase, ahora podras pasar por las\npistas de 2da clase.",["",""],["",""],["","Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues."],["",""],["Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas).",""],
					  ["",""],["Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.",""],"","","","","","Llegaste a una casilla \"Espera\naqui\" (el numero dentro marca el\nnumero de turnos que perderas).","","Llegaste en una casilla de \"Mas a\nPrisa\" (Avanzas 2 casillas).","","","","Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.","","","","Tienes frente de ti un obstaculo\nque debes flanquear (Pierdes 2\nturnos).","","","",
					  "Llegaste a una casilla \"Espera\naqui\" (el numero dentro marca el\nnumero de turnos que perderas).","","","Haces una declaracion de paz (Si\ncaes en una casilla de guerra\npierdes un turno).","","Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas).","","","","","","Llegaste a una casilla de guerra y\nte vez forzado a declararla.","","","","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.","Pasas en una zona de ataque, por\nlo que debes esperar a que otro\nelemento te releve.","","",
					  "Llegaste a una casilla de guerra y\nte vez forzado a declararla.","Desde tu posicion actual observas\n2 caminos, si posees 1 brujula u\nobtienes los numeros \"1, 3, 5\"\nseguiras por el camino mas corto,\nde lo contrario seguiras por el\ncamino mas largo.",["",""],["","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis."],["",""],["",""],["",""],["Llegaste a una casilla \"Espera\naqui\" (el numero dentro marca el\nnumero de turnos que perderas).",""],
					  ["","Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis."],["",""],["Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas).",""],"Llegaste a una casilla de guerra y\nte vez forzado a declararla.","¡¡Felicidades, haz ganado el juego!!","","","","","",""]
		self.turper=  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,[1,0],[0,0,0],[0,0,0],[1,0,0],[0,0,0],[2,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0],[0,0],[0,0],[0,0],1,0,0,0,0,0,[0,0],[0,0],[0,0],[2,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0],[0,0],[0,0],[2,0],[0,0],[0,0],[0,0],[1,2],[0,0],0,0,0,0,0,0,0,2,0,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0],[0,0],[0,0],[4,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0]
		self.carticla=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,[0,1],[0,0,0],[0,0,1],[0,0,0],[0,0,1],[0,0,0],[0,1,0],[0,0,0],[0,1,0],[0,0],[1,0],[0,0],[0,0],0,0,0,0,0,1,[0,0],[1,0],[0,0],[0,0],[0,0],[0,1],[0,0],0,0,0,0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,1,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0]
		self.espera2=0
		self.paisaje1.place(x=1050,y=1050)
	def velocidad(self,a):
		self.turno[self.numturno][10]=a
		self.velo1.configure(bg="white")
		self.velo2.configure(bg="white")
		self.velo3.configure(bg="white")
		self.velo1.configure(state="normal")
		self.velo2.configure(state="normal")
		self.velo3.configure(state="normal")
		if a==1:
			self.velo1.configure(bg="khaki")
			self.velo1.configure(state="disabled")
		elif a==2:
			self.velo2.configure(bg="khaki")
			self.velo2.configure(state="disabled")
		else:
			self.velo3.configure(bg="khaki")
			self.velo3.configure(state="disabled")
	def tirar(self):#btn, x, y, tur.per, carril, posi, mache, bruju, segun.cla, paz, velo
		#111 paz, 119 y 127 guerra, reunion 124
		#35-67-89-109-124-134-139
		self.intento.configure(state="disabled")
		self.intento.configure(bg="khaki")
		self.lbl1.configure(bg="white")
		self.lbl2.configure(bg="white")
		self.lbl3.configure(bg="white")
		self.lbl4.configure(bg="white")
		self.lbl5.configure(bg="white")
		self.lbl6.configure(bg="white")
		self.mensaje.configure(text="")
		self.giros=random.randrange(12,123)
		self.movimientos=self.giros%6
		if self.movimientos==0:
			self.movimientos+=6
		self.espera2=3.5-self.movimientos/2
		self.espera=.032786885/self.giros*122
		if self.turno[self.numturno][3]:
			self.turno[self.numturno][3]-=1
			if self.turno[self.numturno][3]>1:
				self.mensaje.configure(text="  Pierdes tu turno.\n    Te faltan "+str(self.turno[self.numturno][3])+" turnos por perder.")
			elif self.turno[self.numturno][3]==1:
				self.mensaje.configure(text="   Pierdes tu turno.\n      Te falta 1 turno por perder.")
			else:
				self.mensaje.configure(text="Pierdes tu turno.\nEn el siguiente ya te podras mover.")
			self.lbl1.configure(bg="red")
			self.lbl2.configure(bg="red")
			self.lbl3.configure(bg="red")
			self.lbl4.configure(bg="red")
			self.lbl5.configure(bg="red")
			self.lbl6.configure(bg="red")
			self.ventana2.update()
			time.sleep(3/self.turno[self.numturno][10])
			self.espera2=self.espera=self.movimientos=self.giros=0
		elif self.turno[self.numturno][5]==124:
			self.ultimo=True
			for i in range(0,self.a):
				if self.numturno!=i and self.turno[i][5]<self.turno[self.numturno][5]:
					self.ultimo=False;break
			if self.ultimo==False:
				self.mensaje.configure(text=self.mensajes[124])
				self.lbl1.configure(bg="red")
				self.lbl2.configure(bg="red")
				self.lbl3.configure(bg="red")
				self.lbl4.configure(bg="red")
				self.lbl5.configure(bg="red")
				self.lbl6.configure(bg="red")
				self.ventana2.update()
				time.sleep(3/self.turno[self.numturno][10])
				self.espera2=self.espera=self.movimientos=self.giros=0
		while(self.giros>0):
			self.op()
		acturno=self.turno[self.numturno][5]
		movi=self.movimientos
		cari=self.turno[self.numturno][4]
		corx=self.turno[self.numturno][1]
		cory=self.turno[self.numturno][2]
		while(movi):
			if len(self.casi[acturno])<len(self.casi[acturno+1]) and movi==self.movimientos:
				if acturno!=25 and acturno!=43 and acturno!=81 and self.turno[self.numturno][7]==0 and self.movimientos%2==0:
					cari+=1
				elif (acturno==43 or acturno==81) and self.turno[self.numturno][8]==0 and self.turno[self.numturno][7]==0:
					cari+=1
				elif acturno==25 and cari==2 and (self.turno[self.numturno][8] or self.turno[self.numturno][7]):
					cari+=1
			movi-=1
			acturno+=1
			corx+=self.casi[acturno][(cari-1)*2]
			cory+=self.casi[acturno][(cari-1)*2+1]
			if(corx>=self.limx and corx<self.limx+40 and cory>=self.limy and cory<self.limy+40):
				movi=0
			if len(self.casi[acturno])<len(self.casi[acturno+1]) and movi:
				if acturno!=25 and acturno!=43 and acturno!=81 and self.turno[self.numturno][7]==0 and self.movimientos%2==0:
					cari+=1
				elif (acturno==43 or acturno==81) and self.turno[self.numturno][8]==0 and self.turno[self.numturno][7]==0:
					cari+=1
				elif acturno==25 and cari==2 and (self.turno[self.numturno][8] or self.turno[self.numturno][7]):
					cari+=1
			elif len(self.casi[acturno])>len(self.casi[acturno+1]) and len(self.casi[acturno])/2==cari:
				acturno+=self.casi[acturno][cari*2-1]
				cari=1
		if self.espera:
			if len(self.casi[acturno])==2:
				self.mensaje.configure(text=self.mensajes[acturno])
				self.turno[self.numturno][3]+=self.turper[acturno]
				self.turno[self.numturno][8]+=self.carticla[acturno]
			else:
				self.mensaje.configure(text=self.mensajes[acturno][cari-1])
				self.turno[self.numturno][3]+=self.turper[acturno][cari-1]
				self.turno[self.numturno][8]+=self.carticla[acturno][cari-1]
			if acturno==1:
				self.turno[self.numturno][7]=1
			elif acturno==111:
				self.turno[self.numturno][9]=1
			elif self.turno[self.numturno][9]==1 and (acturno==119 or acturno==127 or acturno==138):
				self.mensaje.configure(text=self.mensaje.cget("text")+"\n(Pierdes un turno por haber roto\nla declaracion de paz).")
				self.turno[self.numturno][3]+=1
			elif acturno==124:
				self.ultimo=True
				for i in range(0,self.a):
					if self.numturno!=i and self.turno[i][5]<self.turno[self.numturno][5]:
						self.ultimo=False;break
				if self.ultimo==True:
					self.mensaje.configure(text=self.mensaje.cget("text")+"\n(Ya que eres el ultimo elemento,\nesto no te afecta).")
			elif self.mensaje.cget("text")=="Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis." or self.mensaje.cget("text")=="Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.":
				self.intento.place(x=91,y=600)
			elif corx>=self.limx and corx<self.limx+40 and cory>=self.limy and cory<self.limy+40:
				self.mensaje.configure(text="¡¡Felicidades, haz ganado el juego!!")
		self.ventana2.update()
		movi=self.movimientos
		while(self.movimientos):
			if len(self.casi[self.turno[self.numturno][5]])<len(self.casi[self.turno[self.numturno][5]+1]) and self.movimientos==movi:
				if self.turno[self.numturno][5]!=25 and self.turno[self.numturno][5]!=43 and self.turno[self.numturno][5]!=81 and self.turno[self.numturno][7]==0 and movi%2==0:
					self.turno[self.numturno][4]+=1
				elif (self.turno[self.numturno][5]==43 or self.turno[self.numturno][5]==81) and self.turno[self.numturno][8]==0 and self.turno[self.numturno][7]==0:
					self.turno[self.numturno][4]+=1
				elif self.turno[self.numturno][5]==25 and self.turno[self.numturno][4]==2 and (self.turno[self.numturno][8] or self.turno[self.numturno][7]):
					self.turno[self.numturno][4]+=1
			self.movimientos-=1
			self.turno[self.numturno][5]+=1
			if len(self.casi[self.turno[self.numturno][5]])>len(self.casi[self.turno[self.numturno][5]+1]) and len(self.casi[self.turno[self.numturno][5]])/2==self.turno[self.numturno][4]:
				self.turno[self.numturno][5]+=self.casi[self.turno[self.numturno][5]][self.turno[self.numturno][4]*2-1]
				self.turno[self.numturno][4]=1
			cari=self.casi[self.turno[self.numturno][5]][(self.turno[self.numturno][4]-1)*2]
			while(cari!=0):
				time.sleep(0.02/self.turno[self.numturno][10])
				if cari>0:
					cari-=1
					self.turno[self.numturno][1]+=1
				else:
					cari+=1
					self.turno[self.numturno][1]-=1
				self.turno[self.numturno][0].place(x=self.turno[self.numturno][1],y=self.turno[self.numturno][2])
				self.ventana2.update()
			cari=self.casi[self.turno[self.numturno][5]][(self.turno[self.numturno][4]-1)*2+1]
			while(cari!=0):
				time.sleep(0.02/self.turno[self.numturno][10])
				if cari>0:
					cari-=1
					self.turno[self.numturno][2]+=1
				else:
					cari+=1
					self.turno[self.numturno][2]-=1
				self.turno[self.numturno][0].place(x=self.turno[self.numturno][1],y=self.turno[self.numturno][2])
				self.ventana2.update()
			if(self.turno[self.numturno][1]>=self.limx and self.turno[self.numturno][1]<self.limx+40 and self.turno[self.numturno][2]>=self.limy and self.turno[self.numturno][2]<self.limy+40):
				self.movimientos=0
			if len(self.casi[self.turno[self.numturno][5]])<len(self.casi[self.turno[self.numturno][5]+1]) and self.movimientos:
				if self.turno[self.numturno][5]!=25 and self.turno[self.numturno][5]!=43 and self.turno[self.numturno][5]!=81 and self.turno[self.numturno][7]==0 and movi%2==0:
					self.turno[self.numturno][4]+=1
				elif (self.turno[self.numturno][5]==43 or self.turno[self.numturno][5]==81) and self.turno[self.numturno][8]==0 and self.turno[self.numturno][7]==0:
					self.turno[self.numturno][4]+=1
				elif self.turno[self.numturno][5]==25 and self.turno[self.numturno][4]==2 and (self.turno[self.numturno][8] or self.turno[self.numturno][7]):
					self.turno[self.numturno][4]+=1
		#btn, x, y, tur.per, carril, posi, mache, bruju, segun.cla, paz
		if self.turno[self.numturno][5]==19 or self.turno[self.numturno][5]==75 or self.turno[self.numturno][5]==96:
			self.mensaje.configure(text="")
			self.movimientos=2
			while(self.movimientos):
				self.movimientos-=1
				self.turno[self.numturno][5]+=1
				cari=self.casi[self.turno[self.numturno][5]][(self.turno[self.numturno][4]-1)*2]
				while(cari!=0):
					time.sleep(0.02/self.turno[self.numturno][10])
					if cari>0:
						cari-=1
						self.turno[self.numturno][1]+=1
					else:
						cari+=1
						self.turno[self.numturno][1]-=1
					self.turno[self.numturno][0].place(x=self.turno[self.numturno][1],y=self.turno[self.numturno][2])
					self.ventana2.update()
				cari=self.casi[self.turno[self.numturno][5]][(self.turno[self.numturno][4]-1)*2+1]
				while(cari!=0):
					time.sleep(0.02/self.turno[self.numturno][10])
					if cari>0:
						cari-=1
						self.turno[self.numturno][2]+=1
					else:
						cari+=1
						self.turno[self.numturno][2]-=1
					self.turno[self.numturno][0].place(x=self.turno[self.numturno][1],y=self.turno[self.numturno][2])
					self.ventana2.update()
		elif self.mensaje.cget("text")=="Estas en una zona altamente\npeligrosa (Retrocedes 2 casillas).":
			if self.turno[self.numturno][5]==113:
				self.turno[self.numturno][9]=1
				self.mensaje.configure(text="Haces una declaracion de paz (Si\ncaes en una casilla de guerra\npierdes un turno).")
			self.movimientos=2
			while(self.movimientos):
				self.movimientos-=1
				cari=self.casi[self.turno[self.numturno][5]][(self.turno[self.numturno][4]-1)*2]
				while(cari!=0):
					time.sleep(0.02/self.turno[self.numturno][10])
					if cari>0:
						cari-=1
						self.turno[self.numturno][1]-=1
					else:
						cari+=1
						self.turno[self.numturno][1]+=1
					self.turno[self.numturno][0].place(x=self.turno[self.numturno][1],y=self.turno[self.numturno][2])
					self.ventana2.update()
				cari=self.casi[self.turno[self.numturno][5]][(self.turno[self.numturno][4]-1)*2+1]
				while(cari!=0):
					time.sleep(0.02/self.turno[self.numturno][10])
					if cari>0:
						cari-=1
						self.turno[self.numturno][2]-=1
					else:
						cari+=1
						self.turno[self.numturno][2]+=1
					self.turno[self.numturno][0].place(x=self.turno[self.numturno][1],y=self.turno[self.numturno][2])
					self.ventana2.update()
				self.turno[self.numturno][5]-=1
		if self.mensaje.cget("text")=="Encontraste un baston de madera\n(El cual te ayudara a ir mas rapido)\noprime el boton para obtener un\nturno gratis.":
			self.intengratis.place(x=91,y=300)
			self.ventana2.update()
		elif self.mensaje.cget("text")=="Te topaste con un machete\noxidado, puedes escoger usarlo\nahora y conseguir un turno gratis o\nguardarlo para despues.":
			self.turno[self.numturno][6]=self.turno[self.numturno][6]+1
			self.usarmache.place(x=15,y=300)
			self.nousarmache.place(x=165,y=300)
			self.ventana2.update()
		elif self.turno[self.numturno][6]>0:
			self.intento.place(x=91,y=600)
			self.usarmache.place(x=15,y=140)
			self.nousarmache.place(x=165,y=140)
		elif self.turno[self.numturno][1]<self.limx or self.turno[self.numturno][1]>=self.limx+40 or self.turno[self.numturno][2]<self.limy or self.turno[self.numturno][2]>=self.limy+40: 
			self.fin()
	def siusar(self):
		self.turno[self.numturno][6]=self.turno[self.numturno][6]-1
		self.intento.place(x=91,y=140)
		self.nousarmache.place(x=91,y=600)
		self.usarmache.place(x=91,y=600)
		self.mensaje.configure(text="")
		self.ventana2.update()
		self.tirar()
	def nousar(self):
		self.nousarmache.configure(bg="khaki")
		self.nousarmache.configure(state="disabled")
		self.usarmache.configure(state="disabled")
		self.ventana2.update()
		self.fin()
		self.nousarmache.place(x=91,y=600)
		self.usarmache.place(x=91,y=600)
		self.nousarmache.configure(bg="white")
		self.usarmache.configure(state="normal")
		self.nousarmache.configure(state="normal")
		self.intento.place(x=91,y=140)
	def fin(self):
		time.sleep(self.espera2/self.turno[self.numturno][10])
		self.numturno=self.numturno+1
		if(self.a==self.numturno):
			self.numturno=0
		self.numcolor.configure(bg=self.colores[self.numturno])
		self.nickname.configure(text=self.elementos[self.numturno].get())
		self.lbl1.configure(bg="white")
		self.lbl2.configure(bg="white")
		self.lbl3.configure(bg="white")
		self.lbl4.configure(bg="white")
		self.lbl5.configure(bg="white")
		self.lbl6.configure(bg="white")
		self.mensaje.configure(text="")
		self.velocidad(self.turno[self.numturno][10])
		self.intento.configure(bg="white")
		self.intento.configure(state="normal")
		self.ventana2.update()
		time.sleep(0.01)
	def tirarpremium(self):
		self.intengratis.place(x=91,y=600)
		self.intento.place(x=91,y=140)
		self.mensaje.configure(text="")
		self.ventana2.update()
		self.tirar()
	def op(self):
		if(self.giros>0):
			time.sleep(self.espera/self.turno[self.numturno][10])
			self.lbl6.configure(bg="white")
			self.lbl1.configure(bg="khaki")
			self.ventana2.update()
			self.giros=self.giros-1
		if(self.giros>0):
			time.sleep(self.espera/self.turno[self.numturno][10])
			self.lbl1.configure(bg="white")
			self.lbl2.configure(bg="khaki")
			self.ventana2.update()
			self.giros=self.giros-1
		if(self.giros>0):
			time.sleep(self.espera/self.turno[self.numturno][10])
			self.lbl2.configure(bg="white")
			self.lbl3.configure(bg="khaki")
			self.ventana2.update()
			self.giros=self.giros-1
		if(self.giros>0):
			time.sleep(self.espera/self.turno[self.numturno][10])
			self.lbl3.configure(bg="white")
			self.lbl4.configure(bg="khaki")
			self.ventana2.update()
			self.giros=self.giros-1
		if(self.giros>0):
			time.sleep(self.espera/self.turno[self.numturno][10])
			self.lbl4.configure(bg="white")
			self.lbl5.configure(bg="khaki")
			self.ventana2.update()
			self.giros=self.giros-1
		if(self.giros>0):
			time.sleep(self.espera/self.turno[self.numturno][10])
			self.lbl5.configure(bg="white")
			self.lbl6.configure(bg="khaki")
			self.ventana2.update()
			self.giros=self.giros-1

objeto=CaminataScout()
"""
a.datas+=[(".imagenes/bosque1.png", "bosque1.png", "DATA"),
(".imagenes/cs46.png", "cs46.png", "DATA"),
(".imagenes/cs9b.png", "cs9b.png", "DATA"),
(".imagenes/cs17.png", "cs17.png", "DATA"),
(".imagenes/cs45.png", "cs45.png", "DATA"),
(".imagenes/cs47.png", "cs47.png", "DATA"),
(".imagenes/cs48.png", "cs48.png", "DATA"),
(".imagenes/cs28.png", "cs28.png", "DATA"),
(".imagenes/cs49.png", "cs49.png", "DATA"),
(".imagenes/cs51.png", "cs51.png", "DATA"),
(".imagenes/cs42.png", "cs42.png", "DATA"),
(".imagenes/cs52.png", "cs52.png", "DATA"),
(".imagenes/cs44.png", "cs44.png", "DATA"),
(".imagenes/cs9.png", "cs9.png", "DATA"),
(".imagenes/cs53.png", "cs53.png", "DATA"),
(".imagenes/cs54.png", "cs54.png", "DATA"),
(".imagenes/cs55.png", "cs55.png", "DATA"),
(".imagenes/cs34.png", "cs34.png", "DATA"),
(".imagenes/cs56.png", "cs56.png", "DATA"),
(".imagenes/cs40.png", "cs40.png", "DATA"),
(".imagenes/cs26.png", "cs26.png", "DATA"),
(".imagenes/cs30.png", "cs30.png", "DATA"),
(".imagenes/cs57.png", "cs57.png", "DATA"),
(".imagenes/cs13.png", "cs13.png", "DATA"),
(".imagenes/cs15.png", "cs15.png", "DATA"),
(".imagenes/cs27.png", "cs27.png", "DATA"),
(".imagenes/cs21.png", "cs21.png", "DATA"),
(".imagenes/cs36.png", "cs36.png", "DATA"),
(".imagenes/cs38.png", "cs38.png", "DATA"),
(".imagenes/cs58.png", "cs58.png", "DATA"),
(".imagenes/cs59.png", "cs59.png", "DATA"),
(".imagenes/cs32.png", "cs32.png", "DATA"),
(".imagenes/cs11.png", "cs11.png", "DATA"),
(".imagenes/cs25.png", "cs25.png", "DATA"),
(".imagenes/cs21b.png", "cs21b.png", "DATA"),
(".imagenes/cs19b.png", "cs19b.png", "DATA"),
(".imagenes/cs23.png", "cs23.png", "DATA"),
(".imagenes/cs3.png", "cs3.png", "DATA"),
(".imagenes/cs50.png", "cs50.png", "DATA"),
(".imagenes/paisaje1.png", "paisaje1.png", "DATA"),
(".imagenes/sco1.png", "sco1.png", "DATA"),
(".imagenes/sco2.png", "sco2.png", "DATA"),
(".imagenes/sco3.png", "sco3.png", "DATA"),
(".imagenes/sco4.png", "sco4.png", "DATA"),
(".imagenes/sco5.png", "sco5.png", "DATA"),
(".imagenes/sco6.png", "sco6.png", "DATA"),
(".imagenes/sco7.png", "sco7.png", "DATA"),
(".imagenes/sco8.png", "sco8.png", "DATA"),
(".imagenes/venado.ico", "venado.ico", "DATA"),
(".imagenes/leon.ico", "leon.ico", "DATA")]

if os.path.isdir('.imagenes/ImagenesOGSLCaminataScoutBBSVProgramacion')==False:
	estacompleto=False
elif os.path.isfile('.imagenes/bosque1.png')==False:
	estacompleto=False

if os.path.isdir('imagenes')==False:
	os.mkdir('imagenes')
	shutil.copy('.imagenes/bosque1.png','.imagenes/imagenes/bosque1.png')
#reine jesus por siempre, reine su corazón, porque nuestra patria y nuestro suelo, es de maria la nación"""
