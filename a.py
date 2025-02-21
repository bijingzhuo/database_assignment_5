from connect import get_connection


def read_student(sno):

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()

        sql = "SELECT * FROM student WHERE sno = %s;"
        cur.execute(sql, (sno,))
        student = cur.fetchone()
        if student:
            print("result:")
            print(f"sno: {student[0]}, sname: {student[1]}, sage: {student[2]}, sgender: {student[3]}, sdept: {student[4]}")
        else:
            print("No record of the student was found.")
    except Exception as e:
        print("Query Error:", e)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    read_student("20200001")
