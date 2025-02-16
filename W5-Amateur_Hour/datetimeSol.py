from datetime import datetime

def hoursPassed(startTime: int, endTime: int) -> str:
    # conversion
    startTime = datetime.strptime(startTime, "%I:%M %p")
    endTime = datetime.strptime(endTime, "%I:%M %p")
    # calculation
    timePassed: int = endTime - startTime
    timePassed = int(timePassed.total_seconds() / 3600)
    # output
    return f"{timePassed} hours" if timePassed != 0 else "no time passed"      

print(hoursPassed("3:00 AM", "9:00 AM"))
print(hoursPassed("2:00 PM", "4:00 PM"))
print(hoursPassed("1:00 AM", "3:00 PM"))
print(hoursPassed("4:00 PM", "4:00 PM"))

'''
Expected Output:
hoursPassed("3:00 AM", "9:00 AM")
output = "6 hours"
hoursPassed("2:00 PM", "4:00 PM")
output = "2 hours"
hoursPassed("1:00 AM", "3:00 PM")
output = "14 hours"
hoursPassed("4:00 PM", "4:00 PM")
output = "no time passed"
'''