def voicetoText (path):

    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.AudioFile(path) as source:
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
        except:
            print("Sorry we could not recognize This voice")

    return "You said : {}".format(text)

#for testing this function call the next line and any location of .wav sound .
#print(voicetoText("Put the path of the wav here"))    
