from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotional_detect():
    """This code receives the text from HTML interface and
       runs emotional detector over it using emotion_detector
       function. The output shows scores various emotions 
       and dominant emotion
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to emotion_detect function and store the response
    response = emotion_detector(text_to_analyze)

    #return the respone
    return f"For the given statement, the system response is 'anger': {response['anger']}, " \
           f"'disgust': {response['disgust']}, 'fear': {response['fear']}, " \
           f"'joy': {response['joy']} and 'sadness': {response['sadness']}. " \
           f"The Dominant emotion is {response['dominant_emotion']}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
