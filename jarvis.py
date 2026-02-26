from core.speech import listen
from core.router import route
from config import ASSISTANT_NAME, VERSION
import time

def stream_output(text):
    print("Jarvis: ", end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

def main():
    print(f"{ASSISTANT_NAME} Version {VERSION} Online")

    while True:
        command = listen()

        if command.lower() in ["exit", "quit", "bye"]:
            stream_output("Shutting down.")
            break

        response = route(command)

        stream_output(response)

if __name__ == "__main__":
    main()