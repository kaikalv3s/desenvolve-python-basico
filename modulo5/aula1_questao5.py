import emoji

print("Emojis disponíveis:")
print(f"❤️ - :red_heart:")
print(f"👍 - :thumbs_up:")
print(f"🤔 - :thinking_face:")
print(f"🥳 - :partying_face:")
print()

frase_usuario = input("Digite uma frase e ela será emojizada:\n")

frase_emojizada = emoji.emojize(frase_usuario, language='alias')

print("Frase emojizada:")
print(frase_emojizada)