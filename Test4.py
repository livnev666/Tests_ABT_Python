import json


#Test 4
def count_questions(data: dict):

    lst = []
    for item in data['game']['rounds']:
        for i in item['questions']:
            lst.append(i['question'])
    return f'Количество вопросов: {len(lst)}'


def print_right_answers(data: dict):

    lst = []
    for item in data['game']['rounds']:
        for i in item['questions']:
            lst.append(i['correct_answer'])
    return f'Список правильных ответов: {lst}'


def print_max_answer_time(data: dict):

    settings_time_to_answer = []
    questions_time_to_answer = []
    for item in data['game']['rounds']:
        settings_time_to_answer.append(item['settings']['time_to_answer'])
    for elem in data['game']['rounds'][1]['questions']:
        questions_time_to_answer.append(elem['time_to_answer'])
    settings_time_to_answer.extend(questions_time_to_answer)
    max_time = max(settings_time_to_answer)
    return f'Максимальное время ответа составляет: {max_time}'


def main(filename):

    with open(filename) as file:
        dc_data = json.load(file)
        print(count_questions(dc_data))
        print(print_right_answers(dc_data))
        print(print_max_answer_time(dc_data))


if __name__ == '__main__':
    main('test.json')