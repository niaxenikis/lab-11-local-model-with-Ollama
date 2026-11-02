# my_main.py
# Author: Antonia Xenikis

# Import the two classes this program uses, one from each file.
from my_assistant import StudioHelper
from my_tool import ClassSchedule

CLASSES = {
    "monday": "6:00 am Reformer and 5:30 pm Mat",
    "wednesday": "9:00 am Reformer",
    "friday": "none",
}

schedule = ClassSchedule(CLASSES)
helper = StudioHelper(
    "Nia",
    "You help clients of a Pilates studio find open classes.",
    schedule,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
# Each turn adds two messages, so five turns gives ten.
