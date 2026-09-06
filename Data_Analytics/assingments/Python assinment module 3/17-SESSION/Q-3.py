# Use the datetime module to get the current date and time, then format and print it as 'DD-MM-YYYY HH:MM:SS', similar to how WhatsApp shows message timestamps.<br><br><em><strong>Hint:</strong> Use strftime() to format the output.</em>


from datetime import datetime

now = datetime.now()

formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted_time)