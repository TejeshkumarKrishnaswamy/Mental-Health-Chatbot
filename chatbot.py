def reply(msg):
 m=msg.lower()
 if "happy" in m:return "😊 Glad you're happy!"
 if "sad" in m:return "😔 I'm sorry you're feeling sad."
 if "angry" in m:return "😌 I understand you're angry."
 if "stress" in m or "frustrated" in m:return "💙 Take a deep breath. I'm here for you."
 return "🙂 Tell me more."
