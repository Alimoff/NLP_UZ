# from google.cloud import speech
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

# client = speech.SpeechClient()

# filename = "GPT.wav"

# with open(filename, "rb") as f:
#         mp3_data = f.read()

# audio_file = speech.RecognitionAudio(content=mp3_data)

# config = speech.RecognitionConfig(
#         # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         enable_automatic_punctuation = True,
#         language_code="en-US",
#     )
# #  operation = client.long_running_recognize(config=config, audio=audio)

# print("Waiting for operation to complete...")
# response = client.long_running_recognize(
#     config=config,
#     audio=audio_file
# )

# print(response)

# for result in response.results:
#         # The first alternative is the most likely one for this portion.
#     print("Transcript: {}".format(result.alternatives[0].transcript))
#     print("Confidence: {}".format(result.alternatives[0].confidence))



# import speech_recognition as sr 

# r = sr.Recognizer()


# with sr.Microphone() as source:
#     print("Say something")
#     audio = r.listen(source)
#     print("Done")


# text = r.recognize_google(audio,language='uz-UZ')   


# print(text)




# # Imports the Google Cloud client library
# from google.cloud import speech

# import os

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
# # Instantiates a client
# client = speech.SpeechClient()

# # The name of the audio file to transcribe
# gcs_uri = "GPT.wav"

# audio = speech.RecognitionAudio(uri=gcs_uri)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code="en-US",
# )

# # Detects speech in the audio file
# response = client.recognize(config=config, audio=audio)

# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))



# import os

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


# def transcribe_streaming(stream_file):
#     """Streams transcription of the given audio file."""
#     import io


#     from google.cloud import speech

#     client = speech.SpeechClient()

#     with io.open(stream_file, "rb") as audio_file:
#         content = audio_file.read()

#     # In practice, stream should be a generator yielding chunks of audio data.
#     stream = [content]

#     requests = (
#         speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
#     )

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#     )

#     streaming_config = speech.StreamingRecognitionConfig(config=config)

#     # streaming_recognize returns a generator.
#     responses = client.streaming_recognize(
#         config=streaming_config,
#         requests=requests,
#     )

#     for response in responses:
#         # Once the transcription has settled, the first result will contain the
#         # is_final result. The other results will be for subsequent portions of
#         # the audio.
#         for result in response.results:
#             print("Finished: {}".format(result.is_final))
#             print("Stability: {}".format(result.stability))
#             alternatives = result.alternatives
#             # The alternatives are ordered from most likely to least.
#             for alternative in alternatives:
#                 print("Confidence: {}".format(alternative.confidence))
#                 print("Transcript: {}".format(alternative.transcript))



# a = transcribe_streaming("RishiSunak.mp3")
# print(a)




# def transcribe_gcs(gcs_uri):
#     """Asynchronously transcribes the audio file specified by the gcs_uri."""
#     from google.cloud import speech
#     import os

#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

#     client = speech.SpeechClient()

#     audio = speech.RecognitionAudio(uri=gcs_uri)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#     )

#     operation = client.long_running_recognize(config=config, audio=audio)

#     print("Waiting for operation to complete...")
#     response = operation.result(timeout=90)

#     # Each result is for a consecutive portion of the audio. Iterate through
#     # them to get the transcripts for the entire audio file.
#     for result in response.results:
#         # The first alternative is the most likely one for this portion.
#         print("Transcript: {}".format(result.alternatives[0].transcript))
#         print("Confidence: {}".format(result.alternatives[0].confidence))

# transcribe_gcs("ummon.mp3")



# def transcribe_file(speech_file):
#     """Transcribe the given audio file."""
#     from google.cloud import speech
#     import io

#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


#     client = speech.SpeechClient()

#     with io.open(speech_file, "rb") as audio_file:
#         content = audio_file.read()

#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#     )

#     response = client.recognize(config=config, audio=audio)

#     # Each result is for a consecutive portion of the audio. Iterate through
#     # them to get the transcripts for the entire audio file.
#     for result in response.results:
#         # The first alternative is the most likely one for this portion.
#         print("Transcript: {}".format(result.alternatives[0].transcript))


# a = transcribe_file("ovoz.ogg")

# print(a)




def transcribe_streaming(stream_file):
    """Streams transcription of the given audio file."""
    import io
    from google.cloud import speech

    client = speech.SpeechClient()

    with io.open(stream_file, "rb") as audio_file:
        content = audio_file.read()

    # In practice, stream should be a generator yielding chunks of audio data.
    stream = [content]

    requests = (
        speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
    )

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44000,
        language_code="en-US",
    )

    streaming_config = speech.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    responses = client.streaming_recognize(
        config=streaming_config,
        requests=requests,
    )

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            print("Finished: {}".format(result.is_final))
            print("Stability: {}".format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print("Confidence: {}".format(alternative.confidence))
                print("Transcript: {}".format(alternative.transcript))

a  = transcribe_streaming("RishiSunak.mp3")
