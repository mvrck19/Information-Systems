from pyfirmata import Arduino, util
import mysql.connector
import time

board = Arduino('/dev/ttyUSB0')

green_led = 8
blue_led = 7

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="storedb"
)
cursor = db.cursor()
while True:
    time.sleep(1)

    cursor.execute("SELECT * FROM items WHERE avail<'5'")
    if cursor.fetchone() is not None:
        board.digital[blue_led].write(1)
    else:
        board.digital[green_led].write(1)
    cursor.reset()
cursor.close()