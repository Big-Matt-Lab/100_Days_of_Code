"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Daily Quotes Email Sender ***
This script sends a daily inspirational quote via email. It reads quotes from a local
'quotes.txt' file, selects one randomly, and then sends it using Python's `smtplib`
module for email communication. It utilizes environment variables for secure
handling of the sender's email password.

Python Concepts Highlighted:
- `os` module for interacting with the operating system, specifically for environment variables (`os.getenv()`).
- `random` module for selecting a random item from a list (`random.choice()`).
- `smtplib` for sending emails using the Simple Mail Transfer Protocol.
- `email.message.EmailMessage` for constructing well-formatted email messages.
- File I/O operations (`open()`, `readlines()`) for reading data from a text file.
- `try/except` blocks for robust error handling during email transmission.
- Global variables for configuration settings (`smtp_server`, `smtp_port`, `sender_email`, etc.).
"""

import os
import random
import smtplib
from email.message import EmailMessage

# Configuration for the SMTP server and email details.
# These global variables define how the email will be sent and to whom.
smtp_server = "smtp.gmail.com"  # The hostname of the SMTP server.
smtp_port = 587  # Standard port for STARTTLS (secure connection).
sender_email = "mattlabcode@gmail.com"  # The email address from which the quotes will be sent.
# Python concept: Using `os.getenv()` to securely retrieve the email password from environment variables.
# This prevents hardcoding sensitive information directly in the script.
password = os.getenv("MY_GOOGLE_APP_PASSWORD") # Do not use your regular password here
receiver_email = "matt.labriola@gmail.com"  # The recipient's email address.


def get_message() -> str:
    """Retrieves a random quote from the 'quotes.txt' file.

    This function opens the 'quotes.txt' file, reads all lines (each representing a quote),
    and then randomly selects one quote to be returned.

    Returns:
        str: A randomly selected quote from the 'quotes.txt' file.
    """
    # Python concept: Using `with open(...)` for safe file handling.
    # This ensures the file is properly closed even if errors occur.
    with open("quotes.txt", mode="r") as file:
        # Python concept: `readlines()` reads all lines from the file into a list of strings.
        quotes = file.readlines()
        # Python concept: `random.choice()` selects a single random element from the `quotes` list.
        quote_of_the_day = random.choice(quotes)
        return quote_of_the_day


# Python concept: Instantiating `EmailMessage` to create a new email object.
# This object allows for easy construction of email headers and content.
msg = EmailMessage()
# Setting the 'From' header of the email.
msg["From"] = sender_email
# Setting the 'To' header of the email.
msg["To"] = receiver_email
# Setting the 'Subject' header of the email.
msg["Subject"] = "Quote of the Day!"
# Python concept: Setting the content of the email by calling `get_message()` to fetch a quote.
msg.set_content(get_message())

# Python concept: `try/except` block for error handling during the email sending process.
# This ensures that the program doesn't crash if there's an issue with the SMTP connection or credentials.
try:
    # Python concept: Using `with smtplib.SMTP(...)` to establish an SMTP connection.
    # This ensures the connection is closed automatically after the block.
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        # Python concept: `starttls()` upgrades the connection to TLS (Transport Layer Security)
        # for secure communication.
        connection.starttls()
        # Python concept: `login()` authenticates the sender with the SMTP server using their email and password.
        connection.login(sender_email, password)
        # Python concept: `send_message()` sends the constructed `EmailMessage` object.
        connection.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    # If any error occurs during the `try` block, it will be caught here and printed.
    print(f"Error sending email: {e}")
