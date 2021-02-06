# prenotabot

ISTRUZIONI PER PRENOTARE


1) Salvare in una cartella prenotapy.py


2) Aprire Qt-console/Spider/quello che preferite, entrate nella cartella dove si trova il 
   file e lanciarlo


3) Caricare la pagina delle prenotazioni dell'aula studio che preferisci scrivendo:

	aulastudio = apri_pagina(aula_studio)

  i codici sono:
	
	'PC'	Pacinotti
	'FB'	Fibonacci
	'RC'	Ricci
	'PN'	Porta Nuova
	'PG'	Piagge

  Esempio. Per aprire la pagina delle prenotazioni del Pacinotti scrivo:

	pacinotti = apri_pagina('PC') 


4) Inserire le proprie credenziali di ateneo nella pagina aperta


A questo punto si può scegliere una delle seguenti:

a) Per prenotare alla mattina: scrivere 

	prenota_mattina(aulastudio, giorno)

  I codici per giorno sono:

	0	lunedì
	2	martedì
	4	mercoledì
	6	giovedì
	8	venerdì
	10	sabato
	11	domenica

   Esempio (continuazione). Voglio prenotare giovedì al Pacinotti, scrivo:

	prenota_mattina(pacinotti, 6)

   Questa routine va fatta partire la sera prima (o quanto meno prima delle 8:30) e NON 
   bisogna fare andare in stop il computer.

b) Questa routine prenota un posto quando si libera. 

	trova_posto(aulastudio, giorno, slot)

   I codici per giorno sono quelli di sopra, slot può essere 0 oppure 1 a seconda che si 
   cerchi un posto la mattina o il pomeriggio rispettivamente.

   Esempio (continuazione). Voglio trovare un posto giovedì pomeriggio al pacinotti, scrivo:

	 trova_posto(pacinotti, 6, 1)

	
