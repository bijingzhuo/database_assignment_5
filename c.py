from connect import get_connection


def update_student(sno, new_name, new_age, new_gender, new_dept):

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()

        select_sql = "SELECT * FROM student WHERE sno = %s;"
        cur.execute(select_sql, (sno,))
        old_record = cur.fetchone()
        if not old_record:
            print(f"sno {sno} Doesn't exist, can't update。")
            return
        
        print("source:", old_record)
        

        update_sql = """
            UPDATE student
            SET sname = %s,
                sage = %s,
                sgender = %s,
                sdept = %s
            WHERE sno = %s;
        """
        cur.execute(update_sql, (new_name, new_age, new_gender, new_dept, sno))
        conn.commit()
        
        cur.execute(select_sql, (sno,))
        updated_record = cur.fetchone()
        print("Updated information:", updated_record)
    except Exception as e:
        conn.rollback()
        print("update failure:", e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    update_student("20200005", "Alicia", 20, "F", "MA")
