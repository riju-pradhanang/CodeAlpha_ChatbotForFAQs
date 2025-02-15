import sys
import spacy
import random
import time
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
)
from PyQt6.QtGui import QTextCursor, QFont, QColor, QPalette, QIcon
from PyQt6.QtCore import Qt

class Chatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.responses = {
            "hello": [
    "Hi there! How can I help you?",
    "Hello! What can I do for you today?"
  ],
  "how are you": [
    "I'm just a chatbot, but I'm doing fine!",
    "I'm doing well, thank you for asking!"
  ],
  "what is your name": [
    "I am your AI assistant.",
    "I'm your virtual assistant, here to help you."
  ],
  "What is Artificial Intelligence (AI)?": [
    "AI is the science of creating computer systems that can perform tasks that normally require human intelligence. These tasks include understanding language, recognizing patterns, making decisions, and even learning from experience.",
    "Artificial Intelligence refers to technology that mimics human intelligence through learning, reasoning, and self-correction."
  ],
  "What are some everyday examples of AI?": [
    "You encounter AI almost every day! Virtual assistants like Siri and Google Assistant, recommendation systems on Netflix or Amazon, spam filters in your email, and navigation apps that suggest the best routes all use AI.",
    "Everyday examples of AI include voice assistants, smart home devices, personalized recommendations on streaming platforms, and even the fraud detection systems used by banks."
  ],
  "What is machine learning, and how is it related to AI?": [
    "Machine learning is a branch of AI that focuses on teaching computers to learn from data. Instead of programming every step, you give the computer examples, and it figures out patterns on its own.",
    "It's a subset of AI where computers improve their performance on tasks over time by analyzing data, rather than following explicit instructions."
  ],
  "What is deep learning?": [
    "Deep learning is a type of machine learning that uses artificial neural networks—computer systems inspired by the human brain. It is especially useful for tasks like image recognition and natural language processing.",
    "It involves using multiple layers of neural networks to analyze data with high complexity and make accurate predictions."
  ],
  "How do AI systems “learn”?": [
    "AI systems learn by processing large amounts of data and using algorithms to find patterns. Over time, with more data, these systems improve their accuracy and performance.",
    "They learn through a process of training on data, adjusting their internal parameters to reduce errors and improve decision-making."
  ],
  "What is a neural network?": [
    "A neural network is a model in AI designed to simulate the way a human brain works, consisting of layers of nodes (or 'neurons') that process input data.",
    "It's an interconnected system of algorithms that helps the AI recognize complex patterns, such as images or speech, by processing data through multiple layers."
  ],
  "What are some common misconceptions about AI?": [
    "Many people think AI is like a human brain or that it can think and feel. In reality, AI is a set of programmed instructions that process data and lacks emotions or consciousness.",
    "A common misconception is that AI possesses human-like understanding; however, it operates strictly on data and algorithms without true awareness."
  ],
  "How can I start learning about AI?": [
    "Beginners can start with online courses, tutorials, or books. Platforms like Coursera, edX, and Udacity offer courses on AI and machine learning.",
    "You might begin by exploring introductory resources such as online courses, beginner-friendly books like 'Artificial Intelligence: A Modern Approach', and blogs that simplify AI concepts."
  ],
  "Will AI replace human jobs?": [
    "AI is expected to automate certain tasks, which may change the nature of some jobs, but it also creates new opportunities by driving innovation and requiring new skills.",
    "While AI can take over repetitive tasks, it often works alongside humans, enhancing productivity rather than completely replacing jobs."
  ],
  "How does AI differ from human intelligence?": [
    "While AI can perform specific tasks very well, it doesn’t possess the general, adaptable intelligence that humans do, which includes creativity and emotional understanding.",
    "AI is designed for specific tasks and lacks the broad, flexible intelligence and emotional depth that characterize human thinking."
  ],
  "What ethical guidelines should be considered in AI development?": [
    "Ethical guidelines for AI include ensuring fairness by avoiding bias, maintaining transparency in decision-making, protecting user privacy, and establishing accountability in how systems operate.",
    "Key considerations are fairness, transparency, privacy protection, and accountability to ensure that AI systems are used responsibly and do not cause harm."
  ],
  "What is supervised vs. unsupervised learning?": [
    "In supervised learning, an AI system is trained on a labeled dataset where the correct answers are provided. In unsupervised learning, the system works with unlabeled data to identify patterns on its own.",
    "Supervised learning uses known outputs to train the system, whereas unsupervised learning lets the system find hidden structures in data without explicit guidance."
  ],
  "What are reinforcement learning and its applications?": [
    "Reinforcement learning is a type of machine learning where an AI learns optimal actions through trial and error by receiving rewards or penalties. It is used in robotics, gaming, and autonomous systems.",
    "It involves an AI agent taking actions in an environment to maximize cumulative rewards, with applications in areas like automated control systems and advanced game-playing strategies."
  ],
  "How can AI benefit society?": [
    "AI can solve complex problems in fields such as healthcare, environmental management, and education, increase operational efficiency, and drive innovation across industries.",
    "By automating tasks, providing insights from big data, and enabling new solutions in various fields, AI has the potential to significantly improve quality of life and economic productivity."
  ],
  "How do I stay updated with the latest AI developments?": [
    "You can stay informed by following reputable AI news sources, blogs, online communities, webinars, and academic publications like MIT Technology Review and The Verge.",
    "Subscribing to AI newsletters, joining online forums, and attending webinars or conferences are great ways to keep up with the rapid advancements in AI."
  ],
  "What should I consider when evaluating an AI system?": [
    "Consider the quality and diversity of the data used, the transparency and robustness of the algorithms, potential biases, ease of use, and how well the system addresses ethical and privacy concerns.",
    "Key factors include the data quality, algorithm transparency, bias mitigation, user-friendliness, and adherence to ethical standards to ensure reliable and fair performance."
  ],
  "bye": [
    "Goodbye! Have a nice day!",
    "See you later! Feel free to reach out if you need more help."
  ]
        }

    def get_response(self, user_input):
        doc = self.nlp(user_input.lower())

        best_match = None
        max_similarity = 0.0

        for key in self.responses:
            key_doc = self.nlp(key)
            similarity = key_doc.similarity(doc)

            if similarity > max_similarity:
                max_similarity = similarity
                best_match = key

        if best_match and max_similarity > 0.6:
            return random.choice(self.responses[best_match])

        return "I'm not sure how to respond to that, but I'm learning!"

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.chatbot = Chatbot()
        self.has_started_chat = False

    def init_ui(self):
        self.setWindowTitle("AI Chatbot 🧠")
        self.setGeometry(100, 100, 450, 550)
        self.setWindowIcon(QIcon("botImage.png"))

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1e1e1e"))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        self.setPalette(palette)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Arial", 12))
        self.chat_display.setStyleSheet(
            "background-color: #2d2d2d; border-radius: 10px; padding: 10px;"
            "color: white; border: 2px solid #444;"
        )
        self.chat_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chat_display.setText("👋 Hello\n Ask me anything!")
        self.layout.addWidget(self.chat_display)

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("🗨️ Type your message...")
        self.input_box.setFont(QFont("Arial", 12))
        self.input_box.setStyleSheet(
            "background-color: #333; border: 2px solid #555; padding: 8px; "
            "color: white; border-radius: 10px;"
        )
        self.input_box.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_box)

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

            if user_input.lower() == "bye":
                time.sleep(3)
                QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_gui = ChatbotGUI()
    chatbot_gui.show()
    sys.exit(app.exec())
