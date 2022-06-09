from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0
print(detect('ನನಗೆ ಬೇಕು'))