import datetime

today =  datetime.date.today()

print(today)

#Calcoliamo quanto terminano le 8 settimane disponibili oper effettuare la prenotazione:
end_of_res = today + datetime.timedelta(weeks=8)


def enter_room_number():

    #usiamo una Tuple con i 3 possibili valori
    rooms = ("1","2","3")

    room = input("Inserisci il numero associato alla stanza x la prenotazione [1-Large, 2-Small1, 3-Small2]: \n")

    #Ciclo While per far inserire giorno
    while room not in rooms:
        room = input("Please enter a valid room number [1- Large, 2- Small1, 3- Small2]: \n")
    return int(room)


def enter_date():
    enter_res_day()
    enter_res_month()

def enter_res_day():
    dlst = range(1,32)
    days_in_month = ["{}".format(x) for x in dlst]
    #print(days_in_month)
    rday = input("Inserisci il giorno x la prenotazione: \n")
    print(type(rday))
    #Ciclo While per far inserire giorno
    while rday not in days_in_month:
        rday = input("Please enter a valid day number [1-31]: \n")
    return int(rday)

#res_day = enter_res_day()

def enter_res_month():
    today =  datetime.date.today()
    mlst = range(1,13)
    months_in_year = ["{}".format(x) for x in mlst]
    rmonth = input("Inserisci il mese x la prenotazione: \n")
    #print(type(rmonth))
    #Ciclo While per inserire Mese
    while rmonth not in months_in_year:
        rmonth = input("Please enter a valid month number [1-12]: \n")
    return int(rmonth)

#res_month = enter_res_month()

