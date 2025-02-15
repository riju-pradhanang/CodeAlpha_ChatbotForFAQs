# AI Chatbot Project

This project implements a simple AI chatbot using Python, spaCy for natural language processing, and PyQt6 for the graphical user interface. The chatbot is designed to answer questions about Artificial Intelligence.

## Features

*   **GUI Interface:** User-friendly interface built with PyQt6.
*   **Dark Mode:** Eye-friendly dark mode for extended use.
*   **Basic NLP:** Utilizes spaCy for basic natural language processing.
*   **Predefined Responses:** Answers common questions about AI with predefined responses.

## Installation

1.  **Clone the repository:**

    ```
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Install the required packages:**

    ```
    pip install spacy PyQt6
    python -m spacy download en_core_web_sm
    ```

## Usage

1.  **Run the chatbot:**

    ```
    python chatbot.py
    ```

2.  **Interact with the chatbot:**

    *   Type your message in the input box.
    *   Press Enter or click the "Send" button to send your message.
    *   The chatbot will display its response in the chat display area.
    *   Say "bye" to quit the application after a 3-second delay.

## Code Overview

*   `chatbot.py`: Contains the main application code, including the `Chatbot` class for handling responses and the `ChatbotGUI` class for the graphical interface.

    *   `Chatbot` class:

        *   `__init__`: Initializes the spaCy NLP model and the dictionary of predefined responses about Artificial Intelligence.
        *   `get_response`: Processes user input using spaCy to determine the best matching response from the predefined dictionary.  A similarity threshold of 0.6 is used. If no match is found above this threshold, a default "I'm not sure how to respond..." message is returned.
    *   `ChatbotGUI` class:

        *   `__init__`: Initializes the GUI components, including setting the window title, geometry, and icon. It also sets the initial `has_started_chat` flag to `False`.
        *   `init_ui`: Sets up the GUI layout, widgets (including `QTextEdit`, `QLineEdit`, and `QPushButton`), and styles, using a dark color palette.  It also sets the initial message in the `chat_display`.
        *   `send_message`: Retrieves user input, sends it to the chatbot, and displays both the user's message and the chatbot's response in the `chat_display`.  It handles clearing the initial "Hello" message upon the first user interaction. If the user types "bye", it quits the application after a 3-second delay.

## Dependencies

*   [spaCy](https://spacy.io/): For natural language processing (`en_core_web_sm` model is required).
*   [PyQt6](https://www.riverbankcomputing.com/software/pyqt/): For creating the graphical user interface.

## Predefined Responses

The chatbot is pre-programmed with responses to the following questions/phrases:

*   "hello"
*   "how are you"
*   "what is your name"
*   "What is Artificial Intelligence (AI)?"
*   "What are some everyday examples of AI?"
*   "What is machine learning, and how is it related to AI?"
*   "What is deep learning?"
*   "How do AI systems “learn”?"
*   "What is a neural network?"
*   "What are some common misconceptions about AI?"
*   "How can I start learning about AI?"
*   "Will AI replace human jobs?"
*   "How does AI differ from human intelligence?"
*   "What ethical guidelines should be considered in AI development?"
*   "What is supervised vs. unsupervised learning?"
*   "What are reinforcement learning and its applications?"
*   "How can AI benefit society?"
*   "How do I stay updated with the latest AI developments?"
*   "What should I consider when evaluating an AI system?"
*   "bye"

## Future Enhancements

*   **Improved NLP:** Implement more advanced NLP techniques to improve the chatbot's understanding of user input.
*   **Expanded Knowledge Base:** Add more predefined responses to cover a wider range of topics.
*   **Dynamic Learning:** Integrate machine learning models to allow the chatbot to learn from user interactions and improve its responses over time.
*   **Multimedia Support:** Add support for images, audio, and video.
*   **GUI Improvements:** Enhance the GUI with features like message timestamps, user avatars, and improved styling.
*   **Error Handling:** Implement more robust error handling and logging.

## Contributing

Contributions are welcome! Please feel free to submit pull requests with bug fixes, new features, or improvements to the documentation.

