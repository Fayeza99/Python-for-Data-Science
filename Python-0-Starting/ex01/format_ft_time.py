
from datetime import datetime, timedelta, date, time

current_datetime = datetime.now()
# month_name = current_datetime.strftime("%B")

past_date = datetime(1970, 1, 1)
time_diff = current_datetime - past_date
seconds_count = f"{time_diff.total_seconds():,.4f}"
seconds_count_sci_notation = f"{time_diff.total_seconds():.2e}"

print("Seconds since January 1, 1970:",seconds_count, "or", seconds_count_sci_notation, "in scintific notation")

date_format = current_datetime.strftime("%b %d %Y")
print(date_format)