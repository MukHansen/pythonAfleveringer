import datetime
import pymysql
import pandas as pd
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly


#  This Works
# cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='3rdSemExam')  

# cursor = cnx.cursor()

# query = ("SELECT firstname, lastname, id FROM DRIVER")

# # hire_start = datetime.date(1960, 1, 1)
# # hire_end = datetime.date(2004, 12, 31)

# # cursor.execute(query, (hire_start, hire_end))
# cursor.execute(query)

# for (firstname, lastname, id) in cursor:
#   print("Name {} {} ---- ID {}".format(firstname, lastname, id))

# cursor.close()
# cnx.close()

#  This Works
# cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='pythonTest')

# cursor = cnx.cursor()

# query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo WHERE startdate BETWEEN %s AND %s")

# hire_start = datetime.date(1960, 1, 1)
# hire_end = datetime.date(2004, 12, 31)

# cursor.execute(query, (hire_start, hire_end))

# for (firstname, lastname, startdate, enddate, salary) in cursor:
#     print("{} {} hired from {} to {} is paid: {} DKR pr month".format(firstname, lastname, startdate, enddate, salary))

# cursor.close()
# cnx.close()

# ---------------------------------------------------------------------------------------------------------------------
# cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='pythonTest')
# cursor = cnx.cursor()

# add_person = ("INSERT INTO %s "
#               "(personId, firstName, lastName) "
#               "VALUES (%(personId)s, %(firstName)s, %(lastName)s)")


# table = "person"
# myDict = {"personId": 111, "firstName": "John", "lastName": "Johnson"}

# cursor.execute(add_person, (table, list(myDict.values())))
# cnx.commit()

# cursor.close()
# cnx.close()

# cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='pythonTest')
# df = pd.read_sql('SELECT * FROM pythondemo', con=cnx)
# print(df)
# -----------------------------------------------------------------------------------------------------


#cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 
con_str = 'mysql+pymysql://dev:ax2@localhost:3307/pythonTest'
engine = create_engine(con_str)
df = pd.read_csv('cars.csv')
df.to_sql('cars2',con=engine, if_exists='append', index = False)