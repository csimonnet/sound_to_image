import wave


def read_sound_file(file_path):
    wave_read_object = wave.open(file_path, 'rb')
    print(wave_read_object.getnchannels())
    wave_read_object.close()
