import webbrowser
import difflib


# list of popular websites
KNOWN_SITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "instagram": "https://instagram.com",
    "facebook": "https://facebook.com",
    "twitter": "https://twitter.com",
    "linkedin": "https://linkedin.com",
    "chatgpt": "https://chat.openai.com"
}


def find_best_match(word):

    matches = difflib.get_close_matches(
        word,
        KNOWN_SITES.keys(),
        n=1,
        cutoff=0.6
    )

    return matches[0] if matches else word


def open_website(command):

    command = command.lower()

    # remove trigger words
    for trigger in ["open", "go to", "visit", "launch"]:
        command = command.replace(trigger, "")

    site_name = command.strip()

    corrected = find_best_match(site_name)

    if corrected in KNOWN_SITES:

        url = KNOWN_SITES[corrected]

    else:

        url = "https://" + corrected + ".com"

    webbrowser.open(url)

    print("Opening", corrected)