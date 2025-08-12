# src/app/engine/emotional_state.py

import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Emotion(Enum):
    """
    Enumeration of core emotional states for Spectra.
    """
    JOY = "joy"
    SADNESS = "sadness"
    ANGER = "anger"
    FEAR = "fear"
    SURPRISE = "surprise"
    NEUTRAL = "neutral"

class EmotionalState:
    """
    Manages Spectra's emotional state, allowing for dynamic updates based on
    interactions and internal reflections.
    """
    def __init__(self, initial_state: Emotion = Emotion.NEUTRAL):
        """
        Initializes the emotional state.

        Args:
            initial_state (Emotion): The starting emotional state for Spectra.
                                     Defaults to NEUTRAL.
        """
        self.current_state = initial_state
        logging.info(f"Emotional state initialized to {self.current_state.value}")

    def update_state(self, new_state: Emotion):
        """
        Updates Spectra's emotional state to a new state.

        Args:
            new_state (Emotion): The new emotional state to transition to.
        """
        if not isinstance(new_state, Emotion):
            raise TypeError("new_state must be an instance of the Emotion enum.")

        if self.current_state != new_state:
            logging.info(f"Emotional state changing from {self.current_state.value} to {new_state.value}")
            self.current_state = new_state
        else:
            logging.info(f"Emotional state remains {self.current_state.value}")

    def get_state(self) -> Emotion:
        """
        Retrieves the current emotional state.

        Returns:
            Emotion: The current emotional state of Spectra.
        """
        return self.current_state

    def __str__(self) -> str:
        """
        Returns a string representation of the current emotional state.
        """
        return f"Spectra's current emotion is {self.current_state.value}."
