"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import json
import os
import google.generativeai as genai
from decouple import config

# Use config to get the API key
genai.configure(api_key=config("GEMINI_API_KEY"))


def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini.

    See https://ai.google.dev/gemini-api/docs/prompting_with_media
    """
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file


# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

current_directory = os.path.dirname(os.path.abspath(__file__))

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "你是一个购物小票识别程序，我会上传照片，你识别后返回给我JSON，完需要如下信息：超市名称，超市地址，商品名称，商品翻译成英文的名称，商品翻译成中文的名称，商品价格，商品折扣，小票总价，时间日期",
            ],
        },
        {
            "role": "model",
            "parts": [
                "```json\n{\n  \"storeName\": \"LIDL\",\n  \"storeAddress\": \"Lidl Suomi Ky Turku-Keskusta Eerikinkatu 4\",\n  \"items\": [\n    {\n      \"name\": \"Rostin Bao Bun höyry­sämpy­lä\",\n      \"nameEnglish\": \"Steamed Bao Bun\",\n      \"nameChinese\": \"蒸笼包\",\n      \"price\": 2.39,\n      \"discount\": 0.29,\n    },\n    {\n      \"name\": \"Viini­ry­pä­le­tu­m­ma 500g\",\n      \"nameEnglish\": \"Dark Grapes 500g\",\n      \"nameChinese\": \"黑葡萄 500g\",\n      \"price\": 1.59\n    },\n    {\n      \"name\": \"Pohjolan Meijeri Täys­maito E\",\n      \"nameEnglish\": \"Full Milk E\",\n      \"nameChinese\": \"全脂牛奶\",\n      \"price\": 0.99\n    },\n    {\n      \"name\": \"Vit­a­sia­g­yo­za tai­ki­nan­yy­t. 1l\",\n      \"nameEnglish\": \"Gyoza Dough 1L\",\n      \"nameChinese\": \"饺子皮 1L\",\n      \"price\": 2.99\n    },\n    {\n      \"name\": \"Cosmo­po­li­tan salaatti 225g\",\n      \"nameEnglish\": \"Cosmopolitan Salad 225g\",\n      \"nameChinese\": \"大都会沙拉 225g\",\n      \"price\": 1.18\n    }\n  ],\n  \"totalPrice\": 8.32,\n  \"date\": \"2024-09-26T20:13:00Z\"\n}\n",
            ],
        },
    ]
)

response = chat_session.send_message(upload_to_gemini(os.path.join(current_directory,
                                                                   "../readme/example4.jpeg"), mime_type="image/jpeg"),)

print(response.text)

python_dict = json.loads(response.text)

print(python_dict)
