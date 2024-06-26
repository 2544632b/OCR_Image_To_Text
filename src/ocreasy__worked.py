import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np



# reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
# result = reader.readtext('data/mod01.jpg')
# print(result)

# read image
image_path ='../data/new_bl_croped.jpg'
# image_path ='../data/mod01_croped.jpg'
# image_path ='../data/denoise_mod01_resized.jpg'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['fr']) # Reader(['fr'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# Extract text and store it in a variable
extracted_text = '\n'.join([t[1] for t in text_])

# Export the extracted text to a text file
with open('../output_results/output_easyocr.txt', 'w') as text_file:
    text_file.write(extracted_text)

print("Text extracted from the image has been exported to output.txt file.")