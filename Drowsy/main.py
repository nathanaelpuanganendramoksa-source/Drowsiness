# main.py

def classify_state(result: dict):
    """
    result = {
        "yawn_score": float,
        "eye_score": float
    }
    """

    yawn = result.get("yawn_score", 0)
    eye = result.get("eye_score", 0)

    if yawn > 0.7 or eye > 0.8:
        return "DROWSY"
    else:
        return "NORMAL"
