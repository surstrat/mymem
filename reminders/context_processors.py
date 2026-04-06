# reminders/context_processors.py

def public_reminders(request):
    """
    Контекстный процессор для передачи публичных напоминаний во все шаблоны.
    Пока возвращает заглушку, позже заменим на реальные данные.
    """
    # Временная заглушка
    fake_public_reminders = [
        {
            'id': 1,
            'title': 'Дедлайн по проекту',
            'description': 'Сдать отчёт до конца недели',
            'author_name': 'Иван Петров',
            'send_at': '2026-04-10 18:00',
        },
        {
            'id': 2,
            'title': 'Вебинар по Django',
            'description': 'Бесплатный вебинар в четверг',
            'author_name': 'Анна Смирнова',
            'send_at': '2026-04-08 15:00',
        },
        {
            'id': 3,
            'title': 'День рождения друга',
            'description': 'Не забыть поздравить',
            'author_name': 'Популярный пользователь',
            'send_at': '2026-04-12 10:00',
        },
    ]
    
    return {
        'public_reminders_list': fake_public_reminders,
    }