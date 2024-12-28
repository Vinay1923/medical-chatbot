from flask import Flask, render_template, request

app = Flask()

# Dummy data for the application
symptoms_data = {
    'fever': {'diseases': ['Malaria', 'Typhoid'], 'remedies': ['Paracetamol', 'Hydration'], 'specialists': ['General Physician'], 'diets': ['Light Soup', 'Water']},
    'cough': {'diseases': ['Cold', 'Flu'], 'remedies': ['Cough Syrup', 'Honey'], 'specialists': ['Pulmonologist'], 'diets': ['Ginger Tea', 'Honey Water']},
    'headache': {'diseases': ['Migraine', 'Tension Headache'], 'remedies': ['Painkiller', 'Rest'], 'specialists': ['Neurologist'], 'diets': ['Water', 'Balanced Diet']},
}

@app.route('/', methods=['GET', 'POST'])
def index():
    diseases = []
    remedies = []
    specialists = []
    diets = []
    
    if request.method == 'POST':
        selected_symptoms = request.form.getlist('symptoms')
        
        for symptom in selected_symptoms:
            if symptom in symptoms_data:
                diseases.extend(symptoms_data[symptom]['diseases'])
                remedies.extend(symptoms_data[symptom]['remedies'])
                specialists.extend(symptoms_data[symptom]['specialists'])
                diets.extend(symptoms_data[symptom]['diets'])
        
        # Remove duplicates
        diseases = list(set(diseases))
        remedies = list(set(remedies))
        specialists = list(set(specialists))
        diets = list(set(diets))
        
    return render_template('index.html', symptoms=symptoms_data.keys(), diseases=diseases, remedies=remedies, specialists=specialists, diets=diets)

if __name__ == '__main__':
    app.run(debug=True)
