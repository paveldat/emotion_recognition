# Recognition of emotions from a photo
In this project I will analyze how you can find out age, gender, race and emotion from a photo.

## How to install
1. Clone this repository on your computer
`https://github.com/paveldat/emotion_recognition.git`
2. Install all the requirements
`run libraries.bat`
3. Run the program
`python main.py`
4. Write path to the image you want to analyze and press ENTER

## Result
<img src="https://github.com/paveldat/emotion_recognition/blob/main/img/1.jpg">

```
Age: 29
Gender: Woman
Race: black
Emotions: happy
```

More information you can find in "analyze_face_emotions.json"
```
{
    "age": 29,
    "region": {
        "x": 159,
        "y": 214,
        "w": 655,
        "h": 655
    },
    "gender": "Woman",
    "race": {
        "asian": 21.657051146030426,
        "indian": 15.542873740196228,
        "black": 40.841639041900635,
        "white": 2.237129956483841,
        "middle eastern": 1.8103785812854767,
        "latino hispanic": 17.910930514335632
    },
    "dominant_race": "black",
    "emotion": {
        "angry": 0.005997404163197863,
        "disgust": 9.302506100040701e-07,
        "fear": 3.2217927161702256,
        "happy": 91.00857484238448,
        "sad": 0.06716915304059946,
        "surprise": 0.6175690991349102,
        "neutral": 5.078888079060545
    },
    "dominant_emotion": "happy"
}
```