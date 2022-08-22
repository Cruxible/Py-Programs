import progressbar
import time
bar = progressbar.ProgressBar(maxval=20, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(10):
    bar.update(i+1)
    time.sleep(1)
bar.finish()