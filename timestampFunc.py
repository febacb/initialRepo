from datetime import datetime
import pytz
import time

day_mapping = {
    'Senin': 'Monday',
    'Selasa': 'Tuesday',
    'Rabu': 'Wednesday',
    'Kamis': 'Thursday',
    'Jumat': 'Friday',
    'Sabtu': 'Saturday',
    'Minggu': 'Sunday'
}

month_mapping = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'Mei': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Ags': 'August',
    'Sep': 'September',
    'Okt': 'October',
    'Nov': 'November',
    'Des': 'December'
}

def formattedNewsDetik(date_string):
  try:
    # Replace Indonesian day and month names with English equivalents
    for indo_day, eng_day in day_mapping.items():
        date_string = date_string.replace(indo_day, eng_day)

    for indo_month, eng_month in month_mapping.items():
        date_string = date_string.replace(indo_month, eng_month)

    # Define the format of the input date and time string
    date_format = "%A, %d %B %Y %H:%M WIB"

    # Parse the date string into a datetime object
    parsed_datetime = datetime.strptime(date_string, date_format)

    # Set the time zone to WIB (Waktu Indonesia Barat)
    wib_timezone = pytz.timezone('Asia/Jakarta')
    parsed_datetime = wib_timezone.localize(parsed_datetime)

    # Format the datetime object as a string in "YYYY-MM-DD HH:MI:SS" format
    date_string = parsed_datetime.strftime("%Y-%m-%d %H:%M:%S")
  except:
    pass

