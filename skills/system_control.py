import os


def shutdown():

    os.system("shutdown /s /t 30")
    print("Shutdown command executed")


def restart():

    os.system("shutdown /r /t 30")
    print("Restart command executed")


def cancel_shutdown():

    os.system("shutdown /a")
    print("Shutdown cancelled")