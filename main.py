# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
# format (HH:MM:SS)
#
#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59
#
# The maximum time never exceeds 359999 (99:59:59)
def make_readable(seconds):
    if seconds < 0 & seconds > 359999:
        return 'Invalid Input'

    hours, remainder = divmod(seconds, 3600)
    minutes, sec = divmod(remainder, 60)

    formatted_hours = str(hours).zfill(2)
    formatted_minutes = str(minutes).zfill(2)
    formatted_seconds = str(sec).zfill(2)

    return f"{formatted_hours}:{formatted_minutes}:{formatted_seconds}"


seconds = 3661
formatted_time = make_readable(seconds)
print(formatted_time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_readable(seconds)
