from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='91fdc33e-35f4-4b10-b05f-53af120c1aba',
    password='aIqlCWkHKKkO')

#print(json.dumps(text_to_speech.list_voices(), indent=2))
f = open("text.txt","r")

with open(join(dirname(__file__), 'output.wav'),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(f.read(), accept='audio/wav',
                                  voice="en-US_AllisonVoice").content)

print(" ")
f.close()
#print(json.dumps(text_to_speech.get_pronunciation('Watson', format='spr'), indent=2))

#print(json.dumps(text_to_speech.list_voice_models(), indent=2))
