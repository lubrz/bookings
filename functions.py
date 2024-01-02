import datetime

today =  datetime.date.today()

print(today)

#Calcoliamo quanto terminano le 8 settimane disponibili oper effettuare la prenotazione:
end_of_res = today + datetime.timedelta(weeks=8)


todaylst = [today.day,today.month,today.year]

eor_lst = [end_of_res.day, end_of_res.month, end_of_res.year]

start = datetime.datetime(day=today.day,month= today.month,year=today.year)
end = datetime.datetime(day=end_of_res.day,month=end_of_res.month,year=end_of_res.year)

print(todaylst)

print(eor_lst)

def check_date(d,m,y):
    dlst = range(1,31)
    days_in_month = ["{}".format(x) for x in dlst]  #lista di caratteri da 1 a 31
    rday =str(d)
    if (m in [4,6,9,11]):
        #rday = input(("Return a correct day for the month entered 0{}: ").format(m))
        while (rday not in days_in_month):
            rday = input(("Return a correct day for the month entered 0{} between 1 and 30: ").format(m))
    elif m==2 and y%4 == 0:
        #rday = input(("PLease enter a correct day between 1 and 29 for the month entered 0{}-February: ").format(m))
        while (rday not in days_in_month[:-1]):
           rday = input(("PLease enter a correct day between 1 and 29 for the month entered 0{}-February: ").format(m))
    elif (m==2 and y%4 != 0):
        #rday = input(("PLease enter a correct day between 1 and 28 for the month entered 0{}-February: ").format(m))
        while (rday not in days_in_month[0:-2]):
            rday = input(("PLease enter a correct day between 1 and 28 for the month entered 0{}-February: ").format(m))   
    return int(rday)
        


def check_res_date(res_room,res_name, prenotazione):
    if start <= prenotazione <= end:
        print("La data della prenotazione e corretta!!")
        reservation = booking(res_room,res_name,prenotazione)
        return reservation
    else:
        print(("Per favore inserire una data compresa tra {}-{}-{} ed inferiore a {}-{}-{}").format(today.day,today.month,today.year,end_of_res.day, end_of_res.month, end_of_res.year))
    return 0

room1 = {
    'dates': [0],
    'names': ['A'],
    'rcode': ['C'],
    'price': 295
}

room2 = {
    'dates': [0],
    'names': ['A'],
    'rcode': ['C'],
    'price': 295
}

room3 = {
    'dates': [0],
    'names': ['A'],
    'rcode': ['C'],
    'price': 295
}

def booking(room, name, rdate):
    if room == 1:
        if rdate in room1['dates']:
            print("Mi dispiace la stanza 1 non é disponibile per il GMA, scegliere un'altra data o giorno")
            return 0
        else:
            res = addbooking(room, name, rdate)
    elif room == 2:
        if rdate in room2['dates']:
            print("Mi dispiace la stanza 2 non é disponibile per il GMA, scegliere un'altra data o giorno")
            return 0
        else:
           res = addbooking(room, name, rdate)
    elif room == 3:
        if rdate in room3['dates']:
            print("Mi dispiace la stanza 1 non é disponibile per il GMA, scegliere un'altra data o giorno")
            return 0
        else:
           res = addbooking(room, name, rdate)
    return res

def addbooking(n, name, rdate):
    print(rdate)
    print(name)
    print(n)
    r='room'+str(n)
    r['dates'].append(rdate)
    r['names'].append(name)
    r['code'].append(name+rdate+"R0"+str(n))
    
    rcode = name+str(rdate)+"R0"+str(n)
    price = r['price']
    return rcode,price