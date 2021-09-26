import telnyx
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",passwd="antrug0s-98.",database="tadhack")
cursor =db.cursor()
cursor.execute("SELECT phone FROM coffeeGrower WHERE active = 1")
r = cursor.fetchall()

def run(msm):
    #Telnyx API
    telnyx.api_key = "KEY017C1EEA1E2FF76222DF1C06B3171859_absHb0Pc3bsuRBT9r2Pq5m"
    for phone in r:
        resp = telnyx.Message.create(
            from_= "+13054141964",
            to = phone,
            text = msm

        )

if __name__ == '__main__':
    msm = input('Ingrese el mensaje que desea enviar: ')
    run(msm)
