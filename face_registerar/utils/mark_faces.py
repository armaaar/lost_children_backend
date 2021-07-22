import json
import cv2
from numpy import ndarray
from face_registerar.models.kid_face import KidFace

_mark_settings: dict = {
    'padding': 5,
    'thickness': 2,
    'font_scale': 0.6,
    'label_height': 20,
    'color': (0, 255, 0),
    'text_color': (255, 255, 255)
}


def mark_faces(image: ndarray, faces: list[KidFace]) -> list[ndarray, dict]:
    """Retrun an image with all faces marked in an image"""
    marked_image: ndarray = image.copy()
    handlers: dict = {}
    for index, face in enumerate(faces):
        handler = str(index + 1)
        handlers[handler] = face.id
        y_1, x_2, y_2, x_1 = json.loads(face.location)
        # Draw rectangle around face
        cv2.rectangle(
            marked_image,
            (x_1, y_1),
            (x_2, y_2),
            _mark_settings['color'],
            _mark_settings['thickness']
        )
        # Create rectangle to put face handler in
        cv2.rectangle(
            marked_image,
            (x_1, y_2),
            (x_2, y_2 + _mark_settings['label_height']),
            _mark_settings['color'],
            cv2.FILLED
        )
        # Put face handler
        cv2.putText(
            marked_image,
            handler,
            (x_1 + _mark_settings['padding'], y_2  + _mark_settings['label_height'] - _mark_settings['padding']),
            cv2.FONT_HERSHEY_COMPLEX,
            _mark_settings['font_scale'],
            _mark_settings['text_color'],
            _mark_settings['thickness']
        )

    return [marked_image, handlers]
