import sys
import json
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

leer = json.loads(open(sys.argv[1]).read())
fechaCreacion = leer['fechaCreacion']
fechaFin = leer['fechaFin']
generadosGDD = leer['fechas']
fcdate = datetime.strptime(fechaCreacion, '%Y-%m-%d')
fcmonth = fcdate.month
fcfaltantes = 12 - int(fcmonth)
indice = 1
datelost = []
lostresult = []

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

fcInit = fechaCreacion.split("-")
fcFin = fechaFin.split("-")

start_date = date(int(fcInit[0]), int(fcInit[1]), int(fcInit[2]))
end_date = date(int(fcFin[0]), int(fcFin[1]), int(fcFin[2]))
for single_date in daterange(start_date, end_date):
    if str(single_date)[8:] == '01':
        datelost.append(single_date.strftime("%Y-%m-%d"))

for d in datelost:
    if d not in generadosGDD and fechaCreacion != d  :
        lostresult.append(d)

data = {
    "id":leer["id"],
    "fechaCreacion":leer['fechaCreacion'],
    "fechaFin":leer['fechaFin'],
    "fechasFaltantes": lostresult
}

print("¡Archivo: ", sys.argv[2], " creado con exito!")
with open(sys.argv[2], 'w') as file:
    json.dump(data, file, indent=4)
