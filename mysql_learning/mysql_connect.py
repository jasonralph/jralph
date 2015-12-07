from mysql import connector
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', action="store", help="Enter Job ID#", type="int")
parser.add_option('-n', action="store", help="Enter Employee Name", type="string")
parser.add_option('-d', action="store", help="Enter Department", type="string")
parser.add_option('-s', action="store", help="Enter Salary", type="int")
options, args = parser.parse_args()


def database_add(id, name, dept, salary):
    try:
        con = connector.Connect(user='jason',
                                password='trace3',
                                database='jason',
                                host='localhost')
        c = con.cursor()
        table_name = "employee"
        insert = "INSERT INTO " + table_name + " (id,name,dept,salary) \
        VALUES (%s, %s, %s, %s)"
        data_value = (id, name, dept, salary)
        c.execute(insert, data_value)
        con.commit()
        c.close()
        con.close()
    except:
        print('Can\'t connect to the database')


database_add(options.i, options.n, options.d, options.s)
