import json
import os
import random
import time

WORDS_FILE = "words.txt"
SCORE_FILE = os.path.join("Data", "HS.json")


def load_words(words_file=WORDS_FILE):
    with open(words_file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def load_high_scores(score_file=SCORE_FILE):
    if not os.path.exists(score_file):
        return {}

    with open(score_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict) and "" in data and isinstance(data[""], dict):
        legacy_entry = data[""]
        if "High score" in legacy_entry or "words" in legacy_entry:
            return {
                str(legacy_entry.get("words", 0)): {
                    "High score": legacy_entry.get("High score", 0),
                    "words": legacy_entry.get("words", 0),
                }
            }

    return data if isinstance(data, dict) else {}


def update_high_scores(scores, word_count, elapsed_time):
    key = str(word_count)
    entry = scores.get(key)

    if entry is None:
        scores[key] = {"High score": elapsed_time, "words": word_count}
        return True

    if elapsed_time < entry.get("High score", float("inf")):
        entry["High score"] = elapsed_time
        entry["words"] = word_count
        return True

    return False


def save_high_scores(scores, score_file=SCORE_FILE):
    os.makedirs(os.path.dirname(score_file), exist_ok=True)
    with open(score_file, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=2)


def play_game():
    commands = load_words()
    while True:
        words = input("How many words do you want to type? \n")
        if words.isdigit() and int(words) > 0:
            break
        print("Please enter a valid number.")

    word_count = int(words)
    if word_count > len(commands):
        word_count = len(commands)

    high_scores = load_high_scores()

    input("Press Enter to ready")

    timea = time.time()
    completed = []
    mistakes = 0
    wdone = 0

    while wdone < word_count:
        rand = random.choice(commands)
        if rand in completed:
            continue

        print(f"Type: {rand}")
        input_txt = input("> ")

        if input_txt == rand:
            print("Correct!")
            completed.append(rand)
            wdone += 1
        else:
            print("You messed it up!")
            mistakes += 1

    timestop = time.time()
    full = timestop - timea

    if word_count > 10 and full < 5:
        print(f"You're fast! it took you only {full:.2f} seconds!")
    else:
        print(f"That took you {full:.2f} seconds to type that.")

    if update_high_scores(high_scores, word_count, full):
        print("You got a new high score!")
    else:
        current_best = high_scores.get(str(word_count), {}).get("High score")
        if current_best is not None:
            print(f"Your best for {word_count} words is {current_best:.2f} seconds.")

    save_high_scores(high_scores)
    print(f"You made {mistakes} mistakes.")
    input("Press Enter to exit")


if __name__ == "__main__":
    play_game()