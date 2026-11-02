# my.assistant.py
# Author: Antonia Xenikis

# Messages with these words change someones booking or money, so a person must handle them.
HANDOFF_WORDS = ["book", "cancel", "refund", "payment"]


class StudioHelper:
    """A mock studio helper. Its replies come from simple rules."""

    def __init__(self, name, instructions, schedule):
        """Set up one helper with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.schedule = schedule
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        # Save what the user said with a role so we know who said it.
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        # Lowercase the message once so "Hello" and "hello" are treated the same.
        text = user_message.lower()
        # Check for a handoff first, so a booking request is never answered by the tool.
        if self.needs_human(text):
            return "I can't change your booking. I'm passing you to the front desk."
        # Questions about open classes use the schedule tool.
        if "open" in text or "available" in text or "class" in text:
            return self.schedule_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me which classes are open on a day."
        # Anything else gets a safe reply that admits it is not sure.
        return "I'm not sure how to help with that. I can list open classes."

    def needs_human(self, text):
        """Return True if the message asks to change a booking or handle money."""
        # Check every handoff word, and stop as soon as one appears in the text.
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def schedule_reply(self, user_message):
        """Use the schedule tool to answer a question about open classes."""
        # Ask the tool which day the message is about.
        day = self.schedule.find_day(user_message)
        # No known day: ask for one instead of guessing.
        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."
        # Ask the tool what is open that day, then build the reply from it.
        classes = self.schedule.classes_for(day)
        return f"Open classes on {day}: {classes}."
