def add_time(start_time: str, duration: str, start_day: str = None) -> str:
    
    days_of_week: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    time, period = start_time.split(" ")
    start_hour, start_minute = map(int, time.split(":"))

    duration_hour, duration_minute = map(int, duration.split(":"))

    if period == 'PM':
        start_hour += 12
    
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    final_hour = total_hours % 24
    days_later = total_hours // 24


    final_period = "PM" if final_hour >= 12 else "AM"
    final_hour %= 12 or 12

    new_time = f'{final_hour}:{final_minute:02d} {final_period}'

    if start_day:
        day_index = days_of_week.index(start_day.capitalize())
        final_day = days_of_week[(day_index + days_later) % 7]
        new_time += f", {final_day}"

    if days_later == 1:
        new_time += f' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    return new_time

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM
print('\n<--------------->\n')

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday
print('\n<--------------->\n')

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM
print('\n<--------------->\n')

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)
print('\n<--------------->\n')

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)
print('\n<--------------->\n')

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)
print('\n<--------------->\n')

print(add_time('8:16 PM', '466:02'))
# Returns: 6:18 AM (20 days later)
