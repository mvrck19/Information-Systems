from pyfirmata import Arduino, util
import mysql.connector
import time

board = Arduino('/dev/ttyUSB0')

led_pin = 11

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="csuth2018"
)
cursor = db.cursor()
while True:
    time.sleep(1)

    cursor.execute("SELECT * FROM items WHERE avail<'10'")
    if cursor.fetchone() is not None:
        board.digital[led_pin].write(1)
    else:
        board.digital[led_pin].write(0)
    cursor.reset()
cursor.close()