import datetime
import sys
from setup import *
from functions import *
from tabulate import tabulate

today =  datetime.date.today()

print(today)

#Calcoliamo quanto terminano le 8 settimane disponibili oper effettuare la prenotazione:
end_of_res = today + datetime.timedelta(weeks=8)


#Parte un ciclo WHILE princile

while True:

    #Stampiamo su schermo il messaggio per informare che sono disponibili prenotazioni fino a end_of_res

    print("Grazie per utilizzare il  sistema di riservazioni di Seaview Castle Visitor Center.\nThe have abailable one large room that can be ussed for a variety of activities such as showing films, holding presentatiopns, displaying\nexhibitions or wedding reception. We also offer two smaller rooms.\n\nEach room can be booked by the day according to the following tariff:\n") 

    #Creiamo lista con le info delle 3 stanze
    
    rooms = [[1,"Large","$295"],[2,"Small1","$175"],[3,"Small2","$150"]]

    #Qui utilizziamo laibreria Tabulate per mostrare le 3 opzioni in tabella piu leggibile

    print(tabulate(rooms,headers=["Room N.","Type of Room","Cost Per Night"],stralign="center",numalign="center"))

    print(("\nAl momento sono aperte le prenotazioni fino al giorno:  {}-{}-{} (FORMAT: DD-MM-YY)\n").format(end_of_res.day,end_of_res.month,end_of_res.year))

    #inserire nome x prenotazione
    res_name = input("Inserisci il nome x la prenotazione: \n")

    #Selezionare la stanza da prenotare
    res_room = enter_room_number()

    #inserire il giorno e mese della prenotazione sono le funzioni che sono in Setup.PY
    res_day = enter_res_day()
    res_month = enter_res_month()

    #se tra 8 settimane siamo ancora nello stesso anno allora non chidediamo di inserire l'anno
    if today.year != end_of_res.year:
        res_year =input("Inserisci l'anno x la prenotazione: \n")
        res_day = check_date(res_day,res_month,res_year)
        #prenotazione = res_day+res_month+res_year
        prenotazione = datetime.datetime(day=res_day,month=res_month, year=res_year)

    else:
        res_day = check_date(res_day,res_month,today.year)
        prenotazione = datetime.datetime(day=res_day,month=res_month, year=today.year)

    #prenotazione = datetime.datetime(day=res_day,month=res_month, year=today.year)

    res_date = check_res_date(res_room,res_name,prenotazione)

    #print(("La tua prenotazione e per il giorno {} del mese di {} dell'anno {}").format(res_day,res_month,today.year))
    userInput = input("\nThank you for using our booking system.\n\nPLease press 'R' to restart or 'X' to exit\n").capitalize()

    if userInput == "X" or userInput!= "R":
        print('Goodbye.')
        sys.exit(-1) # exits the program