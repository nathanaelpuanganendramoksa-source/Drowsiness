from Drowsy.main import classify_state

def test_yawn_condition_false():
    assert classify_state({"yawn_score": 0.69, "eye_score": 0.2}) == "NORMAL"

def test_yawn_condition_true():
    assert classify_state({"yawn_score": 0.71, "eye_score": 0.2}) == "DROWSY"

def test_eye_condition_false():
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.79}) == "NORMAL"

def test_eye_condition_true():
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.81}) == "DROWSY"
