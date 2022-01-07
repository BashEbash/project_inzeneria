from imageai.Detection import ObjectDetection
import os
from imageai.Detection.keras_retinanet.models import load_model
from tensorflow import keras

class CatValidator():
    def __init__(self):
        self.MODEL_FILE_NAME="static/ai_models/resnet50_coco_best_v2.1.0.h5"
        self.execution_path = os.getcwd()
        self.result_file = "cat_or_not_ai/result.jpg"
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(os.path.join(self.execution_path, self.MODEL_FILE_NAME))
        self.custom = self.detector.CustomObjects(cat=True)
        self.detector.loadModel()



    def is_a_cat(self, file):
        detections = self.detector.detectObjectsFromImage(custom_objects=self.custom,
                                             input_image=os.path.join(self.execution_path, file),
                                             minimum_percentage_probability=80,
                                             output_image_path=os.path.join(self.execution_path, self.result_file))

        if detections:
            return True
        return False




