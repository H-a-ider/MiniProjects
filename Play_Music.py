from pygame import mixer
file = 'musicname.mp3' # file with path
mixer.init()
mixer.music.load(file)
mixer.music.play()