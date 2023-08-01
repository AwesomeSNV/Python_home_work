def line_to_tuple(user_string):
    *a, b = user_string.split("/")
    a = "/".join(a)+"/"
    b, c = b.split(".")
    result = (a, b, c)
    return result

default_string = "D:/RetroArch/overlays/misc/xperia_play_l2_r2.cfg"
print(line_to_tuple(default_string))