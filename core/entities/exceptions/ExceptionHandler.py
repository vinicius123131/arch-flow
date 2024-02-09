from colorama import init, Fore, Style

init(autoreset=True)  # config  only for windows


class ExceptionHandler(Exception):
    def __init__(self, type_error, message, color_type=Fore.RED, color_text=Fore.WHITE):
        super().__init__(message)
        self.type_error = type_error
        self.color_type = color_type
        self.color_text = color_text

    def __str__(self):
        character_limit = 100
        identification = 3
        formatted_message = f"{self.color_type} {self.type_error}: {self.args[0]} {Style.RESET_ALL}"

        if len(formatted_message) > character_limit:
            line_one = formatted_message[:character_limit]
            remaining_text = formatted_message[character_limit:]

            available_length = character_limit - len(self.type_error) - identification - 5

            lines = [f"{' ' * (len(self.type_error) + identification)}{remaining_text[i:i + available_length]}" for i in
                     range(0, len(remaining_text), available_length)]
            formatted_message = line_one+"\n"+'\n'.join(lines)

        top_line = f"{self.color_type}{'-' * character_limit} {Style.RESET_ALL}"
        bottom_line = f"{self.color_type}{'-' * character_limit} {Style.RESET_ALL}"
        return f"{top_line}\n{formatted_message}\n{bottom_line}"
