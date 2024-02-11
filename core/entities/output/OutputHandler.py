from colorama import init, Fore, Style

init(autoreset=True)  # config  only for windows


class OutputHandler:
    @staticmethod
    def format_message(type_message, message, color_type=Fore.RED, color_text=Fore.WHITE):
        character_limit = 100
        identification = 5
        formatted_message = f"{color_type} {type_message}: {message} {Style.RESET_ALL}"

        if len(formatted_message) > character_limit:
            line_one = formatted_message[:character_limit]
            remaining_text = formatted_message[character_limit:]

            sentences = remaining_text.split('\n')
            cleaned_sentences = [sentence.lstrip() for sentence in sentences if sentence]
            remaining_text = '\n'.join(cleaned_sentences)

            available_length = character_limit - len(type_message) - identification - 5

            lines = [f"{' ' * (len(type_message) + identification)}{remaining_text[i:i + available_length]}" for i in
                     range(0, len(remaining_text), available_length)]
            formatted_message = line_one+"\n"+'\n'.join(lines)

        top_line = f"{color_type}{'-' * character_limit} {Style.RESET_ALL}"
        bottom_line = f"{color_type}{'-' * character_limit} {Style.RESET_ALL}"
        return f"{top_line}\n{formatted_message}\n{bottom_line}"

    @staticmethod
    def success_message(message):
        print(OutputHandler.format_message("📟success📟", message, color_type=Fore.GREEN, color_text=Fore.GREEN))

    @staticmethod
    def information_message(message):
        print(OutputHandler.format_message("🏴️information🏴", message, color_text=Fore.LIGHTBLACK_EX, color_type=Fore.LIGHTBLACK_EX))

OutputHandler.success_message("A criação de pasta foi realizada com sucesso pasta 'teste/cae/teasdfasd'")
OutputHandler.success_message("O serviço do Google, oferecido sem custo financeiro, traduz instantaneamente palavras, frases e páginas da Web do português para mais de cem outros idiomas.")
OutputHandler.information_message("Olá! Sim, estou bem, obrigado! Como posso ajudar você hoje?")
OutputHandler.information_message("Certamente! Para que tema você gostaria de um texto informativo? Pode ser sobre ciência,tecnologia, saúde, meio ambiente, ou qualquer outro assunto específico de seu interesse. Por favor, forneça mais detalhes para que eu possa criar um texto informativo que atenda às suas expectativas.")

