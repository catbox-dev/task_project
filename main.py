import os

# Create task list
tasks_list = []

# Add functions for task managment
def print_menu():
    print('Main menu')
    print('1. Add task')
    print('2. Complete task')
    print('3. Show task list')
    print('4. Exit\n')

# Add functions for task managment
def add_task():
    tasks_list.append(input('Add task: '))
    print('Task added succesfully')

def complete_task():
    tasks_list.pop(int(input('Complete task: ')) - 1)
    print('Task completed succesfully')

def show_tasks():
    print("Pending tasks:")
    for i, task in enumerate(tasks_list):
        print(f"{i + 1} {task}")

def get_option():
    option = int(input("Enter option: "))
    return option

# Create main function
def main():
    while True:
        print_menu()
        option = get_option()
        if option == 1:
            add_task()
        elif option == 2:
            complete_task()
        elif option == 3:
            show_tasks()
        elif option == 4:
            break
        else:
            print("Invalid Option")
        print()
        input("Press ENTER to continue...")
        os.system('clear')


# Call main function
if __name__ == "__main__":
    main()