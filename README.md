# My First Odoo Module – Ta-Da Test Task

Цей модуль створений як тестове завдання для ознайомлення з базовим підходом до створення кастомного модуля в Odoo.

## Опис

Модуль додає нову модель `my_first_model` до системи Odoo з трьома полями:
- `name` – назва (Char)
- `places` – кількість місць (Integer)
- `active` – активність запису (Boolean)

## Структура модуля

```bash
module/
├── init.py
├── manifest.py
├── models/
│ └── test_model.py
├── views/
│ └── my_first_model_views.xml
├── security/
│ └── ir.model.access.csv
```


## Основні файли

- `__manifest__.py`: містить основну метаінформацію про модуль.
- `test_model.py`: Python-модель з визначенням структури таблиці.
- `my_first_model_views.xml`: XML-файл, що описує представлення (form & tree views).
- `ir.model.access.csv`: правила доступу до моделі (ACL).

## Встановлення

1. Активуйте `venv`
    ```bash
    for Mac:
    python3 -m venv venv
    source venv/bin/activate

    for Windows/Linux:
    python -m venv venv
    venv\Scripts\activate

    ```
2. Запустіть контейнери:
   ```bash
   docker compose up -d
   ```
   Оновіть:
   ```bash
   odoo -u module -d test_db --stop-after-init
   ```
    або активуйте модуль через інтерфейс Odoo.
3. Доступ до серверу http://localhost:8069/

    login: `admin`

    pass: `admin`
4. Перевірте, що модель доступна в меню.

## Мінімальні вимоги
- Odoo 18 (перевірено на останній nightly build)
- Python 3.10+
- PostgreSQL 13+