import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
import smtplib
from PyQt5.QtGui import QIcon  # Import QIcon module for setting the window icon
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSenderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Email Sender")
        self.setGeometry(100, 100, 400, 300)

        self.setWindowIcon(QIcon('chipcodelogo.png'))

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label_to = QLabel("To:")
        self.input_to = QLineEdit(self)

        self.label_subject = QLabel("Subject:")
        self.input_subject = QLineEdit(self)

        self.label_body = QLabel("Message:")
        self.input_body = QTextEdit(self)

        self.button_send = QPushButton("Send Email", self)
        self.button_send.clicked.connect(self.send_email)

        layout.addWidget(self.label_to)
        layout.addWidget(self.input_to)

        layout.addWidget(self.label_subject)
        layout.addWidget(self.input_subject)

        layout.addWidget(self.label_body)
        layout.addWidget(self.input_body)

        layout.addWidget(self.button_send)

        self.setLayout(layout)

    def send_email(self):
        to_address = self.input_to.text()
        subject = self.input_subject.text()
        body = self.input_body.toPlainText()

        if not to_address or not subject or not body:
            self.show_message("Error", "Please fill in all fields.")
            return

        try:
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "martinsseba3@gmail.com"
            smtp_password = "kilyxoranmdpunza"

            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = to_address
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, to_address, msg.as_string())

            self.show_message("Success", "Email sent successfully.")
        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}")

    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    email_sender_app = EmailSenderApp()
    email_sender_app.show()
    sys.exit(app.exec_())
