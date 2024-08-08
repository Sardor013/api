import uuid

class SaveMediaFiles(object):
    def song_image_save(instance, filename):
        image_path = filename.split('.')[-1]
        return f'api/songs/{uuid.uuid4()}.{image_path}'
