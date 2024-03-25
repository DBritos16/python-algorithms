def palindrome_reorder(text):
    
    text_trim = text.replace(" ", "").lower()
    text_reversed = text_trim[::-1]

    if text_trim == text_reversed:
        return text_reversed
    else:
        return 'NO SOLUTION'



assert palindrome_reorder("anita lava la tina") == "anita lava la tina", "Error en el caso de prueba"