#!/usr/bin/env python3

from subprocess import run

def interpret_info(info):
    cmus_data = info.split("\n")
    info = {}

    for line in cmus_data:
        parts = line.split(" ")
        key = parts[0]
        if key == "tag":
            key = parts[1]
            val = parts[2:]
        else:
            val = parts[1:]

        info[key] = " ".join(val)

    return info

def get_emoji(status):
    if status == "playing":
        return "🎵"
    elif status == "paused":
        return "▌▌"
    elif status == "stopped":
        return "◻️"
    else:
        return "stat: {}".format(status)

def seconds_to_time(n):
    n = int(n)
    mins = n // 60
    secs = n % 60
    return "{:02}:{:02}".format(mins, secs)

def get_info(info):
    parsed = interpret_info(info)
    status = parsed["status"]

    emoji = get_emoji(status)

    msg = ""
    if "artist" not in parsed and "title" not in parsed:
        msg = "{} {}".format(emoji, status.capitalize())
    else:
        artist = parsed["artist"]
        title = parsed["title"]
        msg = "{} {} - {}".format(emoji, artist, title)
        
    if status != "stopped":
        duration = parsed["duration"]
        progress = parsed["position"]
        msg = "{} | {} / {}".format(msg, seconds_to_time(progress), seconds_to_time(duration))

    return {
        "status": status,
        "msg": msg
    }

def get_colour(status):
    if status == "playing":
        return "#ffffff"
    elif status == "paused":
        return "#FFFF00"
    elif status == "stopped":
        return "#FFA500"
    return "#ffffff" 

def i3():
    res = run(["pgrep", "cmus"], capture_output=True).returncode
    if res != 0:
        print("cmus down")
        print("#ff0000")
        return

    raw = run(["cmus-remote", "-Q"], capture_output=True).stdout
    info = get_info(str(raw, "utf-8"))

    print(info["msg"])
    print(get_colour(info["status"]))

if __name__ == "__main__":
    i3()