def main():
    school42 = [
        {'school_class': 'класс 1', 'scores': [3,2,2,5,5]},
        {'school_class': 'класс 2', 'scores': [3,3,3,5,2]},
        {'school_class': 'класс 3', 'scores': []},
    ]

    len_total = 0
    school_total = 0
    for class_info in school42:
        try: 
            class_name = class_info['school_class']   
            scores = class_info['scores']
            scores_total = sum(scores)
            scores_average = scores_total/len(scores)
            print(f"Средняя оценка {class_name} : {scores_average}")
            school_total += sum(scores)
            len_total += len(scores)
            school_average = school_total/len_total
        except ZeroDivisionError:
            print(f'Средняя оценка {class_name}: Четверть еще не началась, оценок нет')

    print(f"Средняя оценка по школе: {school_average}")
    
if __name__ == "__main__":
    main()


