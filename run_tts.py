from TTS.api import TTS

# Init TTS with the right model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True, gpu=False)

# Run TTS
tts.tts_to_file(
    text="hello i am atharv, i tried to clone the voice of aman verasia. hello this is voice check, this is check second i know it feels like it did not cloned the voice instead it is converting text to speech.",
    speaker_wav="Advent of Code Day 2： Solving Puzzles Together LIVE! [G_yezeuMJl4].wav",
    language="en",
    file_path="test02.wav"
)
