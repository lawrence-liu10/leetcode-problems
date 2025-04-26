import os

def create_solution(difficulty, number, title):
    difficulty = difficulty.lower()

    number_str = str(number).zfill(3)
    formatted_title = title.lower().replace(' ', '-')
    filename = f"{number_str}_{formatted_title}.py"

    filepath = os.path.join(difficulty, filename)

    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
    else:
        with open(filepath, 'w') as f:
            f.write(f"# {number_str}. {title.title()}\n")
            f.write(f"# Difficulty: {difficulty.capitalize()}\n\n")
            f.write(f"# Link: ")
        print(f"Created file: {filepath}")

if __name__ == "__main__":
    difficulty = input("easy/medium/hard: ")
    number = int(input("problem number: "))
    title = input("problem title: ")
    create_solution(difficulty, number, title)