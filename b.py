from connect import get_connection


def insert_student(sno, sname, sage, sgender, sdept):

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        check_sql = "SELECT sno FROM student WHERE sno = %s;"
        cur.execute(check_sql, (sno,))
        if cur.fetchone():
            print(f"sno {sno} Already exists, please re-enter.")
            return
        
        insert_sql = """
            INSERT INTO student (sno, sname, sage, sgender, sdept)
            VALUES (%s, %s, %s, %s, %s);
        """
        cur.execute(insert_sql, (sno, sname, sage, sgender, sdept))
        conn.commit()
        print("Insert New Student Success！")
    except Exception as e:
        conn.rollback()
        print("insertion failure:", e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    insert_student("20200005", "Alice", 19, "F", "CS")
