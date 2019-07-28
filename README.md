- Visit python.org, Install latest version of python.
- pip install pyttsx3
- pip install speechRecognition
- pip install wikipedia
- If  "ImportError : No module   named PyAudio." error occurs:
  pip install PyAudio.(make sure that the latest version is installed.)
- If error related to buffer or "exception_on_overflow" occurs, related to pyaudio      module, then try lowering the default sample rate of the default audio device.
- If the listening and recognizing takes longer than usual then try noise suppression.    The "listen" function has problems with environment noise. 
  Use this ambient noise suppression/adjustment;  r.adjust_for_ambient_noise      (source, duration=5), in 'takeCommands()' function.
- A good speed internet connection is always a plus. 
