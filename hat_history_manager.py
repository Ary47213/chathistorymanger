class Message:
    def __init__(self, text):
        self.text = text
        self.timestamp =  datetime.datetime.now()

class ChatHistory:
    def __init__(self):
        self.message_queue = []
        self.undo_stack = []
        self.redo_stack = []

    def send_message(self, text):
        message = Message(text)
        self.message_queue.append(message)
        self.undo_stack.append(message)
        self.redo_stack = []  # Clear redo stack

    def undo_message(self):
        if self.undo_stack:
            message = self.undo_stack.pop()
            self.redo_stack.append(message)
            self.message_queue.remove(message)
            print(f"Message undone: {message.text}")
        else:
            print("No messages to undo.")

    def redo_message(self):
        if self.redo_stack:
            message = self.redo_stack.pop()
            self.undo_stack.append(message)
            self.message_queue.append(message)
            print(f"Message redone: {message.text}")
        else:
            print("No messages to redo.")

    def display_messages(self):
        for message in self.message_queue:
            print(f"{message.text} ({message.timestamp})")

def main():
    chat_history = ChatHistory()
    while True:
        print("1. Send message")
        print("2. Undo message")
        print("3. Redo message")
        print("4. Display messages")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter message: ")
            chat_history.send_message(text)
        elif choice == "2":
            chat_history.undo_message()
        elif choice == "3":
            chat_history.redo_message()
        elif choice == "4":
            chat_history.display_messages()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

