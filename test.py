from Terminal import *
import time

progress = ProgressBar("$res[$gre$bri[has]$yel$dim[need]$res]", "-", 40)
symbol = AnimatedString(["-", "\\", "|", "/"])
NEED = 10000000
for i in range(NEED + 1):
    index = progress.calc_index(i, NEED)
    progress.print_frame("\r", f"({i}/{NEED}: {int((i/NEED)*100)}%) {symbol}", index=index, end="")
    symbol.next()