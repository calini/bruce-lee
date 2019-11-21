# Bruce Lee, replica of Alex's Chuck Norris party trick
import time
import sys
import os
import subprocess
from utils import getch

# Prompts
prompt = "Please Bruce, answer the following question:\n"
instructions = "Hello, I'm Bruce Lee. You can ask me anything, as long as you ask nicely:\n\"%s\" (without quotes)." % prompt[:-1]
wrong_prompt_message = "You have to ask nicely you idiot."
sorry_message = "I am sorry but I do not reply to the plebe."
next_question = "Ask another question (nicely)..."
DELAY = 0.2

def wait(delay):
    for t in "[====================]\n":
        time.sleep(delay)
        print("%s" % t, end='')
        sys.stdout.flush()

if __name__ == '__main__':

    # Print instructions
    print(instructions)

    while True:
        # Get a first character to assess admin mode
        c = getch()
        if c == ';':
            # If admin mode, start replacing input with the prompt, and use the input as answer
            print(prompt[0], end='')
            sys.stdout.flush()
            S = ""
            for ch in prompt[1:]:
                S += getch()
                print("%s" % ch, end='')
                sys.stdout.flush()
            answer = S.split(';')[0]
        else:
            # Otherwise print the first character, ignore the input and excuse yourself
            s = input(c)
            if c + s != prompt[:-1]:
                answer = wrong_prompt_message
            else:
                answer = sorry_message
        input()
        wait(DELAY)
        print(answer)
        # Use Mac's text to speech
        subprocess.call(['say', '-v', 'Daniel', answer])

        # Ask for another question
        print("\n%s" % next_question)