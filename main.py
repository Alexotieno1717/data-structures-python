# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
# format (HH:MM:SS)
#
#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59
#
# The maximum time never exceeds 359999 (99:59:59)
def make_readable(seconds):
    if seconds < 0 or seconds > 359999:
        return 'Invalid Input'

    hours, remainder = divmod(seconds, 3600)
    minutes, sec = divmod(remainder, 60)

    return '{:02}:{:02}:{:02}' . format(hours, minutes, sec)


seconds = 459999
formatted_time = make_readable(seconds)
print(formatted_time)  # 99:59:59 final output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_readable(seconds)
