import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def list_todos(todos):
    if not todos:
        print("No todos found.")
    else:
        for idx, todo in enumerate(todos, 1):
            status = "✓" if todo["done"] else " "
            print(f"{idx}. [{status}] {todo['task']}")

def add_todo(todos, task):
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"Added: {task}")

def mark_done(todos, idx):
    if 0 <= idx < len(todos):
        todos[idx]["done"] = True
        save_todos(todos)
        print(f"Marked as done: {todos[idx]['task']}")
    else:
        print("Invalid todo number.")

def delete_todo(todos, idx):
    if 0 <= idx < len(todos):
        removed = todos.pop(idx)
        save_todos(todos)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid todo number.")

def main():
    todos = load_todos()
    while True:
        print("\nTodo App")
        print("1. List todos")
        print("2. Add todo")
        print("3. Mark todo as done")
        print("4. Delete todo")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            list_todos(todos)
        elif choice == "2":
            task = input("Enter todo: ")
            add_todo(todos, task)
        elif choice == "3":
            list_todos(todos)
            idx = int(input("Enter todo number to mark as done: ")) - 1
            mark_done(todos, idx)
        elif choice == "4":
            list_todos(todos)
            idx = int(input("Enter todo number to delete: ")) - 1
            delete_todo(todos, idx)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()