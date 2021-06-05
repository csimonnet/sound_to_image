# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sound_analyzer.file_reader


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_reader = sound_analyzer.file_reader.FileReader("./lerhargy.wav")
    print(file_reader.get_number_channels())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
