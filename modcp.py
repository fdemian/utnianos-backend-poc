import argparse
from api.scripts.add_user import add_user
from api.dataloading.courses import load_courses
from api.dataloading.career_plans import load_career_plans

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Moderator control panel.')
    parser.add_argument('--command', metavar='c', type=str, nargs=1,
                        default='User', help='Command ')
    parser.add_argument('--file', metavar='f', type=str, nargs=1,
                        default='', help='File ')
    args = parser.parse_args()
    program_command = args.command[0]
    program_file = args.file[0]

    if program_command == None:
        program_command = "User"

    command = None
    prompt = ''
    continue_execution = True
    command_heading = ''

    if program_command == "User":
        command = add_user
        prompt = "Do you wish to continue adding users?" + " (Y/N) "
        command_heading = "Adding a user"

    if program_command == "Courses":
        command = load_courses
        prompt = "Do you wish to continue adding courses?"
        command_heading = "Adding courses"

    if program_command == "CareerPlans":
        command = load_career_plans
        prompt = "Do you wish to continue adding career plans?"
        command_heading = "Adding career plans."


    print(command_heading)
    print("====================================")

    # Execute command in a loop until the user is done
    while continue_execution:
        command(program_file)
        confirmation = input(prompt)
        if confirmation.strip() == "N":
            continue_execution = False
