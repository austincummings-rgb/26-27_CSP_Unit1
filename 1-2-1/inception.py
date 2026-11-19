def my_function():
    print("does stuff")

    def your_fuction():
        print("Does other stuff")

        def other_fuction():
            my_function()
            your_fuction()

            other_function