# AI MED - Disease prediction and patient management system

## WEBSITE: https://smathur.pythonanywhere.com

## MOTIVATION:<br>
The COVID-19 pandemic has drastically reduced the routine visits made by the patients which includes the routine care for pregnant women, elderly patients and timely immunisation of the infants. Everything today is moving towards digitalization. Also, a major challenge faced by many healthcare organisations is the provision of quality medical services at affordable costs which implies proper diagnosis of the patient. Most of the people lack means to consult a doctor specialised in the field that they are looking for. The product proposed by us focuses on the methods by which we can overcome these challenges.

The product would reduce the chances of disease transmission and would also be convenient for both the patient and the doctor especially residing in high alert areas. This would also help to overcome the problem of deficiency of human resources in the health sector which is prevalent at several levels such as between regions, between rural and urban areas and between private and public sectors. This challenge is solved by providing the feature that doctors throughout the country can sign up at our portal thus providing the benefit of consulting the health care specialists in the respective fields and bridging the gap between different sections of the society.

## OVERVIEW:

The portal would provide an e-consultation facility to the patients. The patients can sign up at the portal. After logging in the patients would observe there are various sections that cater to their needs. A section for predicting the disease that they are likely to suffer from where they can fill a form by providing their details along with the symptoms witnessed. Based on the result of the prediction, the patients can search for the specialised doctors and share the prediction results with the selected doctor. 

The doctors across the country can register themselves on our portal specifying the fields that they have been working in. Once logged in then each doctor will receive notifications regarding the patients who have approached them along with their details including their symptoms. The doctor can provide a confirmation of the appointment and if required they can even provide the patient with the prescription that needs to be followed till the appointment date. This will help overcome the challenge of increased drop rate in the regular patient visits and also help patients to consult the doctors in case of emergency situations by fixing an appointment without the need to visit the hospital regarding the same. 

## PRODUCT FEATURES:

### 1.	REGISTRATION/ LOGIN: <br>
The patients and the doctors need to register on the portal before they can start accessing the functionalities which are available to them. After login, they will be assigned a token to make sure that they are authenticated users.

<b>RESPONSE SEQUENCE:</b>

Registration:

1.	Users would click on the register button.
2.	The user will be presented with a form in which they will fill all the required details.
3.	The System will check the validity of the password and email followed by whether the data is valid or not 
4.	A user account will be created if all the details are valid.


Login:

1.	User will Click on the login button.
2.	The user will be presented with a form in which they will enter their email and password
3.	The System will check the validity of the password and email followed by whether the data is valid or not. 
4.	If details are valid, Then the user will be logged in.


### 2.	DISEASE PREDICTION AND DOCTOR SUGGESTION:<br>
Patients fill their symptoms in a form and according to that the system predicts the disease through machine learning models. The models are trained using various algorithms such as:

DECISION TREES:

It is used for classification as well as regression tasks. It is a flowchart-like structure where each internal node represents a test on the various symptoms entered by the user and each leaf node represents the class label i.e. the diseases.

NAIVE BAYES:

It is a classifier which works on Bayes theorem. The prediction of membership probabilities is made for every class of disease such as the given set of symptoms is associated with a given disease (eg: fungal infection).
The patient can search for the concerned doctor within our database or any other doctor based on their location.

<b>RESPONSE SEQUENCE:</b>

1.	After logging into the portal, the patient will have to navigate to the tab which requires the patient to fill the symptoms.
2.	The patient would have to select the appropriate symptom from the list so offered.
3.	Based upon these symptoms, the patient will be provided a predicted disease using various Machine Learning models.
4.	The result of prediction is displayed on the screen.
5.	Based on the disease predicted, the patient would be shown a list of doctors.
6.	He/she would have an option to choose the doctor. Suppose the patient chooses a doctor, an appointment request would be sent to that particular doctor.


## 3.	APPOINTMENT CONFIRMATION:<br>
The doctor can set up an appointment with the patient for further consultation and diagnosis if he/she feels the need for the same. This will also replace the manual procedures of recording the appointment dates thereby increasing the reliability, efficiency and performance of the product. 

<b> RESPONSE SEQUENCE:</b><br>
1.	The doctor would receive an appointment request from a patient.
2.	The doctor would send the appointment confirmation.


## 4.	PRESCRIPTION:
Doctors can send a prescription which can then be viewed by the patient. Depending upon the prediction, the doctor can decide whether to keep the further follow ups in an offline mode by fixing the appointment through the portal and asking the patient to follow the prescription till the next check-up or a course of the medicine for a certain period suggested is enough to recover from the disease.

<b>RESPONSE SEQUENCE:</b><br>
1.	The doctor would view the predicted disease and other details of the patient and send him a prescription for the same.
2.	The patient would be able to view the prescription sent by the doctor.


## 5.	QUESTION AND ANSWER (QnA):<br>
The patients and doctors are provided with a chat functionality for any active treatment. This facility helps the concerned patient and doctor to communicate with one another when it comes to fixing appointment dates or telling the precautions that the patient needs to take in case of emergency.

<b> RESPONSE SEQUENCE:</b>

1.	The patient and the doctor would be able to chat via the QnA section.
2.	The patient can ask a question to the doctor and the doctor can respond to it.


## 6.	CHANGE PASSWORD: <br>
The patients and doctors are provided with a functionality to change their password. They would have to logout and then on the login page they would find an option by clicking on which they can change their password.

<b>RESPONSE SEQUENCE:</b>

1.	The patient and the doctor would have to logout.
2.	They would find the change password option on the login page.


## USER INTERFACES:<br>
### 1.	Patient interface:<br>
•	The patient would see a register button upon clicking on which a registration form would open.<br>
•	After registration, the patient would have a Login button which on clicking would open a login form.<br>
•	After the authentication is done, the patient would be able to view all the options that our portal provides and the basic instructions.<br>
•	A tab for disease prediction would open on clicking the predict disease button. This would contain a form which would ask the patient to select the symptoms he/she is witnessing.<br>
•	The Patient would have a button option to search for the concerned doctor once the disease has been predicted .It would show a list of doctors whom the patient can consult by asking for an appointment. The patient would receive a notification once the doctor has confirmed the appointment.<br>
•	A tab is provided to review the prescription sent by the doctor which the patient needs to follow up with until the next appointment. <br>
•	There would also be an option for QnA with the doctor.<br>


### 2.	Doctor interface:<br>
•	The doctor would see a register as a doctor button upon clicking on which a registration form would open (in case if he/she has not registered before).<br>
•	After registration, the doctor would have a Login button which on clicking would open a login form.<br>
•	After the authentication is done, the doctor would be able to view all the options that our portal provides and the basic instructions.<br>
•	A tab for active patient’s details would open on clicking the view details button. This would contain all the details of the active patient such as age, weight etc.<br>
•	There will also be another tab to review appointment requests of patients in which the doctor would have an option to schedule an appointment for the patient.<br>
•	The doctor can also prescribe patients appropriate medication based on the disease predicted. Also there will be an option to update or modify the prescriptions as in some cases with time dosage of medicine to be taken changes.<br>
