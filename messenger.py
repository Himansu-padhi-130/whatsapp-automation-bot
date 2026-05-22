import pywhatkit

def send_message(phone_number, message, hour, minute):
    print("Opening WhatsApp Web...")

    pywhatkit.sendwhatmsg(
        phone_number,
        message,
        hour,
        minute,
        wait_time=15
    )

    print("Message scheduled successfully!")