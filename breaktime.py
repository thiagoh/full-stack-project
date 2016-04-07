import time
import webbrowser

i = 0

print('Work started at ' + time.ctime())

while i < 3:
    time.sleep(10)
    print('Break time!')
    webbrowser.open('https://www.youtube.com/watch?v=izGwDsrQ1eQ')
    i += 1
