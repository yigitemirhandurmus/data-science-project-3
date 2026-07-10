import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);
""")

cur.execute("""
ALTER TABLE students
ADD COLUMN IF NOT EXISTS city VARCHAR(50);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    category VARCHAR(50)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    enrollment_date DATE
);
""")


cur.execute("""
INSERT INTO students (first_name, last_name, age, city) VALUES
('Ali', 'Yılmaz', 21, 'İstanbul'),
('Ayşe', 'Demir', 23, 'Ankara'),
('Mehmet', 'Kaya', 25, 'İzmir'),
('Zeynep', 'Çelik', 22, 'Bursa'),
('Can', 'Öztürk', 24, 'Antalya');
""")

cur.execute("""
INSERT INTO courses (course_name, category) VALUES
('Veritabanı Temelleri', 'Veritabanı'),
('İleri SQL', 'Veritabanı'),
('Python Programlama', 'Yazılım'),
('Web Geliştirme', 'Yazılım');
""")

cur.execute("""
INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2023-01-10'),
(1, 2, '2023-03-12'),
(2, 1, '2023-02-01'),
(3, 3, '2023-04-15'),
(4, 1, '2023-05-10'),
(5, 4, '2023-06-20');
""")


conn.commit()
cur.close()
conn.close()
