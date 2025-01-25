
# import cv2
# import numpy as np
# import pytesseract
# from groq import Groq

# # Load the camera scanner
# cap = cv2.VideoCapture(0)

# # Preprocess the images
# def preprocess_image(image):
#     image = cv2.resize(image, (640, 480))
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     return image

# # Detect text using Tesseract
# def detect_text(image):
#     text = pytesseract.image_to_string(image, lang='eng', config='--psm 11')
#     return text

# # Extract specific numbers or text using Groq
# def extract_data(text):
#     # Initialize Groq
#     groq = Groq()
#     # Extract specific patterns or formats (e.g., dates, phone numbers, IDs)
#     data = groq.extract_data(text, pattern='\\d{4}-\\d{2}-\\d{2}')  # Extract dates in YYYY-MM-DD format
#     return data

# # Main loop
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     # Preprocess the image
#     image = preprocess_image(frame)
#     # Detect text
#     text = detect_text(image)
#     # Extract specific numbers or text
#     data = extract_data(text)
#     # Store the extracted data
#     print(data)


# from groq import Groq

# client = Groq()
# completion = client.chat.completions.create(
#     model="llama-3.2-90b-vision-preview",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "Tell me the brand, price range, material, and manufacturing location of the clothing item. Below is an exmaple of what your output should look like. No other text should be included.\nBrand\nPrice range\nMaterial\nManufacturing location"
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "${IMAGE_DATA_URL}"
#                     }
#                 }
#             ]
#         },
#         {
#             "role": "assistant",
#             "content": "GILDAN\n$10-$20\n100% cotton\nBangladesh"
#         }
#     ],
#     temperature=1,
#     max_completion_tokens=1024,
#     top_p=1,
#     stream=False,
#     stop=None,
# )

# print(completion.choices[0].message)


from groq import Groq
api_key = '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' # generated API key
client = Groq()
completion = client.chat.completions.create(
    model="llama-3.2-90b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Read the number below the barcode. Your answer output should o only feature the digits and nothing else."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "${IMAGE_DATA_URL}"
                    }
                }
            ]
        },
        {
            "role": "assistant",
            "content": "577606577902"
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
