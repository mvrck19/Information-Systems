# Information-Systems
**Setup**
> - Θα πρέπει να δημιουργηθεί μια βάση MySQL με τα εξής στοιχεία :
>   host="localhost"
>   user="root"
>   passwd=""
>   database="storedb"
> - Θα πρέπει να εκτελεστεί το dump.sql για τη δημιουργία των αντικειμένων στη βάση.
> - Θα πρέπει να εγκατασταθούν μέσω pip οι εξής βιβλιοθήκες :
>   [pyfirmata](https://pypi.org/project/pyFirmata/)
>   [mysql-connector](https://pypi.org/project/mysql-connector/)
> - Θα πρέπει στη γραμμή 5 του python script να μπει το port που είναι συνδεδεμένο το Arduino
```
board = Arduino('/dev/ttyUSB0')
```
>   αντικαθιστώντας το '/dev/ttyUSB0'.
> - Οδηγίες για το πως να βρείτε το port [εδώ](https://www.swarthmore.edu/NatSci/echeeve1/Class/E02/Lab01/PortID.html)
**Usage**
>   Στη σελίδα index υπάρχουν δύο link, κάθε ένα απ' αυτά αντιστοιχεί σε ένα αντικείμενο στη     βάση δεδομένων. Κάθε φορά που ένας χρήστης πατάει το ένα από τα δύο link η μεταβλητή         avail του αντίστοιχου αντικείμενου στη βάση μειώνεται κατά 1.Όταν το main.py εκτελεστεί      ένα από τα δυο λαμπάκια που είναι συνδεδεμένα στις ψηφιακές εξόδους 7 και 8 θα ανάψει        συμβολίζοντας αν η μεταβλητή avail είναι μεγαλύτερή η μικρότερή από 5.
