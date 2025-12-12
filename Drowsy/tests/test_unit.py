import pytest
from Drowsy.main import classify_state

def test_normal_state():
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.1}) == "NORMAL"

def test_drowsy_yawn():
    assert classify_state({"yawn_score": 0.9, "eye_score": 0.1}) == "DROWSY"

def test_drowsy_eye():
    assert classify_state({"yawn_score": 0.2, "eye_score": 0.9}) == "DROWSY"

def test_drowsy_both():
    assert classify_state({"yawn_score": 0.9, "eye_score": 0.95}) == "DROWSY"
