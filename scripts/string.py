# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 10:22:36 2022

@author: Mateusz
"""
quote='A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one','1'))
print(quote.replace('both', '2'))
print(quote.split(' '))
print(quote.isalnum())
print(quote.isalpha())
print(quote.isdecimal())
print(quote.isdigit())


drive = 'c:\\'
folder = 'github\\Mateusz.Cikavy\\'
file = 'functionsString.py'
path = drive + folder + file
print(path)
JustText = r"text with\nnewline"
print(JustText)
Text='Mc Donald\'s'
print(Text)


firstName ="Kasia"
familyName="Sowa"
lastName="Mrugała"
newName=firstName+ " " + familyName + " " + lastName
print(newName, sep="\ ")


music="\n\"Universal Fanfare\" Jerry Goldsmith \n\"Happy Together\" Garry Bonner \n\"I'm a Man\" Steve Winwood"
print(music)

print('(/(/')
print('-.-')


somethingLikeNumber='1000'
print(int(somethingLikeNumber) + 1)
print(somethingLikeNumber + str(1))


article='''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution To Cinema. In 1998, they were awarded the AFI Star Award by the American Film Institute. Many sketches from their TV show and films are well-known and widely quoted. Both Holy Grail and Life of Brian are frequently ranked in lists of greatest comedy films. In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]'''
print(article.upper())
print(article.lower().replace('monty','flying'))
print(article.split( ))
python=article.find('Python')
print("word python appears", python ,"times")

print("to print the \\ you need to put \\ twice in your text like this:\\\\")
print("The best hits of '80s!!!")
print('The best hits of \'80s!!!')

amountPLN=234
USD=3.65
EUR=4.23
# print("cur"+" "+"exchange"+" " +"amount")
# print("USD",USD, + amountPLN/USD, sep="\t")
# print("EUR",EUR, + amountPLN/EUR, sep="\t")

print('cur','\texchange','amount')
print('USD',"\t",3.65,"\t",amountPLN/3.65)
print('EUR','\t',4.23,"\t",amountPLN/4.23)


ValueAsText='123.45'
factor=1.23
print("value is",ValueAsText,"factor is", factor, "value*factor=", float(ValueAsText)*factor)