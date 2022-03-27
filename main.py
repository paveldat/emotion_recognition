from deepface import DeepFace
import json

def analyze_face_emotions():
	try:
		result = DeepFace.analyze(img_path='img/1.jpg', actions=['age', 'gender', 'race', 'emotion'])
		
		print(f'Age: {result.get("age")}')
		print(f'Gender: {result.get("gender")}')
		print('Race:')
        
		for k, v in result.get('race').items():
			print(f'{k} - {round(v, 2)}%')
            
		print('Emotions:')
        
		for k, v in result.get('emotion').items():
			print(f'{k} - {round(v, 2)}%')

        # write result in .json file
		with open('analyze_face_emotions.json', 'w') as file:
			json.dump(result, file, indent=4, ensure_ascii=False)

	except Exception as ex:
		return ex

def main():
	analyze_face_emotions()

if __name__ == '__main__':
	main()