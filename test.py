'''
c460c7fe30b841b1a83170591df37d6f

caaadd2bb1ca4e01850fe840f70c017a

https://ansertech.cognitiveservices.azure.com/

koreacentral
'''

import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://ansertech.cognitiveservices.azure.com/"
key = "c460c7fe30b841b1a83170591df37d6f"  