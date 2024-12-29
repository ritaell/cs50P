import random

# Main function
def main():
    print("Welcome to the Vocabulary Quiz App!")
    words = {}
    while True:
        print("\nChoose an option:")
        print("1. Add a new word")
        print("2. Take a quiz")
        print("3. View progress")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_word(words)
        elif choice == "2":
            take_quiz(words)
        elif choice == "3":
            view_progress(words)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add a new word
def add_word(words):
    word = input("Enter a new word: ").strip()
    meaning = input("Enter the meaning: ").strip()
    if word in words:
        print("This word is already in your list!")
    else:
        words[word] = {"meaning": meaning, "correct": 0, "attempts": 0}
        print(f"Word '{word}' added successfully.")

# Function to quiz the user
def take_quiz(words):
    if not words:
        print("Your vocabulary list is empty. Add words first!")
        return

    word, data = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ").strip()

    if answer.lower() == data["meaning"].lower():
        print("Correct!")
        words[word]["correct"] += 1
    else:
        print(f"Incorrect. The correct meaning is '{data['meaning']}'.")
    words[word]["attempts"] += 1

# Function to view progress
def view_progress(words):
    if not words:
        print("Your vocabulary list is empty. Add words first!")
        return

    print("\nYour Progress:")
    for word, data in words.items():
        attempts = data["attempts"]
        correct = data["correct"]
        accuracy = (correct / attempts * 100) if attempts > 0 else 0
        print(f"- {word}: {correct}/{attempts} correct ({accuracy:.2f}% accuracy)")

if __name__ == "__main__":
    main()
