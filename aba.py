def aba_translate(s):
    translated = ''
    vowels = 'aeiouAEIOU'
    for ch in s:
        if ch in vowels:
            translated += ch + 'b' + ch.lower()
        else:
            translated += ch
    return translated

print(aba_translate('Cats and dogs'))
