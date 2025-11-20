import time

max_tries = 5
attempts = 0
wait_time = 1

while attempts < max_tries:
    print ("Attempts", attempts+1, "wait time", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1