import datetime
from decimal import Decimal
import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.question import (
    question_1_query, question_2_query, question_3_query, question_4_query, question_5_query,
    question_6_query, question_7_query, question_8_query, question_9_query, question_10_query
)


def run_common_test(expected_data, tested_func):
    result = tested_func()
    assert result == expected_data


# Q1: DATE_TRUNC ay bazlı kayıt sayıları (month, count)
def test_question_1_query():
    result = question_1_query()
    assert len(result) == 6
    # Her ay 1 kayıt var
    assert all(r[1] == 1 for r in result)


# Q2: DATE_PART yıl bilgisi
def test_question_2_query():
    result = question_2_query()
    assert len(result) == 6
    assert all(r[0] == 2023.0 for r in result)


# Q3: SUM yaş = 115
def test_question_3_query():
    expected = [(115,)]
    run_common_test(expected, question_3_query)


# Q4: COUNT kurs sayısı = 4
def test_question_4_query():
    expected = [(4,)]
    run_common_test(expected, question_4_query)


# Q5: Yaşı ortalama yaştan (23) büyük olan öğrenciler
def test_question_5_query():
    expected = [
        (3, 'Mehmet', 'Kaya', 25, 'İzmir'),
        (5, 'Can', 'Öztürk', 24, 'Antalya'),
    ]
    run_common_test(expected, question_5_query)


# Q6: Her kursun en eski kayıt tarihi (course_id, first_enrollment)
def test_question_6_query():
    result = question_6_query()
    dates = {r[0]: r[1] for r in result}
    assert dates[1] == datetime.date(2023, 1, 10)
    assert dates[2] == datetime.date(2023, 3, 12)
    assert dates[3] == datetime.date(2023, 4, 15)
    assert dates[4] == datetime.date(2023, 6, 20)


# Q7: Kurs başına ortalama yaş (course_name, avg_age)
def test_question_7_query():
    result = question_7_query()
    avgs = {r[0]: r[1] for r in result}
    assert avgs['Veritabanı Temelleri'] == Decimal('22.0000000000000000')
    assert avgs['İleri SQL'] == Decimal('21.0000000000000000')
    assert avgs['Python Programlama'] == Decimal('25.0000000000000000')
    assert avgs['Web Geliştirme'] == Decimal('24.0000000000000000')


# Q8: En genç öğrencinin yaşı = 21
def test_question_8_query():
    expected = [(21,)]
    run_common_test(expected, question_8_query)


# Q9: Ders başına öğrenci sayısı (course_name, student_count)
def test_question_9_query():
    result = question_9_query()
    counts = {r[0]: r[1] for r in result}
    assert counts['Veritabanı Temelleri'] == 3
    assert counts['İleri SQL'] == 1
    assert counts['Python Programlama'] == 1
    assert counts['Web Geliştirme'] == 1


# Q10: Kayıt olunmuş ders isimleri (DISTINCT)
def test_question_10_query():
    result = question_10_query()
    names = {r[0] for r in result}
    assert names == {'Python Programlama', 'Veritabanı Temelleri', 'Web Geliştirme', 'İleri SQL'}


def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")


class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1


def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    total = collector.passed + collector.failed
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")

    if total == 0:
        print("Hiç test çalıştırılmadı.")
        return

    user_score = round((collector.passed / total) * 100, 2)
    print(f"Skor: {user_score}")

    url = "https://kaizu-api-8cd10af40cb3.herokuapp.com/projectLog"
    payload = {
        "user_id": 638,
        "project_id": 36,
        "user_score": user_score,
        "is_auto": False
    }
    headers = {"Content-Type": "application/json"}
    send_post_request(url, payload, headers)


if __name__ == "__main__":
    run_tests()
