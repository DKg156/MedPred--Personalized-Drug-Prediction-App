# MedPred--Personalized-Drug-Prediction-App
This GUI app was developed in Python using Spyder IDE. Once trained on a dataset, it can predict a suitable drug for a patient by taking personalized clinical parameters like age, sex, blood pressure, etc. Users can either use inbuilt dataset or import custom datasets for new disease predictions. User can also check the accuracy of the trained model and load the dataset being used by the app. <br><br>

The project application is named MedPred. Coding of the app has been done in the programming language Python. All GUI of the app has been created with the help of built-in Tkinter module. The default dataset used for training the app model is retrieved from the Internet. Spyder IDE has been used for writing and testing the code of the app. It comes with the Anaconda package which needs to be downloaded from the official website of Anaconda. Python Libraries used for the project come pre-installed with Anaconda.<br>

Once Anaconda is installed, open Spyder IDE and import the project code with the dataset and image files. Ensure that dataset and images are in the same directory file that contains the code. The only task now is to run the code which can be done either from the IPython console or by clicking the Run button in Spyder.<br>

# Python Libraries Used
**1. Tkinter :** Built-in library in Python for GUI programming. This was used for placing buttons, labels, menu, entry boxes and various widgets inside Frames that control the flow of this app.<br>
**2. PIL :** Python Imaging Library. This is used to edit images and was used for setting background images for the app.<br>
**3. NumPy and Pandas :** Pandas is a popular library used for analyzing
datasets and NumPy is used for handling two-dimensional arrays.<br>
**4. Scikit-Learn :** It is a popular ML library containing several algorithms for classification, regression and other ML tasks. The Decision Tree classifier used for training the model is used from this library.<br>
14
**5. CSV :** Library for handling spreadsheet-like documents of comma-separated values (CSV) format.<br><br>

# Screenshots of the app
Home screen<br>
![image](https://user-images.githubusercontent.com/42437054/83779835-0fec0a80-a6aa-11ea-8305-8631d861e078.png)<br>
**Using in-built disease dataset**<br><br>
![image](https://user-images.githubusercontent.com/42437054/83780130-622d2b80-a6aa-11ea-9a6e-5e7f5ae84f7e.png) <br>
![image](https://user-images.githubusercontent.com/42437054/83780160-6bb69380-a6aa-11ea-88a5-9072246ff22b.png)<br>
![image](https://user-images.githubusercontent.com/42437054/83780729-2a72b380-a6ab-11ea-9c9a-42d38015739b.png)<br>
![image](https://user-images.githubusercontent.com/42437054/83781639-72dea100-a6ac-11ea-82b6-2de568454a73.png)<br>
**Loading the dataset and viewing accuracy of model**<br><br>
![image](https://user-images.githubusercontent.com/42437054/83781922-cc46d000-a6ac-11ea-8cd5-a55d09fb8ac7.png)<br>
![image](https://user-images.githubusercontent.com/42437054/83781937-d10b8400-a6ac-11ea-855a-391aa195b194.png)<br>
**Using a custom disease dataset**<br><br>
![image](https://user-images.githubusercontent.com/42437054/83782236-28a9ef80-a6ad-11ea-9121-5fc21f04eb5b.png)<br>
![image](https://user-images.githubusercontent.com/42437054/83782410-673faa00-a6ad-11ea-854d-f92b0e4617b1.png)<br>
**Viewing the custom dataset**<br><br>
![image](https://user-images.githubusercontent.com/42437054/83782774-91916780-a6ad-11ea-8d85-af2029ce0587.png)<br>
**Warnings and error messages that MedPred can show**<br><br>
When user tries to import dataset of format other than .csv<br>
![image](https://user-images.githubusercontent.com/42437054/83783342-bdace880-a6ad-11ea-99cb-66a21777f9a6.png)<br>
When user tries to train a model with a dataset of small size<br>
![image](https://user-images.githubusercontent.com/42437054/83783975-f220a480-a6ad-11ea-9248-44c1e01a2ee7.png)<br>
When the user enters incorrect format of Na-K levels for prediction<br><br>
![image](https://user-images.githubusercontent.com/42437054/83784416-15e3ea80-a6ae-11ea-967b-4ec2d82bb1fb.png)


