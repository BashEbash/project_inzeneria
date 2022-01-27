import unittest
import os
from PIL import Image
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from cat_or_not.CatOrNotAI.CatValidator import CatValidator
from cat_or_not.Validation.ImageValidate import ImageValidator
from cat_or_not.AddictionalFiles.app_tools import file_size

class MainTests(unittest.TestCase):
    def test_is_cat(self):
        catValidator = CatValidator("../Static/AIModel/resnet50_coco_best_v2.1.0.h5")
        self.assertEqual(catValidator.is_a_cat("TestFiles/cat.jpg"), True, "Powinno być: True")

    def test_is_not_cat(self):
        catValidator = CatValidator("../Static/AIModel/resnet50_coco_best_v2.1.0.h5")
        catValidator.MODEL_FILE_NAME = "../Static/AIModel/resnet50_coco_best_v2.1.0.h5"
        self.assertEqual(catValidator.is_a_cat("TestFiles/dog.jpg"), False, "Powinno być: False")

    def test_supported_file_type1(self):
        imageValidator = ImageValidator()
        image = Image.open("TestFiles/cat.jpg")
        self.assertEqual(imageValidator.has_image_extension("cat.jpg"), True, "Powinno być: True")
        image.close()

    def test_supported_file_type2(self):
        imageValidator = ImageValidator()
        image = Image.open("TestFiles/colors.jpeg")
        self.assertEqual(imageValidator.has_image_extension("colors.jpeg"), True, "Powinno być: True")
        image.close()

    def test_supported_file_type3(self):
        imageValidator = ImageValidator()
        image = Image.open("TestFiles/structure.png")
        self.assertEqual(imageValidator.has_image_extension("structure.png"), True, "Powinno być: True")
        image.close()

    def test_supported_file_type4(self):
        imageValidator = ImageValidator()
        image = Image.open("TestFiles/sample.bmp")
        self.assertEqual(imageValidator.has_image_extension("sample.bmp"), True, "Powinno być: True")
        image.close()

    def test_unsupported_file_type1(self):
        imageValidator = ImageValidator()
        image = Image.open("TestFiles/earth.gif")
        self.assertEqual(imageValidator.has_image_extension("earth.gif"), False, "Powinno być: False")
        image.close()

    def test_unsupported_file_type2(self):
        imageValidator = ImageValidator()
        file = open("TestFiles/not_photo.txt")
        self.assertEqual(imageValidator.has_image_extension("not_photo.txt"), False, "Powinno być: False")
        file.close()

    def test_too_big_file1(self):
        file = open("TestFiles/dog.jpg")
        size = file_size(file)
        self.assertLessEqual(size, 1024 * 1024 * 4)
        file.close()

    def test_too_big_file2(self):
        file = open("TestFiles/too_big.jpg")
        size = file_size(file)
        self.assertGreaterEqual(size, 1024 * 1024 * 4)
        file.close()

if __name__ == '__main__':
    unittest.main()