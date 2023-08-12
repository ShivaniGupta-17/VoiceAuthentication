import pickle
from models import matching

def matching_check_file(InputMFCC):
    with open("Voicerecognition.pkl","rb") as pkl4:
        data=pickle.load(pkl4)
        mini=None
        name=None
        for i in data:
            print(InputMFCC.shape)
            print(i,matching(InputMFCC,data[i]),"FINALMATCHES")
            value=matching(InputMFCC,data[i])
            if mini==None or value<mini:
                mini=value
                name=i
    return mini,name