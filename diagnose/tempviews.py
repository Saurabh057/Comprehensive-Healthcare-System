from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views

def showDiagnosis(request):

    diseaseNaiveBAyes = "Tuberculosis" #yash bhadkahv ithe functions madhun return kr
    accNaiveBayes = 100
    diseaseKnn = "TuberCulosis"
    accKnn = 95
    diseaseDecisionTree = "Asthma"
    accDecisionTree = 94

    symptoms = ["itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering"]


    disease = {
        'Naive Bayes Classifier' : [diseaseNaiveBAyes, accNaiveBayes],
        'K-Nearest Neighbors Algorithm' : [diseaseKnn, accKnn],
        'Decision Tree Classifier' : [diseaseDecisionTree, accDecisionTree]
    }

    choosenAlgorithm =  max(disease, key=lambda x : disease[x][1])

    chosen = {
        'choosenAlgorithm' : choosenAlgorithm,
        'choosenDisease' : disease[choosenAlgorithm][0],
        'chosenAcc' : disease[choosenAlgorithm][1]
    }

    context = {'chosen':chosen, 'disease': disease, 'symptoms':symptoms}

    return render(request, 'diagnose/diagnoseDash.html', context)