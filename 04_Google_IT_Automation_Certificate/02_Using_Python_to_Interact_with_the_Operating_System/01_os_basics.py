import arrow

# get tody's date and time
current_time = arrow.now()

# printing Time in professional format
print("Current Time:", current_time.format('YYYY-MM-DD HH:mm:ss'))

# get the time after 3 hours
future_time = current_time.shift(hours=-3)
print("3 hours ago:", future_time.humanize())

from PIL import Image

# Creating a new image of 300x200 pixels with red color
print("Creating a new image...")
img = Image.new('RGB', (300, 200), color= '#00FF00')

img.show()
print("Success! PIL (Pillow) is working perfectly.")