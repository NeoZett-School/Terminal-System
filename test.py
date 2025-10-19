from Terminal import *

NOTICE_COLOR = lookup("$gre")
notice_env = new_env(NOTICE_COLOR,lookup("$res"))
notice_builder = Builder()
def set_notice(*value: str) -> None:
    notice_builder.clear()
    notice_builder.print("-----------------------------")
    for text in value:
        notice_builder.print(f"{notice_env.prefix}|$res", text)
    notice_builder.print(f"{notice_env.prefix}-----------------------------")
def notify() -> None:
    notice_env.enable()
    notice_builder.render(end="", color=True)
    notice_env.disable()


set_notice("Hello world!", "", "This is Neo. Say hi!")
notify()