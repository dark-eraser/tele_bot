
import cv2
import cvlib as cv
from IPython.display import Image, display
from cvlib.object_detection import draw_bbox
class IMG_ANALYSIS:
    def detect_and_draw_box(filename, model="yolov3-tiny", confidence=0.6):
        """Detects common objects on an image and creates a new image with bounding boxes.
        Args:
            filename (str): Filename of the image.
            model (str): Either "yolov3" or "yolov3-tiny". Defaults to "yolov3-tiny".
            confidence (float, optional): Desired confidence level. Defaults to 0.6.
        """
        # Images are stored under the images/ directory

        img_filepath = '/Users/darkeraser/Documents/projects/tele_bot/'+filename
        # Read the image into a numpy array
        img = cv2.imread(img_filepath)
        # Perform the object detection
        bbox, label, conf = cv.detect_common_objects(img, confidence=confidence, model=model)
        # Print current image's filename
        print("========================nImage processed: {filename}")
        # Print detected objects with confidence level
        for l, c in zip(label, conf):
            print("Detected object: {l} with confidence level of {c}")
        # Create a new image that includes the bounding boxes
        output_image = draw_bbox(img, bbox, label, conf)
        # Save the image in the directory images_with_boxes
        cv2.imwrite('images_with_boxes/{filename}', output_image)
        # Display the image with bounding boxes
        display(Image('images_with_boxes/{filename}'))

    detect_and_draw_box('image.jpg')