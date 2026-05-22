from messenger import send_message

phone_number = input("Enter phone number with country code: ")
message = input("Enter your message: ")

hour = int(input("Enter hour (24-hour format): "))
minute = int(input("Enter minute: "))

send_message(phone_number, message, hour, minute)