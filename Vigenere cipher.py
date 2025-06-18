import sys


def vigenereEncrypter(keywordShiftList, textLetterNo, letterNo):
    textShift = keywordShiftList[textLetterNo - 1] + letterNo
    return textShift


def vigenereDecrypter(keywordShiftList, textLetterNo, letterNo):
    textShift = (letterNo - keywordShiftList[textLetterNo - 1])
    return textShift


EncOrDec = input('Enter \n1)Encrypt\n2)Decrypt\n3)Brute Force Keyword\n: ')
if EncOrDec not in ['1','2','3']:
    print('Invalid Input')
    sys.exit()
else:
    EncOrDec = int(EncOrDec)

text = input('Enter your text: ').upper()


def vigenere(EncOrDec, text):

    if EncOrDec == 3:
        while True:
            vigenere(2, text)
    keyword = input('Enter your keyword: ').upper()
    if keyword == 'X':
        sys.exit()

    global textCharacter, letterNoKeyword
    # Holds the number of shifts per letter in the keyword
    keywordShiftList = []
    # Holds the ascii no per letter in the text
    textOrdNoList = []
    # Holds the final word
    textShiftList = []
    startingPoint = ord('A')
    keywordLetterNo = 0
    # Breaking each letter of the keyword to add them to the shiftList by breaking the shift for each letter in regards to A (First letter of the alphabet)
    for letter in keyword:
        letterNoKeyword = ord(letter)
        shiftForLetter = letterNoKeyword - startingPoint
        keywordShiftList.append(shiftForLetter)
        keywordLetterNo = keywordLetterNo + 1

    textLetterNo = 0
    # Breaks each letter in the text
    for letter in text:
        if not letter.isalpha():
            textShiftList.append(letter)
        else:
            textLetterNo = textLetterNo + 1
            letterNo = ord(letter)
            textOrdNoList.append(letterNo)
            if EncOrDec == 1:
                textShift = vigenereEncrypter(keywordShiftList, textLetterNo, letterNo)
            elif EncOrDec == 2:
                textShift = vigenereDecrypter(keywordShiftList, textLetterNo, letterNo)
            else:
                print('Invalid Input')
            # Conditioning to remain the letters in the range A-Z in ascii table (65-90)
            if textShift < 65:
                textShift = textShift + 26
            elif textShift <= 90:
                textShift = textShift
            elif textShift > 90:
                textShift -= 26

            textCharacter = chr(textShift)
            textShiftList.append(textCharacter)
            # To break when the no.of letters in the text is exceeded by no.of letters in keyword
            if textLetterNo >= keywordLetterNo:
                textOrdNoList.clear()
                textLetterNo = 0
    print(''.join(textShiftList))
    print()


vigenere(EncOrDec, text)
