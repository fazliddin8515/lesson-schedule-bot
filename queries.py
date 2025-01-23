create_lessons_table_query = '''
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_name VARCHAR NOT NULL,
    day_name VARCHAR NOT NULL,
    lesson_order INTEGER NOT NULL
)
'''

insert_lessons_query = '''
INSERT INTO lessons (lesson_name, day_name, lesson_order) VALUES (?, ?, ?)
'''

select_lessons_query = '''
SELECT lesson_name FROM lessons WHERE day_name = ? ORDER BY lesson_order;
'''