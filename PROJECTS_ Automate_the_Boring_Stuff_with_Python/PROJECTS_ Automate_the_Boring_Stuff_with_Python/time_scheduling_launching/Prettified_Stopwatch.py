#! python3
# A simple stopwatch program.

import pyperclip, time

# Display the program's instructions.
print('Press ENTER to begin. Then, press ENTER to click the stopwatch. Press CTRL-C to quit.')
input()								# Press ENTER to begin.
print('Started.')
startTime = time.time()				# Get the first lap's start time.
lastTime = startTime
lapNum = 1

laps_cotent = []

# Start tracking the lap times.
try:
	while True:
	
		# Record input.
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		
		# Format lap.
		formatted_content = f'Lap # {lapNum}: {totalTime} ( {lapTime} )'	
		print(formatted_content)

		lapNum += 1
		lastTime = time.time()		# Reset the last lap time.
		laps_cotent.append(formatted_content)	# Add to list of saved laps.
		
except KeyboardInterrupt:
	# Handle the CTRL-C exception to keep its error missage from displaying.
	print('\nDone.')
	
	# Copy to pyperclip.
	pyperclip.copy('\n'.join(laps_cotent))