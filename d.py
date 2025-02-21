from connect import get_connection

def delete_student(sno):

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        check_sql = "SELECT * FROM sc WHERE sno = %s;"
        cur.execute(check_sql, (sno,))
        enrollments = cur.fetchall()
        
        if enrollments:
            delete_sc_sql = "DELETE FROM sc WHERE sno = %s;"
            cur.execute(delete_sc_sql, (sno,))
            print(f"Deleted the course record of student number {sno}.")
        
        delete_student_sql = "DELETE FROM student WHERE sno = %s;"
        cur.execute(delete_student_sql, (sno,))
        conn.commit()
        print(f"sno {sno} The student records have been deleted.")
    except Exception as e:
        conn.rollback()
        print("Failed to delete:", e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    delete_student("20200003")
