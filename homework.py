# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
import json


class ToJson:
    def __init__(self, source_file: str, result_file: str):
        self.source_file = source_file
        self.result_file = result_file
        self.file_to_json(self.source_file, self.result_file)

    @staticmethod
    def file_to_json(source_file: str, result_file: str) -> None:
        with(
            open(source_file, 'r', encoding='utf-8') as file1,
            open(result_file, 'w', encoding='utf-8') as result
        ):
            my_dict = {}
            for line in file1:
                key, value = line.split()
                key = str(key).capitalize()
                value = float(value[:-1])
                my_dict[key] = value
            json.dump(my_dict, result, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    ToJson('file1.txt', 'file2.json')
