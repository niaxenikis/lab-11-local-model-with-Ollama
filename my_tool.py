# my_tool.py
# Author: Antonia Xenikis


class ClassSchedule:
    """A tool that knows which classes are open on each day. It knows nothing about chatting."""

    def __init__(self, classes):
        """Store the schedule this tool can look up."""
        # keeps the dirctionary on this object so the other methods can use it later.
        self.classes = classes

    def find_day(self, text):
        """Return the first known day mentioned in text, or None."""
        # Loop over every day in the schedule (the dictonary keys).
        for day in self.classes:
            if day in text.lower():
                return day
        return None

    def classes_for(self, day):
        """Return the classes for one day or None if the day is unknown."""
        # Check that the day exists first, so a missing day doesnt crash.
        if day in self.classes:
            return self.classes[day]
        return None
