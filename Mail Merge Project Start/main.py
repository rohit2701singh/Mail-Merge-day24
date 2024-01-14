PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()   # read all the lines from a file and return them as a list of strings, ['Aang\n', 'Zuko\n', 'Appa\n', ...]

with open("./Input/Letters/starting_letter.txt") as letter:
    sending_letter_template = letter.read()

    for name in name_list:
        stripped_invitee_name = name.strip()    # remove whitespace
        name_shifted_letter = sending_letter_template.replace(PLACEHOLDER, f"{stripped_invitee_name}")

        with open(f"./Output/ReadyToSend/letter_for_{stripped_invitee_name}.txt", "w") as send_ready:
            send_ready.write(name_shifted_letter)
