def detect_emotion(text):
 t=text.lower()
 if "happy" in t:return "Happy"
 if "sad" in t:return "Sad"
 if "angry" in t:return "Angry"
 if "stress" in t or "frustrated" in t:return "Frustrated"
 return "Neutral"
