# SongMoodClassifierApp

Machine Learning Model to Classify Mood of Songs

This application is being created for K3G Music Enterprises, it is a new music station that is planning to enable listeners to listen to music based on how they feel. We planned to use Machine learning to classify songs for this purpose. Acknowledging there are new songs added to their catalog on a daily basis, they intend to build a machine learning based classifier service which would classify songs as (Happy/Sad). In order to test feasibility, they wanted us to be able to build a classifier that would classify “any” Hindi song as Happy/Sad.

# Links

[Web Application](https://song-mood-pred-app.herokuapp.com/api)

[Summary Report](https://codelabs-preview.appspot.com/?file_id=1FDRGfPLQ7AscG0SiqKDy3gJfEz2h_J7-XwPDZKwpTOQ#6)

[Run the app locally](https://youtu.be/LRMoRKkJjfk)

[Presentation Video](https://youtu.be/6K_xV1CwTUc)

# Summary

In order to analyse and run this web application on local host please consider the following steps:
1. Run the preparepickle.ipynb file on jupyter.This notebook will create required pickle objects for classifying the mood of the lyrics
2. After creating the pickle objects run the Web app on command promt using command --> python api.py
3. You will receive a port on which the app is running, open the browser and go to url: https://localhost:portnumber/api to access the web page.
