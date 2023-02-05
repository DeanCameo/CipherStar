from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

# -------------------------- HOME ----------------------------------

def home(request):
    return render(request, 'encrypt/home.html')

# -------------------------- CAESAR ----------------------------------

def encrypt_text(request):
    if request.method == 'POST':
        text = request.POST['text']
        shift = int(request.POST['shift'])

        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
                if char.islower():
                    encrypted_text = encrypted_text + shift_char.lower()
                else:
                    encrypted_text = encrypted_text + shift_char
            else:
                encrypted_text = encrypted_text + char

        context = {'encrypted_text': encrypted_text, 'shift':shift}

        return render(request, 'encrypt/display.html', context)

    return render(request, 'encrypt/encrypt.html')


def caesar_decrypt(encrypted_text, shift):
    text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97)
            if char.isupper():
                shift_char = shift_char.upper()
            text = text + shift_char
        else:
            text = text + char
    return text


def decrypt(request):
    if request.method == 'POST':
        encrypted_text = request.POST['encrypted_text']
        shift = int(request.POST['shift'])
        text = caesar_decrypt(encrypted_text, shift)
        context = {'text': text, 'shift': shift}
        return render(request, 'encrypt/dec_display.html', context)
    else:
        return render(request, 'encrypt/decrypt.html')
