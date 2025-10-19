from Terminal import *

set_env_mode("Single")

page = Builder()
page.print("Hello!")
page.print("How are you doin?")

env = new_env(lookup("$gre"),lookup("$res"))
env.enable()
page.render(end="")
env.disable()