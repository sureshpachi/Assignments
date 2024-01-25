import time
import psutil
#i have set limit 1 so i perform testing as 80% cpu utilisation never crossing 10 also
limit = 1
def monitor_cpu_usage():
    while True:
        try:
        
            cpu_status = psutil.cpu_percent(time.sleep(1))
            
            if cpu_status > limit:
                print(f"\033[31mAlert! CPU usage is {cpu_status}%\033[0m")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
monitor_cpu_usage()