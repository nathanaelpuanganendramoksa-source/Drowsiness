from Drowsy.main import classify_state

def test_ep_normal():
    assert classify_state({"yawn_score": 0.3, "eye_score": 0.3}) == "NORMAL"

def test_ep_drowsy():
    assert classify_state({"yawn_score": 0.85, "eye_score": 0.1}) == "DROWSY"

def test_bva_thresholds():
    # Yawn
    assert classify_state({"yawn_score": 0.69, "eye_score": 0.2}) == "NORMAL"
    assert classify_state({"yawn_score": 0.71, "eye_score": 0.2}) == "DROWSY"

    # Eye
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.79}) == "NORMAL"
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.81}) == "DROWSY"
