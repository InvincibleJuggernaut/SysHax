from tenfrom tensorflow.keras.models import Sequential, save_model, load_model
import numpy

def test_damage():
    loaded_model=load_model('/home/devops/Development/Hackathons/Gov-TechThon/Models/Damage_or_Undamaged_Model.h5')
    input=input_test