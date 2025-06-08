from datetime import datetime
import pytz

# Define the IST timezone
ist = pytz.timezone('Asia/Kolkata')

# Get current time in IST
current_time = datetime.now(ist)

# Print the formatted time
print("Current Date and Time in IST:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
