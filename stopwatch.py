import time
import sys
import keyboard

running = False
start_time = 0

print("Stopwatch Controls:")
print("↑  = Start")
print("↓  = Stop")
print("Space = Quit")

while True:
    if keyboard.is_pressed("space"):
        print("\nProgram Ended.")
        break

    if keyboard.is_pressed("up") and not running:
        start_time = time.time()
        running = True
        print("\nStopwatch Started...")

    if keyboard.is_pressed("down") and running:
        end_time = time.time()
        elapsed = end_time - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        print(f"\nStopwatch Stopped at: {minutes:02d}:{seconds:02d}")
        running = False

    if running:
        elapsed = time.time() - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)

        sys.stdout.write(f"\rTime: {minutes:02d}:{seconds:02d}")
        sys.stdout.flush()
        time.sleep(1)
