def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

display_info(name="Shova", age=20, course="MCA")
