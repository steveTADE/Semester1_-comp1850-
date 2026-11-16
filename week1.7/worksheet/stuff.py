import time
loading = ['\\', '|', '/', '-']

print('\x1b[2J\x1b[3J')
while True:
    for character in loading:
        print('\x1b[H' + character)
        time.sleep(0.1)