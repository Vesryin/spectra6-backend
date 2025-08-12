# tests/test_emotional_state.py

import pytest
from app.engine.emotional_state import EmotionalState, Emotion

def test_emotional_state_initialization():
    """
    Tests that the EmotionalState engine initializes correctly with a default
    or specified state.
    """
    # Test default initialization
    engine_default = EmotionalState()
    assert engine_default.get_state() == Emotion.NEUTRAL

    # Test initialization with a specific emotion
    engine_joy = EmotionalState(initial_state=Emotion.JOY)
    assert engine_joy.get_state() == Emotion.JOY

def test_emotional_state_update():
    """
    Tests that the emotional state can be updated to a new, valid state.
    """
    engine = EmotionalState()
    engine.update_state(Emotion.SADNESS)
    assert engine.get_state() == Emotion.SADNESS

def test_emotional_state_update_invalid_type():
    """
    Tests that updating the state with an invalid type raises a TypeError.
    """
    engine = EmotionalState()
    with pytest.raises(TypeError):
        engine.update_state("not_an_emotion")

def test_emotional_state_str_representation():
    """
    Tests the string representation of the EmotionalState.
    """
    engine = EmotionalState(initial_state=Emotion.ANGER)
    assert str(engine) == "Spectra's current emotion is anger."
