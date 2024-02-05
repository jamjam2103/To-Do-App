import os
import json
import argparse

# File to store the to-do list
TODO_FILE = 'todo.json'

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index}. {task['title']} - Priority: {task['priority']} - {status}")

def add_task(todo_list, title, priority):
    todo_list.append({'title': title, 'done': False, 'priority': priority})
    save_todo_list(todo_list)
    print(f"Task '{title}' added to the to-do list.")

def mark_task_done(todo_list, index):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1]['done'] = True
        save_todo_list(todo_list)
        print(f"Task {index} marked as done.")
    else:
        print("Invalid task index.")

def delete_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        deleted_task = todo_list.pop(index - 1)
        save_todo_list(todo_list)
        print(f"Task '{deleted_task['title']}' deleted from the to-do list.")
    else:
        print("Invalid task index.")

def main():
    parser = argparse.ArgumentParser(description='To-Do List Manager')
    parser.add_argument('action', choices=['display', 'add', 'done', 'delete', 'exit'], help='Action to perform')
    parser.add_argument('--title', help='Task title')
    parser.add_argument('--priority', help='Task priority')
    parser.add_argument('--index', type=int, help='Task index')

    args = parser.parse_args()

    todo_list = load_todo_list()

    if args.action == 'display':
        display_todo_list(todo_list)
    elif args.action == 'add':
        add_task(todo_list, args.title, args.priority)
    elif args.action == 'done':
        mark_task_done(todo_list, args.index)
    elif args.action == 'delete':
        delete_task(todo_list, args.index)
    elif args.action == 'exit':
        print("Exiting the to-do list app. Have a great day!")
    else:
        print("Invalid action. Please choose from display, add, done, delete, or exit.")

    todo_list = load_todo_list()

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            title = input("Enter task title: ")
            priority = input("Enter task priority (e.g., high, medium, low): ")
            add_task(todo_list, title, priority)
        elif choice == '3':
            index = int(input("Enter task index to mark as done: "))
            mark_task_done(todo_list, index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            delete_task(todo_list, index)
        elif choice == '5':
            print("Exiting the to-do list app. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
