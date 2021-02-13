#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
# структуры; записи должны быть упорядочены по возрастанию среднего балла; вывод на
# дисплей фамилий и номеров групп для всех студентов, имеющих оценки 4 и 5; если таких
# студентов нет, вывести соответствующее сообщение.

import sys

if __name__ == '__main__':
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            marks = input("Успеваемость? ")

            student = {
                'name': name,
                'group': group,
                'marks': marks,
            }

            students.append(student)

            if len(students) > 1:
                students.sort(key=lambda item: item.get('marks', 0))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "No",
                    "Ф.И.О.",
                    "Группа",
                    "Успеваемость"
                )
            )
            print(line)

            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        student.get('marks', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):

            count = 0
            for student in students:
                if student.get('marks', '') >= 4:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, student.get('name', ''))
                        )

            if count == 0:
                print("Студентов с такими оценками нет")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <успеваемость> - запросить студентов с успеваемостью выше четверки;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)