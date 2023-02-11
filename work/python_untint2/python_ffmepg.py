import ffmpeg


prop = ffmpeg.probe('1.mp4')
n = prop['format']['duration']
print(n)
