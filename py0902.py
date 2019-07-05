
==================================================================================================================
Declare a class named PatientData that contains two attributes named height_inches and weight_pounds. 

Sample output for the given program with inputs: 63 115
Patient data (before): 0 in, 0 lbs
Patient data (after): 63 in, 115 lbs
==================================================================================================================


''' Your solution goes here '''
class PatientData:
    def __init__(self):
        self.height_inches = 0
        self.weight_pounds = 0
        
patient = PatientData()
print('Patient data (before):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')


patient.height_inches = input()
patient.weight_pounds = input()

print('Patient data (after):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')
