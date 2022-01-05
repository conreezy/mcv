##This file to configure S3 bucket settings for media storage.

LINODE_BUCKET = "crea-ddf-data",
LINODE_BUCKET_REGION = "us-east-1",
LINODE_BUCKET_ACCESS_KEY ="4JCMTXFML1SF4OIIK36I",
LINODE_BUCKET_SECRET_KEY = "KVy4pEJg8kWKCVxOllQ4sLKxAc6e5pDBKgDViadK"

#  #
AWS_ACCESS_KEY_ID = LINODE_BUCKET_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = LINODE_BUCKET_SECRET_KEY

# AWS_ROOT = 'https://s3.us-east-2.amazonaws.com/' #Example
AWS_ROOT = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com'
AWS_STORAGE_BUCKET_NAME = LINODE_BUCKET

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}