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