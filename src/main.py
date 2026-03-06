from ui.lcd_controller import idle, thinking, show_text
import time

def main():
    idle()

    while True:
        question = input("> ")

        thinking()

        # temporary fake AI response
        response = "Thinking..."

        show_text(response)
        time.sleep(2)

        idle()


if __name__ == "__main__":
    main()
