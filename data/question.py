import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT DATE_TRUNC('month', enrollment_date) AS month, COUNT(*) AS count FROM enrollments GROUP BY month ORDER BY month")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT DATE_PART('year', enrollment_date) AS year FROM enrollments")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(age) FROM students")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM courses')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students)')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT course_id, MIN(enrollment_date) AS first_enrollment FROM enrollments GROUP BY course_id')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data




def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, AVG(s.age) AS avg_age FROM enrollments e JOIN students s ON e.student_id = s.student_id JOIN courses c ON e.course_id = c.course_id GROUP BY c.course_name')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT MIN(age) AS min_age FROM students')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""SELECT c.course_name, COUNT(s.student_id) AS student_count FROM enrollments e JOIN students s ON e.student_id = s.student_id JOIN courses c ON e.course_id = c.course_id GROUP BY c.course_name""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""SELECT c.course_name, COUNT(s.student_id) AS student_count FROM enrollments e JOIN students s ON e.student_id = s.student_id JOIN courses c ON e.course_id = c.course_id GROUP BY c.course_name""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
