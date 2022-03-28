import mysql.connector

mydb = mysql.connector.connect(
    host="HOST_IP_ADDRESS",
    port="SERVER_PORT",
    user="DB_USER",
    password="USER_PASSWORD",
    database="DB_NAME"
)

mycursor = mydb.cursor()

mydict = mydb.cursor()

def find_client(cnpj):
    mycursor.execute("SELECT code FROM clients WHERE cnpj= '%s';" % (cnpj))
    myresult = mycursor.fetchone()
    for client in myresult:
        code = client
    return code