# tests/test_my_assistant.py
#  Author: Antonia Xenikis

from my_assistant import StudioHelper
from my_tool import ClassSchedule


def make_helper():
    """Build a fresh helper with its own tool for each test."""
    schedule = ClassSchedule({"monday": "6:00 am Reformer", "friday": "none"})
    return StudioHelper("Nia", "Be clear.", schedule)


def test_class_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("What classes are open on Monday?")
    assert reply == "Open classes on monday: 6:00 am Reformer."


def test_question_without_a_day_asks_for_one():
    helper = make_helper()
    assert "Which day" in helper.respond("What classes are open?")


def test_booking_request_goes_to_a_human():
    helper = make_helper()
    assert "front desk" in helper.respond("Please book me for Monday")


def test_unknown_request_gets_a_safe_reply():
    helper = make_helper()
    assert "not sure" in helper.respond("Do you validate parking?")


def test_history_grows_by_two_each_turn():
    helper = make_helper()
    helper.respond("hello")
    helper.respond("What is open on Friday?")
    assert len(helper.history) == 4
