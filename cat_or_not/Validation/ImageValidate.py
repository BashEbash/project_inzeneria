from cat_or_not.AddictionalFiles.app_tools import file_size

class ImageValidator():

    def __init__(self):
        self.raport = []

    def is_image(self, file):
        size = file_size(file)
        if size > 1024 * 1024 * 4:
            self.raport.append('File must have size <= 4MB')
        if self.has_no_empty_filename(file) and self.has_image_extension(file):
            return True
        elif self.has_no_empty_filename(file) and (not self.has_image_extension(file)):
            self.raport.append('Its not current file extension')
        elif not self.has_no_empty_filename(file):
            self.raport.append('File is empty')
        return False

    def has_no_empty_filename(self, file):
        if not file:
            return False
        return True

    def has_image_extension(self, file):
        file_extension = file.filename.lower().split(".")[1]
        if file_extension in ("png", "jpg", "jpeg", "bmp"):
            return True
        else:
            return False