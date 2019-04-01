import os

from fnmatch import fnmatch


TRAIN = 'G:\ISMIR2004\ismir_train\\'
TEST = 'G:\ISMIR2004\ismir_testrestructure\\'
ISMIR_COMBINED = 'G:\ISMIR2004\ismir_combined\\'


f = open('id_01_resample_mp3_to_wav.bat', 'w')
file_path_string = []
script_line = []
for path, subdirs, files in sorted(os.walk(ISMIR_COMBINED,topdown=False)):
    for name in sorted(files):
        if fnmatch(name, "*.mp3"): #*.mp3 au"
            file_path_string = path + '\\' + name
            script_line = 'ffmpeg -y -i ' + file_path_string + ' -ab 128k -acodec pcm_s16le -ac 1 -ar 22050 ' + file_path_string.replace('.mp3', '.wav') + '\n'
            f.write(script_line)

