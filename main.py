from deepface import DeepFace
import json

def analyze_face_emotions(path_to_image):
	try:
		result = DeepFace.analyze(img_path=path_to_image, actions=['age', 'gender', 'race', 'dominant_race', 'dominant_emotion', 'emotion'])
		
		print(f'Age: {result.get("age")}')
		print(f'Gender: {result.get("gender")}')
		print(f'Race: {result.get("dominant_race")}')
		print(f'Emotions: {result.get("dominant_emotion")}')

        # write result in .json file
		with open('analyze_face_emotions.json', 'w') as file:
			json.dump(result, file, indent=4, ensure_ascii=False)

	except Exception as ex:
		return ex

def main():
	print("Please, type the name of the file. Or press enter to skip. Default name is img/1.jpg\n")
	path_to_image = input()
	if not path_to_image:
		path_to_image = 'img/1.jpg'

	analyze_face_emotions(path_to_image)

if __name__ == '__main__':
	main()