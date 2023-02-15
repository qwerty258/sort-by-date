#!/usr/bin/env python3

import os
import datetime


def main():
    current_dir = os.path.abspath(os.curdir)
    files = filter(os.path.isfile, os.listdir(current_dir))
    print(current_dir)
    for file in files:
        if -1 != file.find("sort-by-date"):
            continue
        print("{}".format(file))
        print(os.path.getmtime(file))
        print(type(datetime.datetime.fromtimestamp(os.path.getmtime(file)).date()))
        date = datetime.datetime.fromtimestamp(
            os.path.getmtime(file)).date().strftime("%Y-%m-%d")
        print(date)
        if not os.path.exists(date):
            os.mkdir(date)
        new_path = current_dir+"/" + date+"/"+file
        print(new_path)
        old_path = current_dir+"/"+file
        print(old_path)
        os.rename(old_path, new_path)


if __name__ == "__main__":
    main()
