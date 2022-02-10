from __future__ import print_function
from charset_normalizer import detect
from google.cloud import vision
import io 
image_uri = 'imagee.jpg'
class A:
  def detect_labels(path):

  
      client = vision.ImageAnnotatorClient()

      with io.open(path, 'rb') as image_file:
          content = image_file.read()

      image = vision.Image(content=content)

      response = client.label_detection(image=image)
      labels = response.label_annotations
      print('Labels:')

      for label in labels:
          print(label.description+ ": "+str(label.score*100))

      if response.error.message:
          raise Exception(
              '{}\nFor more info on error messages, check: '
              'https://cloud.google.com/apis/design/errors'.format(
                  response.error.message))
      return labels

  # detect_labels(image_uri)