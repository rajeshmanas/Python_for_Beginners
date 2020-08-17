import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Keerthana@1585',
    database='sql_store'
)

mycursor = mydb.cursor()

# Table name is 'Customers' in the database 'Sql_Store' having following data,copied the data for your easy understanding

# customer_id	first_name	last_name	birth_date	phone	address	city	state	points
# 1	Babara	MacCaffrey	1986-03-28	781-932-9754	0 Sage Terrace	Waltham	MA	7868
# 2	Ines	Brushfield	1986-04-13	804-427-9456	14187 Commercial Trail	Hampton	VA	947
# 3	Freddi	Boagey	1985-02-07	719-724-7869	251 Springs Junction	Colorado Springs	CO	2967
# 4	Ambur	Roseburgh	1974-04-14	407-231-8017	30 Arapahoe Terrace	Orlando	FL	457
# 5	Clemmie	Betchley	1973-11-07	NULL	5 Spohn Circle	Arlington	TX	3675
# 6	Elka	Twiddell	1991-09-04	312-480-8498	7 Manley Drive	Chicago	IL	3073
# 7	Ilene	Dowson	1964-08-30	615-641-4759	50 Lillian Crossing	Nashville	TN	1672
# 8	Thacher	Naseby	1993-07-17	941-527-3977	538 Mosinee Center	Sarasota	FL	205
# 9	Romola	Rumgay	1992-05-23	559-181-3744	3520 Ohio Trail	Visalia	CA	1486
# 10	Levy	Mynett	1969-10-13	404-246-3370	68 Lawn Avenue	Atlanta	GA	796

print('Enter the name you want to fetch from the table:')
name = [input()]

sql = 'select * from customers where first_name = %s'

mycursor.execute(sql, name)

result = mycursor.fetchall()

if result:
    for i in result:
        print(i)
else:
    print('No data')
