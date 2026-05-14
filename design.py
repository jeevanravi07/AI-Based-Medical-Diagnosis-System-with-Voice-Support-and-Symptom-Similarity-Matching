import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr

# Disease database
disease_data = {
    "Flu": ["fever", "cough", "body pain"],
    "Viral Fever": ["fever", "weakness", "body pain"],
    "Common Cold": ["cold", "sneezing", "sore throat"],
    "Migraine": ["headache", "nausea", "light sensitivity"],
    "Food Poisoning": ["vomiting", "stomach pain", "diarrhea"],
    "Asthma": ["chest pain", "breathing problem", "wheezing"],
    "Diabetes": ["thirst", "frequent urination", "fatigue"],
    "Anemia": ["fatigue", "pale skin", "dizziness"],
    "Arthritis": ["joint pain", "swelling", "stiffness"],
    "Allergy": ["itching", "rash", "sneezing"],
    "Hyperthyroidism": ["weight loss", "excess sweating", "rapid heartbeat"],
    "Hypothyroidism": ["weight gain", "tiredness", "dry skin"],
    "Tonsillitis": ["sore throat", "fever", "swollen glands"],
    "Gastroenteritis": ["diarrhea", "dehydration", "stomach cramps"],
    "Muscle Strain": ["back pain", "stiffness", "muscle pain"]
}
disease_info = {

    "Flu": {
        "definition": "Flu is a viral infection affecting the respiratory system.",
        "symptoms": "Fever, cough, body pain, weakness.",
        "prevention": "Wash hands, avoid close contact, maintain immunity.",
        "danger": "Can be serious for elderly and weak immunity.",
        "treatment": "Rest, warm fluids, fever medication.",
        "duration": "Usually lasts 5 to 7 days.",
        "spread": "Spreads through cough and sneezing."
    },

    "Viral Fever": {
        "definition": "Viral fever is caused by viral infection leading to high temperature.",
        "symptoms": "Fever, weakness, body pain.",
        "prevention": "Maintain hygiene and strong immunity.",
        "danger": "Usually mild but monitor temperature.",
        "treatment": "Rest, hydration and fever control medicine.",
        "duration": "Lasts 3 to 7 days.",
        "spread": "Can spread depending on virus type."
    },

    "Common Cold": {
        "definition": "Common cold is a mild viral respiratory infection.",
        "symptoms": "Sneezing, sore throat, mild fever.",
        "prevention": "Avoid cold exposure and maintain hygiene.",
        "danger": "Usually not dangerous.",
        "treatment": "Rest and warm fluids.",
        "duration": "Lasts 5 to 7 days.",
        "spread": "Spreads through droplets."
    },

    "Migraine": {
        "definition": "Migraine is a neurological condition causing severe headaches.",
        "symptoms": "Headache, nausea, light sensitivity.",
        "prevention": "Avoid stress and maintain sleep routine.",
        "danger": "Not life-threatening but painful.",
        "treatment": "Pain relievers and rest in dark room.",
        "duration": "May last hours to days.",
        "spread": "Not contagious."
    },

    "Food Poisoning": {
        "definition": "Food poisoning is illness caused by contaminated food.",
        "symptoms": "Vomiting, diarrhea, stomach pain.",
        "prevention": "Eat fresh food and maintain food hygiene.",
        "danger": "Can cause dehydration.",
        "treatment": "Drink ORS and rest.",
        "duration": "Usually 1 to 3 days.",
        "spread": "Not contagious, but contaminated food spreads bacteria."
    },

    "Asthma": {
        "definition": "Asthma is a chronic respiratory condition.",
        "symptoms": "Breathing difficulty, chest tightness, wheezing.",
        "prevention": "Avoid dust and allergens.",
        "danger": "Severe attacks can be dangerous.",
        "treatment": "Use inhaler and medication.",
        "duration": "Long-term condition.",
        "spread": "Not contagious."
    },

    "Diabetes": {
        "definition": "Diabetes is a condition with high blood sugar levels.",
        "symptoms": "Excess thirst, frequent urination, fatigue.",
        "prevention": "Healthy diet and regular exercise.",
        "danger": "Can cause heart and kidney problems.",
        "treatment": "Blood sugar control and medication.",
        "duration": "Long-term condition.",
        "spread": "Not contagious."
    },

    "Anemia": {
        "definition": "Anemia is a condition with low red blood cells.",
        "symptoms": "Fatigue, pale skin, dizziness.",
        "prevention": "Iron-rich diet.",
        "danger": "Can cause weakness.",
        "treatment": "Iron supplements.",
        "duration": "Depends on treatment.",
        "spread": "Not contagious."
    },

    "Arthritis": {
        "definition": "Arthritis is inflammation of joints.",
        "symptoms": "Joint pain, swelling, stiffness.",
        "prevention": "Maintain healthy weight and exercise.",
        "danger": "Can reduce mobility.",
        "treatment": "Pain relief medicine and therapy.",
        "duration": "Long-term condition.",
        "spread": "Not contagious."
    },

    "Allergy": {
        "definition": "Allergy is immune reaction to substances.",
        "symptoms": "Itching, rash, sneezing.",
        "prevention": "Avoid allergen triggers.",
        "danger": "Severe allergy can cause breathing issue.",
        "treatment": "Antihistamines.",
        "duration": "Depends on exposure.",
        "spread": "Not contagious."
    },

    "Hyperthyroidism": {
        "definition": "Hyperthyroidism is overactive thyroid condition.",
        "symptoms": "Weight loss, sweating, rapid heartbeat.",
        "prevention": "Regular thyroid checkup.",
        "danger": "Can affect heart.",
        "treatment": "Medication and doctor supervision.",
        "duration": "Long-term management.",
        "spread": "Not contagious."
    },

    "Hypothyroidism": {
        "definition": "Hypothyroidism is underactive thyroid condition.",
        "symptoms": "Weight gain, tiredness, dry skin.",
        "prevention": "Regular health checkups.",
        "danger": "Can affect metabolism.",
        "treatment": "Thyroid hormone replacement.",
        "duration": "Long-term treatment.",
        "spread": "Not contagious."
    },

    "Tonsillitis": {
        "definition": "Tonsillitis is inflammation of tonsils.",
        "symptoms": "Sore throat, fever, swollen glands.",
        "prevention": "Maintain hygiene.",
        "danger": "May cause difficulty swallowing.",
        "treatment": "Warm salt water gargle and medicine.",
        "duration": "Usually 3 to 5 days.",
        "spread": "Can spread if viral."
    },

    "Gastroenteritis": {
        "definition": "Gastroenteritis is stomach and intestine infection.",
        "symptoms": "Diarrhea, dehydration, stomach cramps.",
        "prevention": "Clean water and food hygiene.",
        "danger": "Can cause severe dehydration.",
        "treatment": "ORS and rest.",
        "duration": "2 to 5 days.",
        "spread": "Can spread through contaminated food."
    },

    "Muscle Strain": {
        "definition": "Muscle strain is injury due to overstretching.",
        "symptoms": "Back pain, stiffness, muscle pain.",
        "prevention": "Proper warm-up before exercise.",
        "danger": "Not dangerous but painful.",
        "treatment": "Rest and ice application.",
        "duration": "Few days to weeks.",
        "spread": "Not contagious."
    }

}

def take_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "🎤 Listening...\n")
        root.update()

        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)

            symptom_entry.delete(0, tk.END)
            symptom_entry.insert(0, text)

            result_box.insert(tk.END, f"You said: {text}\n")

        except:
            result_box.insert(tk.END, "Sorry, could not understand.\n")

def predict_disease():
    user_input = symptom_entry.get().lower()
    results = []

    for disease, symptoms in disease_data.items():
        match_count = 0
        for symptom in symptoms:
            if symptom in user_input:
                match_count += 1

        if match_count > 0:
            confidence = (match_count / len(symptoms)) * 100
            results.append((disease, confidence))

    results.sort(key=lambda x: x[1], reverse=True)

    result_box.delete("1.0", tk.END)

    if results:
        result_box.insert(tk.END, "🩺 Diagnosis Result\n\n")
        for disease, confidence in results[:3]:
            result_box.insert(tk.END, f"{disease} - Confidence: {confidence:.0f}%\n")
    else:
        result_box.insert(tk.END, "No matching disease found.\n")

def clear_all():
    symptom_entry.delete(0, tk.END)
    result_box.delete("1.0", tk.END)
def ai_assist():
    question = symptom_entry.get().lower()
    result_box.delete("1.0", tk.END)

    for disease in disease_info:
        if disease.lower() in question:

            info = disease_info[disease]

            if "what is" in question:
                result_box.insert(tk.END, info["definition"])

            elif "symptom" in question:
                result_box.insert(tk.END, info["symptoms"])

            elif "prevent" in question or "avoid" in question:
                result_box.insert(tk.END, info["prevention"])

            elif "danger" in question or "serious" in question:
                result_box.insert(tk.END, info["danger"])

            elif "treat" in question or "do" in question:
                result_box.insert(tk.END, info["treatment"])

            elif "how long" in question or "duration" in question:
                result_box.insert(tk.END, info["duration"])

            elif "spread" in question:
                result_box.insert(tk.END, info["spread"])

            else:
                result_box.insert(tk.END, info["definition"])

            return

    result_box.insert(tk.END, "ASK ANYTHING ABOUT THIS DISEASE")

# Create window
root = tk.Tk()
root.title("AI Medical Diagnosis System")
root.geometry("650x500")
root.configure(bg="#1e3d59")

# Title
title = tk.Label(root, text="AI Medical Diagnosis Assistant",
                 font=("Helvetica", 20, "bold"),
                 bg="#1e3d59",
                 fg="white")
title.pack(pady=20)

# Symptom input label
input_label = tk.Label(root, text="Enter Your Symptoms:",
                       font=("Helvetica", 12),
                       bg="#1e3d59",
                       fg="white")
input_label.pack()

# Entry box
symptom_entry = tk.Entry(root, width=60, font=("Helvetica", 12))
symptom_entry.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e3d59")
button_frame.pack(pady=10)

# Predict button
predict_btn = tk.Button(button_frame,
                        text="Predict Disease",
                        command=predict_disease,
                        font=("Helvetica", 12, "bold"),
                        bg="#4CAF50",
                        fg="white",
                        width=18)
predict_btn.grid(row=0, column=0, padx=10)

# Clear button
clear_btn = tk.Button(button_frame,
                      text="Clear",
                      command=clear_all,
                      font=("Helvetica", 12, "bold"),
                      bg="#f44336",
                      fg="white",
                      width=10)
clear_btn.grid(row=0, column=1, padx=10)
voice_btn = tk.Button(button_frame,
                      text="🎤 Speak",
                      command=take_voice_input,
                      font=("Helvetica", 12, "bold"),
                      bg="#2196F3",
                      fg="white",
                      width=10)
voice_btn.grid(row=0, column=2, padx=10)
assist_btn = tk.Button(button_frame,
                       text="🤖 AI Assist",
                       command=ai_assist,
                       font=("Helvetica", 12, "bold"),
                       bg="#9C27B0",
                       fg="white",
                       width=12)
assist_btn.grid(row=0, column=3, padx=10)


# Result box (scrollable)
result_box = scrolledtext.ScrolledText(root,
                                       width=70,
                                       height=10,
                                       font=("Helvetica", 12))
result_box.pack(pady=20)

# Run app
root.mainloop()
