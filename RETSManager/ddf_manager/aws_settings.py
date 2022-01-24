##This file to configure S3 bucket settings for media storage.

# LINODE_BUCKET = "crea-ddf-data"
# #LINODE_BUCKET_REGION = "us-east-1"
# LINODE_BUCKET_ACCESS_KEY ="4JCMTXFML1SF4OIIK36I"
# LINODE_BUCKET_SECRET_KEY = "KVy4pEJg8kWKCVxOllQ4sLKxAc6e5pDBKgDViadK"

# AWS_S3_ENDPOINT_URL = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com'
# AWS_S3_ENDPOINT_URL = 'https://us-east-1.linodeobjects.com'
# AWS_S3_REGION_NAME = LINODE_BUCKET_REGION

# AWS_S3_USE_SSL = True
# AWS_S3_FILE_OVERWRITE = False

# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }

AWS_ACCESS_KEY_ID = LINODE_BUCKET_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = LINODE_BUCKET_SECRET_KEY
AWS_ROOT = 'https://us-east-1.linodeobjects.com'
AWS_STORAGE_BUCKET_NAME = LINODE_BUCKET
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}




### Issa Code
##This file to configure S3 bucket settings for media storage.

# AWS_ACCESS_KEY_ID = '' #KEY_ID HERE
# AWS_SECRET_ACCESS_KEY = '' #ACCESS_KEY HERE
# AWS_ROOT = 'https://s3.us-east-2.amazonaws.com/' #Example
# AWS_STORAGE_BUCKET_NAME = '' #Bucket Name Here

# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
#### end Issa code