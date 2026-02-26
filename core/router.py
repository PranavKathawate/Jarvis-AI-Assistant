from skills.app_launcher import open_app
from skills.web_opener import open_website
from core.brain import ask_ai


def route_command(command):

    print("Routing:", command)

    command = command.lower()


    # website triggers
    if command.startswith(("open", "go to", "visit", "launch")):

        open_website(command)

        open_app(command)

        return


    # AI fallback
    response = ask_ai(command)

    print("Jarvis:", response)