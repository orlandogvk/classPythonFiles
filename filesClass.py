"""
Contador de palabras: actualizar el script anterior que lea un archivo de texto y retorne las 10 palabras más repetidas.
Usando clases, métodos, instancias y lo previamente visto en clase.

Made by Orlando Rodriguez
"""

from operator import itemgetter
import itertools


class Files:
    def __init__(self,file):
        self.file=file

    def fileWordCount(self):
        content_list = []
        words = []
        # We transform a file in a list
        content_list = self.file.read().replace("@", " ") \
            .replace(".", " ").replace("/", " ").replace("-", " ").replace("<", " ") \
            .replace(">", " ").replace(":", " ").replace("([", " ").replace("])", " ") \
            .replace("(", " ").replace(")", " ").replace(";", " ").split()

        # List depurated
        for i in content_list:
            if i.isalpha():
                words.append(i)

        # Lets create a dictionary
        wordsMessage = dict()
        for w in words:
            if w in wordsMessage:
                wordsMessage[w] = wordsMessage[w] + 1
            else:
                wordsMessage[w] = 1

        print("WORDS FILE TOP 10")

        # sort dictionary desc by value
        desc = dict(sorted(wordsMessage.items(), key=itemgetter(1), reverse=True))
        # select first 10 elements
        result = dict(itertools.islice(desc.items(), 10))
        count=1
        for key, value in result.items():
            print(count,".","{0} --> {1}".format(key, value))
            count+=1


#Validation and creating two instances
while True:
    try:
        #Input values
        file1 = input("Input a filename: ").strip()
        content1 = open(file1)

        #Object 1
        print("FIRST FILE")
        file_1=Files(content1)
        file_1.fileWordCount()

        print(" ")
        # Input values
        file2 = input("Input a filename: ").strip()
        content2 = open(file2)

        #Object 2
        print("SECOND FILE")
        file_2=Files(content2)
        file_2.fileWordCount()

        break
    except FileNotFoundError:
        print("filename unknown, try again!")


