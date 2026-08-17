import csv
import subprocess

# Function to send ping requests
def send_ping(url):
    try:
        subprocess.Popen(['ping', '-c', '1', '-w', '1', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Ping sent successfully."
    except Exception as e:
        return str(e)

# File paths
input_txt_file_path = "million_url.txt"  # Replace "url.txt" with your file path
output_csv_file_path = "million_results.csv"  # Replace "ping_results.csv" with your desired output CSV file path

# Read URLs from the text file
urls = []
with open(input_txt_file_path, 'r') as file:
    for line in file:
        urls.append(line.strip())

# Create a list to store the ping results for each URL
ping_results_list = []

# Send ping to each URL
for url in urls:
    ping_result = send_ping(url)
    ping_results_list.append([url, ping_result])

    # Print the ping result for each URL
    print(f"Ping Result for URL '{url}': {ping_result}")

# Save the ping results to the output CSV file
with open(output_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Ping Result"])
    writer.writerows(ping_results_list)

print("Ping results saved to the output CSV file.")
