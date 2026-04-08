class AdmissionLogic:
    # Минимальные проходные баллы для Kozybaev University
    PASSING_SCORES = {
        "Педагогика": 75,
        "ИТ": 65,
        "Агрономия": 50
    }

    @staticmethod
    def check_admission_chance(program: str, score: int) -> str:
        if score < 0 or score > 140:
            raise ValueError("Балл ЕНТ должен быть от 0 до 140")

        req = AdmissionLogic.PASSING_SCORES.get(program)

        if not req:
            return "Образовательная программа не найдена."

        if score >= req:
            return f"Успех! Баллов ({score}) достаточно для '{program}'."
        else:
            return f"Недостаточно баллов для '{program}'. Нужно {req}."
