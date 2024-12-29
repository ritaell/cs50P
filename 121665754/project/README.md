# Vocabulary Quiz App

#### Video Demo: <https://www.youtube.com/shorts/cqnRi1O6O7c>

#### Description:
The **Vocabulary Quiz App** is a Python-based application designed to help users improve their vocabulary through interactive quizzes. Users can add words and their meanings, take quizzes to test their knowledge, and track their progress. This simple yet effective tool offers a fun and educational way for users to expand their vocabulary and improve retention.

The application is run in the terminal, providing a straightforward and user-friendly interface for users to interact with. Upon starting the app, users can choose to add new words, take a quiz on their existing vocabulary list, or view their progress. Feedback is provided immediately after quiz attempts, and users can see how well they are doing with accuracy percentages for each word.

## Files and Structure

The project consists of the following key files:

### `project.py`

This is the main file that contains the core functionality of the Vocabulary Quiz App. The file includes several functions:

- **`main()`**: This is the main entry point of the app. It runs an interactive menu, offering users the options to add words, take quizzes, view progress, or exit the app. This function manages the flow of the program.

- **`add_word(words)`**: This function allows users to add new vocabulary words and their meanings to the app. If a word already exists in the dictionary, the app will notify the user. Otherwise, it adds the word and initializes its attempt and correct counters.

- **`take_quiz(words)`**: This function selects a random word from the user's vocabulary list and asks for its meaning. If the user answers correctly, the correct counter is updated. If the answer is wrong, the app shows the correct meaning.

- **`view_progress(words)`**: This function displays the progress of each word, including how many times it has been attempted, how many times it has been answered correctly, and the accuracy percentage.

### `test_project.py`

This file includes tests written using the `pytest` framework to verify the correctness of the app’s functionality. The tests check if the app correctly adds words, handles quiz answers, and displays progress:

- **`test_add_word()`**: Verifies that the `add_word` function correctly adds words and meanings to the vocabulary list.
- **`test_take_quiz_correct()`**: Ensures the quiz correctly handles correct answers and updates word counters.
- **`test_view_progress()`**: Confirms that progress is displayed accurately for each word, including the correct/incorrect attempts and accuracy percentage.

These tests help ensure the app works as expected and provide a safeguard when making future changes.

## Design Decisions

Several important decisions were made during the development of the app:

1. **Data Structure Choice**: The app uses a dictionary (`words`) to store vocabulary words and their corresponding meanings, as well as the number of attempts and correct answers. This structure allows for efficient lookups and easy updates.

2. **User Interface**: A command-line interface (CLI) was chosen for this app to keep things simple and focus on Python fundamentals. The CLI is ideal for this small-scale project, and it enables quick development and testing without the complexity of a graphical user interface (GUI).

3. **Quiz Randomization**: To make the quiz dynamic and engaging, the app selects words randomly from the list. This helps prevent users from memorizing the order of questions and keeps the quizzes interesting.

4. **Progress Tracking**: A progress-tracking feature was included to help users see how well they are doing. The accuracy percentage helps identify areas that need improvement, making the app more effective for long-term learning.

## Future Improvements

There are several enhancements that could be made to the Vocabulary Quiz App:

- **Data Persistence**: Currently, the app’s data is stored in memory, so any progress is lost when the app is closed. Implementing data persistence, such as saving vocabulary to a file (e.g., JSON or CSV), would allow users to retain their progress across sessions.

- **Graphical User Interface (GUI)**: While the CLI works well for this project, a GUI could enhance the user experience. Using a library like Tkinter or PyQt would provide a more visual and interactive experience.

- **Difficulty Levels**: The app could include difficulty levels, where users can categorize words into different levels (e.g., beginner, intermediate, advanced). This would allow users to focus on words based on their current skill level.

## Conclusion

The **Vocabulary Quiz App** is a simple yet powerful tool for improving vocabulary retention. It allows users to add new words, take quizzes, and track their progress. The app is easy to use and can be a valuable resource for anyone looking to expand their vocabulary, whether for language learning, test preparation, or personal growth.

The project provided a great opportunity to practice Python fundamentals, including the use of dictionaries, loops, conditionals, and handling user input. Moving forward, the app could be further enhanced with additional features like data persistence and a GUI, making it even more useful and engaging for users.
