from Drowsy.main import classify_state

def test_path1():
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.3}) == "NORMAL"

def test_path2():
    assert classify_state({"yawn_score": 0.8, "eye_score": 0.3}) == "DROWSY"

def test_path3():
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.9}) == "DROWSY"

def test_path4():
    assert classify_state({"yawn_score": 0.9, "eye_score": 0.95}) == "DROWSY"
