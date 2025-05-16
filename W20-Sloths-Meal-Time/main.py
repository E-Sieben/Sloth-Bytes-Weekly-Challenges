def timeToEat(current_time: str):
    """how much time remains until 7 a.m. or 7 p.m, while also checking for 12 pm as the odd one out"""
    if current_time == "12:00 a.m.":  # thought of this problem wayyyyy to late
        current_time = "00:00 p.m."
    is_it_am: bool = current_time.split(" ")[1] == "a.m."
    hours: int = 7
    current_time: list[str] = current_time.split(
        " ")[0].split(":")  # formatting

    if current_time == ["7", "0"]:  # it's already time to eat
        return [0, 0]

    if int(current_time[1]) != 0:  # calc minutes if it's not already a full hour
        mins: int = 60 - int(current_time[1])
        hours -= 1
    else:
        mins: int = 0

    if current_time[0] == "6":  # If under an hour distance no calc needed
        return [0, mins]

    hours = hours - int(current_time[0])
    if hours < 0:  # We might tick over the 12
        if is_it_am:
            if int(current_time[0]) == 12:
                hours = 0
            else:
                hours = 12 - int(current_time[0])
            hours -= 1
        else:
            hours = 12 + hours
    return [int(hours), int(mins)]


print(timeToEat("2:00 p.m."))
# 5 hours until the next meal, dinner
[5, 0]

print(timeToEat("5:50 a.m."))
# 1 hour and 10 minutes until the next meal, breakfast
[1, 10]

#! Extended test cases
print(timeToEat("7:00 p.m."))  # Check if current time is already satisfied
# 0 hours and 0 minutes until next meal, dinner
[0, 0]

print(timeToEat("6:43 p.m."))  # Check if only minutes needed
# 0 hours 17 minutes until next meal, dinner
[0, 17]

print(timeToEat("11:59 p.m."))  # What happens when the minute ticks over 12?
# 7 hours and 1 minute until next meal, breakfast
[7, 1]

print(timeToEat("9:59 p.m."))  # What happens when the hour ticks over 12?
# 9 hours and 1 minute until next meal, lunch
[9, 1]

print(timeToEat("7:01 a.m."))  # What happens if we hit lunch?
# 4 hours and 59 minutes until next meal, lunch
[4, 59]

print(timeToEat("12:00 a.m."))
# 7 hours and 0 minutes until next meal, dinner
[7, 0]
