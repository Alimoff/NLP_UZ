from google.cloud import speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
client = speech.SpeechClient()

filename = "GPT.wav"

with open(filename, "rb") as f:
        mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)

config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        enable_automatic_punctuation = True,
        language_code="en-US",
    )
#  operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = client.long_running_recognize(
    config=config,
    audio=audio_file
)

print(response)

for result in response.results:
        # The first alternative is the most likely one for this portion.
    print("Transcript: {}".format(result.alternatives[0].transcript))
    print("Confidence: {}".format(result.alternatives[0].confidence))



# import speech_recognition as sr 

# r = sr.Recognizer()


# with sr.Microphone() as source:
#     print("Say something")
#     audio = r.listen(source)
#     print("Done")


# text = r.recognize_google(audio,language='uz-UZ')   


# print(text)
