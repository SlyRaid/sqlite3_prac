# SQLife3

### Техническое задание:
Создайте базу данных students.db  
В базе данных должны существовать 2 таблицы: students и grades  
В таблице students должны присутствовать следующие поля: id, name, age  
В таблице grades должны присутствовать следующие поля: id, student_id, subject, grade  

Так же нужно создать класс University со следующими атрибутами и методами:  
name - имя университета  
add_student(name, age) - метод добавления студента.  
add_grade(sudent_id, subject, grade) - метод добавления оценки.  
get_students(subject=None) - метод для возврата списка студентов в формате [(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)], где subject, если не является None(по умолчанию) и если такой предмет существует, выводит студентов только по этому предмету.

#### Описание полей:  
id - в обоих таблицах обязательно PRIMARY KEY  
name - STR  
age - INT  
subject - STR  
grade - FLOAT  
и самое интересное student_id - INT (или внешний ключ)

Внешний ключ - это данное в поле указывающее на id в другой таблице, оно может быть реализовано следующей командой в SQL: FOREIGN KEY (student_id) REFERENCES students(id), при создании таблицы.
При этом поле student_id - существует как INT.

#### Пример работы кода:  
###### Код:
```
u1 = University('Urban')  
u1.add_student('Ivan', 26) # id - 1  
u1.add_student('Ilya', 24) # id - 2  
u1.add_grade(1, 'Python', 4.8)  
u1.add_grade(2, 'PHP', 4.3)  
print(u1.get_students())  
print(u1.get_students('Python'))
```
###### Консоль:
[(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)]
[(Ivan, 26, Python, 4.8)]

