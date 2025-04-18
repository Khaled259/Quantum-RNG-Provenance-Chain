import numpy as np
import joblib

def test_model_load():
    model = joblib.load('../ai/model.pkl')
    pred = model.predict([np.zeros(256)])
    assert pred[0] in {0,1}
