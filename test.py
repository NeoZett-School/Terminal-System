from Terminal import *

set_env_mode("")

page = Builder()
page.print("Hello!")
page.print("How are you doin?")

env = new_env(lookup("$gre"),lookup("$res"))
page.render(end="")