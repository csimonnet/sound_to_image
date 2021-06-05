import wave


class FileReader:

    def __init__(self, file_path):
        self.wave_read_object = wave.open(file_path, 'rb')

    def get_number_channels(self):
        return self.wave_read_object.getnchannels()
