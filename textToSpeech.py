def synthesizeText(text):
    import os
    from google.cloud import texttospeech_v1
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
    
    client = texttospeech_v1.TextToSpeechClient()
    input_text = texttospeech_v1.SynthesisInput(text='Bot dice ' + text)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="es-US",
        name="es-US-Standard-B",
        ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE)

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3)
    
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config})

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
    
    
    