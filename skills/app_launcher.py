import os


def open_app(command):

    command = command.replace("open", "").strip()

    try:

        os.system(f"start {command}")

        print(f"Opening {command}")

    except:

        print("App not found")