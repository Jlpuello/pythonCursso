def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname":"Jorge", "lastname": "puello" }

    super_list = [
        {"firstname": "kelly", "lastname":"navarro" },
        {"firstname": "maria", "lastname":"coneo"},
        {"firstname": "cristian", "lastname": "niesto"},
        {"firstname": "jamer", "lastname":"jimenez"},
        {"firstname": "facundo", "lastname":"garcia"},
    ]

    super_dict = {
        "natural_num":[1,2,3,4,5],
        "integer_num":[-1,-2,-0,1,2],
        "floating_num":[1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-" , value)

    


if __name__ == '__main__':
    run()