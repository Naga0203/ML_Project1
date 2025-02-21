from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle

with open('savedmodels/model.pkl','rb') as file:
    model = pickle.load(file)

with open('savedmodels/scaler.pkl','rb') as file1:
    scaler = pickle.load(file1)
    

def pred(request):
    return render(request, 'home.html') 

def features(request):
    print("The features view is triggered") 
    return render(request, 'features.html')


def get_predictions(request):
    result = None 
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        pain_type = request.POST.get('pain-type')
        bp = request.POST.get('bp')
        cholesterol = request.POST.get('cholesterol')
        fbs = request.POST.get('fbs')
        ecg = request.POST.get('ecg')
        max_hr = request.POST.get('max_hr')
        depression = request.POST.get('depression')
        slope = request.POST.get('slope')
        vessels = request.POST.get('vessels')
        thal = request.POST.get('thal')
        history = request.POST.get('history')
        medication = request.POST.get('medication')
        smoking_and_alcohol = request.POST.get('Smoking_Alcohol')
        exercise_physical = request.POST.get('exercise_physical')       
        gender = int(1 if gender == 'Male' else 0)
        new_data = np.array([[age, gender, pain_type, bp, cholesterol, fbs, ecg,
                              max_hr, depression, slope, vessels, thal, history,
                              medication,smoking_and_alcohol,exercise_physical]])
        
        new_data = scaler.transform(new_data)
        prediction = model.predict(new_data)
        probability = model.predict_proba(new_data)[0, 1]
        
        if probability < 0.20:
            mes = 'Your Heart Health is Good and you are safe'
            
        
        elif probability > 0.20 and probability < 0.50:
            mes = 'You Need to Take care of your Heart Health '
        
        
        else:
            mes = "Your Heart health is in Danger please consult a Doctor"
        
        result = {
            'prediction': int(prediction[0]),
            'probability': probability,
            'message': mes
        }
        
        return render(request, 'result.html', {'result': result})
        
    return render(request, 'result.html',{'result': result})






