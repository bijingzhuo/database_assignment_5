import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",     
            user="postgres",       
            password="252436710",    
            host="localhost",         
            port="5432"                  
        )
        return conn
    except Exception as e:
        print("Database connection failure:", e)
        return None


if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("Database connection successful！")
        conn.close()
