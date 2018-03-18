import speech_recognition as sr

#while True:
def listen():                               #adjust sample rate and chunk size according to your mic
    print("listening...")                           #my usb 44100          #512
    r = sr.Recognizer()                             #my web mic 16000      #128
    m=sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.energy_threshold = 500#1250#175#400
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        with open("/memory/sounds/records/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())#records data to be recognized later
        audio.pause_threshold = 0.65# the seconds of silence needed to stop listening
        
    #pick one by commenting out the other
    a =r.recognize_sphinx(audio)
    #a=r.recognize_google(audio)

    try:
        print(a)
    except sr.UnknownValueError:
        print("could not understand audio")
        listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("You're not connected for whatever reason...lets try again")


listen()
