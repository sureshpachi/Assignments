import requests
import time
from tabulate import tabulate

# List of subdomains to be checked
subdomains = ['google.com', 'youtube.com', 'twitter.com']

def check_subdomain_status(subdomains):
    status_table = []

    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}")
            status = 'UP' if response.status_code == 200 else 'DOWN'
        except requests.ConnectionError:
            status = 'DOWN'
        
        status_table.append([subdomain, status])

    return status_table

def print_status_table(status_table):
    headers = ["Subdomain", "Status"]
    print(tabulate(status_table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    while True:
        status_table = check_subdomain_status(subdomains)
        print_status_table(status_table)
        time.sleep(60)  # Sleep for 60 seconds before checking again