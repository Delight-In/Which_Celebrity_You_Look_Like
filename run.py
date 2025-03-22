# Python script that runs two other Python scripts sequentially using the os.system() function. 
import os 

def execute_system():
    bash1 = 'python src/image_embedding.py'
    bash2 = 'python src/feature_extractor.py'

    os.system(bash1)
    os.system(bash2)
    print('Executed successfully!! Now run app.py')

if __name__ == '__main__':
    execute_system()