def get_summ(num_one, num_two):
    try:
        result = num_one + num_two
        return int(result)
    except (TypeError, ValueError):
        print("Введите число") 
   
if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))

