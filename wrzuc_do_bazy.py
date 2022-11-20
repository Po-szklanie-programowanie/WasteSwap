import psycopg2

connection = psycopg2.connect(database="po_szklanie_programowanie",
                              user='postgres', password='poszklanie',
                              host='::1',port='5432') #data to connect to database on postgressql

cursor = connection.cursor()

connection.autocommit = True
crt_table_sql = '''CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    packaging VARCHAR(255),
    company VARCHAR(255),
    categories VARCHAR(255)
);
'''
cursor.execute(crt_table_sql)


csv_sql = '''COPY products(product_name,
    packaging,company,categories)
    FROM 'C:\\Users\\kub20\\Documents\\GitHub\\WasteSwap\\data\\food_products.csv' 
    DELIMITER ';'
    CSV HEADER;
'''
# on FROM put path to csv file with data
cursor.execute(csv_sql)

connection.commit()
cursor.close()
connection.close()
