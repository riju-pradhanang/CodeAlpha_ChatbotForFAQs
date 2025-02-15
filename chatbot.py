import sys
import spacy
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
)
from PyQt6.QtGui import QTextCursor, QFont, QColor, QPalette, QIcon
from PyQt6.QtCore import Qt

class Chatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.responses = {
            "hello": "Hi there! How can I help you?",
            "how are you": "I'm just a chatbot, but I'm doing fine!",
            "what is your name": "I am your AI assistant.",
            "What is Artificial Intelligence (AI)?": "AI is the science of creating computer systems that can perform tasks that normally require human intelligence. These tasks include understanding language, recognizing patterns, making decisions, and even learning from experience.",
            "What are some everyday examples of AI?": "You encounter AI almost every day! Virtual assistants like Siri and Google Assistant, recommendation systems on Netflix or Amazon, spam filters in your email, and even navigation apps that suggest the best routes all use AI.",
            "What is machine learning, and how is it related to AI?": "Machine learning is a branch of AI that focuses on teaching computers to learn from data. Instead of programming every single step, you give the computer examples (data), and it figures out patterns on its own.",
            "What is deep learning?": "Deep learning is a type of machine learning that uses artificial neural networks—computer systems inspired by the human brain. Deep learning is especially useful for tasks like image recognition and natural language processing.",
            "How do AI systems “learn”?": "AI systems learn by processing large amounts of data and using algorithms (sets of rules) to find patterns. Over time, with more data, these systems improve their accuracy and performance, much like how we learn from experience.",
            "What is a neural network?": "A neural network is a model in AI designed to simulate the way a human brain works. It consists of layers of nodes (or “neurons”) that process input data, helping the system recognize complex patterns such as faces in photos or spoken words.",
            "What are some common misconceptions about AI?": "Many people think AI is like a human brain or that it can think and feel. In reality, AI is a set of programmed instructions that process data. It doesn’t have emotions, consciousness, or common sense.",
            "How can I start learning about AI?": "Beginners can start with online courses, tutorials, or books. Platforms like Coursera, edX, and Udacity offer courses on AI and machine learning. For reading, `Artificial Intelligence: A Modern Approach` is a popular introductory text, and websites like Towards Data Science have many articles that explain AI concepts in everyday language.",
            "Will AI replace human jobs?": "AI is expected to automate certain tasks, which may change the nature of some jobs. However, it can also create new opportunities by driving innovation and creating jobs that require new skills. The goal is often to work alongside AI rather than be replaced by it.",
            "How does AI differ from human intelligence?": "While AI can perform specific tasks very well, it doesn’t possess the general, adaptable intelligence that humans do. Human intelligence includes creativity, emotions, and the ability to learn from a wide range of experiences—areas where current AI is limited.",
            "What ethical guidelines should be considered in AI development?": "Ethical guidelines for AI include ensuring fairness by avoiding bias, maintaining transparency in decision-making, protecting user privacy, and establishing accountability in how systems operate.",
            "What is supervised vs. unsupervised learning?": "In supervised learning, an AI system is trained on a labeled dataset where the correct answers are provided, while in unsupervised learning, the system works with unlabeled data to identify patterns and structures on its own.",
            "What are reinforcement learning and its applications?": "Reinforcement learning is a type of machine learning where an AI learns optimal actions through trial and error by receiving rewards or penalties. It is commonly used in robotics, gaming, and autonomous systems.",
            "How can AI benefit society?": "AI can solve complex problems in fields such as healthcare, environmental management, and education, increase operational efficiency, enhance decision-making, and drive innovation across industries.",
            "How do I stay updated with the latest AI developments?": "You can stay informed by following reputable AI news sources, blogs, online communities, webinars, and academic publications. Websites like MIT Technology Review, The Verge, and specialized AI forums are great places to start.",
            "What should I consider when evaluating an AI system?": "Consider the quality and diversity of the data used, the transparency and robustness of the algorithms, potential biases, ease of use, and how well the system addresses ethical and privacy concerns.",
            "bye": "Goodbye! Have a nice day!",
        }

    def get_response(self, user_input):
        doc = self.nlp(user_input.lower())
        for key in self.responses:
            if key in doc.text:
                return self.responses[key]
        return "I'm not sure how to respond to that."

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.chatbot = Chatbot()
        self.has_started_chat = False  # Track if conversation has started

    def init_ui(self):
        self.setWindowTitle("AI Chatbot 🧠 ")
        self.setGeometry(100, 100, 450, 550)

        self.setWindowIcon(QIcon("botImage.png"))

        # Set dark mode palette
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1e1e1e"))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        self.setPalette(palette)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)

        # Chat display area
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Arial", 12))
        self.chat_display.setStyleSheet(
            "background-color: #2d2d2d; border-radius: 10px; padding: 10px;"
            "color: white; border: 2px solid #444;"
        )
        self.chat_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chat_display.setText("👋 Hello\n Ask me anything about AI!")  # Display placeholder text
        self.layout.addWidget(self.chat_display)

        # Input box
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("🗨️ Type your message...")
        self.input_box.setFont(QFont("Arial", 12))
        self.input_box.setStyleSheet(
            "background-color: #333; border: 2px solid #555; padding: 8px; "
            "color: white; border-radius: 10px;"
        )
        self.input_box.returnPressed.connect(self.send_message)  # Enter key event
        self.layout.addWidget(self.input_box)

        # Send button
        self.send_button = QPushButton("Send 🚀", self)
        self.send_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.send_button.setStyleSheet(
            "background-color: #0078D7; color: white; border-radius: 10px; padding: 8px;"
            "border: none;"
        )
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def send_message(self):
        user_input = self.input_box.text().strip()
        if user_input:
            if not self.has_started_chat:
                self.chat_display.clear()
                self.has_started_chat = True

            self.chat_display.append(f"<b style='color: #4CAF50;'>You:</b> {user_input}")
            response = self.chatbot.get_response(user_input)
            self.chat_display.append(f"<b style='color: #FF9800;'>Bot:</b> {response}\n")
            self.chat_display.moveCursor(QTextCursor.MoveOperation.End)
            self.input_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_gui = ChatbotGUI()
    chatbot_gui.show()
    sys.exit(app.exec())
