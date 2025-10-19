from Terminal import *
import time

progress = ProgressBar("$gre$bri[has]$yel$dim[need]$res ($gre[prog]%$res)", "-", 10)
for i in range(11):
    index = progress.calc_index(i, 10)
    progress.print_frame("\r", index=index, end="")
    time.sleep(1)