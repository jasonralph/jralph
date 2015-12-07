from mysql import connector
import sys
import optparse


parser = optparse.OptionParser()
parser.add_option('--id', action="store", help="Enter ID number", type="int")
options, args = parser.parse_args()


try:
    cnx = connector.Connect(user='jason',
                        password='trace3',
                        database='jason',
                        host='localhost')
except connector.Error as err:
    print "Connection to Database Failed"
    print err
    sys.exit(1)




cursor = cnx.cursor()
query = "SELECT * from employee WHERE id='%s'" % options.id
cursor.execute(query)
for row in cursor:
    print row