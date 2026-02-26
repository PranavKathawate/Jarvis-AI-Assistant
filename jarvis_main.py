import threading

from core.wake_word import start_wake_word
from core.listener import start_listening
from core.router import route_command

MODE = "chat"


def chat_mode():
    global MODE

    print("\nChat Mode Active\n")

    while MODE == "chat":

        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Chat Mode...\n")
            break

        route_command(user_input)


def voice_mode():
    global MODE

    print("\nVoice Mode Active (waiting for 'hey jarvis')\n")

    # Wake word loop already handled inside this
    start_wake_word()


def wake_word_switch():
    global MODE
    from core.wake_word import detect_wake_word_only

    while True:
        detected = detect_wake_word_only()

        if detected and MODE == "chat":
            print("\nWake word detected. Switching to Voice Mode...\n")
            MODE = "voice"
            voice_mode()


def start_jarvis():
    global MODE

    while True:

        print("\nSelect Mode:")
        print("1. Chat Mode")
        print("2. Voice Mode")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            MODE = "chat"

            # Start wake listener in background only once
            wake_thread = threading.Thread(
                target=wake_word_switch,
                daemon=True
            )
            wake_thread.start()

            chat_mode()

        elif choice == "2":

            MODE = "voice"
            voice_mode()

        else:
            print("Invalid choice. Please enter 1 or 2.\n")
            continue

        # After exiting mode, return to menu
        MODE = "chat"