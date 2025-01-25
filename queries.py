create_lessons_table_query = '''
CREATE TABLE IF NOT EXISTS lessons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    lesson_name VARCHAR(20) NOT NULL,
    day_name VARCHAR(15) NOT NULL,
    lesson_order INT NOT NULL
);
'''

insert_lessons_query = '''
INSERT INTO lessons (lesson_name, day_name, lesson_order) VALUES (%s, %s, %s);
'''

select_lessons_query = '''
SELECT lesson_name FROM lessons WHERE day_name = %s ORDER BY lesson_order;
'''

delete_lessons_query = '''
DELETE FROM lessons WHERE day_name = %s;
'''