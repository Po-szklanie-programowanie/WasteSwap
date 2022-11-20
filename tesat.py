import streamlit as st
import psycopg2 as pcg



connection = pcg.connect(database="po_szklanie_programowanie",
        user='postgres', password='poszklanie',
        host='::1',port='5432')

def database_reverse_lookup(name, packaging, category):

    splited = str(category).split(sep=',')
    if packaging == 'Paper':
        st.title('wow thats best packaging')
    elif packaging == 'Glass':
            cursor = connection.cursor()

            better_than_plastic = f'''
        
            SELECT * FROM products WHERE packaging = 'Paper' 

            '''

            cursor.execute(better_than_plastic)
            rows = cursor.fetchall()
            if len(rows) > 0:
                st.title("Better packaging options:")
                for row in rows:
                    categories = row[4]
                    db_splited = categories.split(',')
                    inter = list(set(splited).intersection(db_splited))
                    if len(inter) >= 2:
                        id = row[0]
                        product_name = row[1]
                        product_packaging = row[2]
                        company = row[3]
                        st.write(f'company: {company}')
                        st.write(f'name of product: {product_name}')
                        st.write(f'packaging of product:{product_packaging}')
            else:
                st.title("Sorry right now we don't have anything with better packaging")
                
                
            cursor.close()

    elif packaging == 'Metal':
        
            cursor = connection.cursor()

            better_than_plastic = f'''
        
            SELECT * FROM products WHERE (packaging = 'Glass' OR packaging = 'Paper') 

            '''

            cursor.execute(better_than_plastic)
            rows = cursor.fetchall()

            if len(rows) > 0:
                st.title("Better packaging options:")
                for row in rows:
                    categories = row[4]
                    db_splited = categories.split(',')
                    inter = list(set(splited).intersection(db_splited))
                    if len(inter) >= 2:
                        id = row[0]
                        product_name = row[1]
                        product_packaging = row[2]
                        company = row[3]
                        st.write(f'company: {company}')
                        st.write(f'name of product: {product_name}')
                        st.write(f'packaging of product:{product_packaging}')
            else:
                st.write("Sorry right now we don't have anything with better packaging")
                
                
            cursor.close()


    else:

            cursor = connection.cursor()

            better_than_plastic = f'''
        
            SELECT * FROM products WHERE (packaging = 'Metal' OR packaging = 'Glass' OR packaging = 'Paper') 

            '''

            cursor.execute(better_than_plastic)
            rows = cursor.fetchall()

            if len(rows) > 0:
                st.title("Better packaging options:")
                for row in rows:
                    categories = row[4]
                    db_splited = categories.split(',')
                    inter = list(set(splited).intersection(db_splited))
                    if len(inter) >= 2:
                        id = row[0]
                        product_name = row[1]
                        product_packaging = row[2]
                        company = row[3]
                        st.write(f'company: {company}')
                        st.write(f'name of product: {product_name}')
                        st.write(f'packaging of product:{product_packaging}')
            else:
                st.write("Sorry right now we don't have anything with better packaging")
                
                
            cursor.close()
    connection.close()



def database_lookup():
    if text:

        cursor = connection.cursor()
    
        select_data_by_text = '''
        SELECT DISTINCT * FROM products WHERE product_name LIKE INITCAP('%{}%');
        '''.format(text)

        cursor.execute(select_data_by_text)
        rows = cursor.fetchall()
        for i, row in enumerate(rows):
            id = row[0]
            name = row[1]
            packaging = row[2]
            company = row[3]
            categories = row[4]
            st.write(f'company: {company}')
            st.write(f'name of product: {name}')
            st.write(f'packaging of product:{packaging}')
            st.button('Click', key=f'button{i}' , on_click=database_reverse_lookup, args=(name, packaging, categories,))

            cursor.close()
            connection.close()
    else:
        st.text("")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.title('WasteSwap')

    text = st.text_input('Write a name of product which you desire')

    st.button(
        "Search",
        on_click=database_lookup
    )
