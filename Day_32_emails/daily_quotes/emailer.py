import os
import random
import smtplib

from flask import Flask
from google.cloud import storage

app = Flask(__name__)


def get_quote_from_gcs():
    # 1. Grab bucket and blob details from environment settings
    bucket_name = os.environ.get("BUCKET_NAME")
    source_blob_name = "quotes.txt"

    # 2. Use the GCS syntax to target the file
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    # 3. Read the file contents directly as text data from the cloud
    # (No need to download a physical file to the server disk first!)
    file_contents = blob.download_as_text()

    # 4. Split the text into lines and pick a random quote
    quotes = file_contents.splitlines()
    return random.choice(quotes) if quotes else "Keep pushing forward!"


@app.route("/", methods=["POST", "GET"])
def trigger_email_job():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "mattlabcode@gmail.com"
    password = os.getenv("MY_GOOGLE_APP_PASSWORD")
    receiver_email = "matt.labriola@gmail.com"

    try:
        # Fetch the quote dynamically from your cloud bucket blob
        quote_of_the_day = get_quote_from_gcs()

        # Prepare the email body format
        subject = "Subject: Your Scheduled Quote of the Day\n\n"
        body = f"{subject}{quote_of_the_day}"

        # Send using your existing Gmail configuration
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(sender_email, password)
            connection.sendmail(
                from_addr=sender_email, to_addrs=receiver_email, msg=body
            )

        return "Email sent successfully!", 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return f"Error: {e}", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
