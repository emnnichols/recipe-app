from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    """Used to store & serve dynamic media files with no access expiration"""
    location = settings.MEDIA_LOCATION
    default_acl = settings.MEDIA_DEFAULT_ACL
    file_overwrite = False