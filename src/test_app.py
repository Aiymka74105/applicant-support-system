import pytest
import sqlite3
import os
from database import Database
from logic import AdmissionLogic

# --- ЮНИТ-ТЕСТЫ (Проверка изолированной бизнес-логики) ---

def test_admission_success():
    # Тест 1: Проверка успешного прохождения по баллам
    result = AdmissionLogic.check_admission_chance("ИТ", 80)
    assert "Поздравляем" in result

def test_admission_fail():
    # Тест 2: Проверка недобора баллов
    result = AdmissionLogic.check_admission_chance("Педагогика", 60)
    assert "К сожалению" in result

def test_invalid_score():
    # Тест 3: Проверка обработки некорректных данных (ошибка валидации)
    with pytest.raises(ValueError):
        AdmissionLogic.check_admission_chance("ИТ", 150)


# --- ИНТЕГРАЦИОННЫЙ ТЕСТ (Проверка связки: БД + Логика) ---

def test_full_system_integration():
    # Тест 4: Создаем тестовую БД, добавляем пользователя, проверяем его статус
    test_db_name = "test_kozybaev.db"
    db = Database(test_db_name)
    
    # 1. Записываем в базу
    db.add_applicant("123456789012", "Иван Иванов", "Агрономия", 55)
    
    # 2. Читаем из базы
    applicant_data = db.get_applicant("123456789012")
    assert applicant_data is not None
    name, program, score = applicant_data
    
    # 3. Передаем данные из БД в бизнес-логику
    status = AdmissionLogic.check_admission_chance(program, score)
    
    # 4. Проверяем финальный результат
    assert "Поздравляем" in status
    
    # Очистка после теста
    db.conn.close()
    os.remove(test_db_name)