import time
import webbrowser


total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while(break_count < total_breaks):
	time.sleep(7200)
	webbrowser.open_new_tab("https://www.youtube.com/watch?v=syMGF7UaSeQ")
	break_count = break_count + 1

