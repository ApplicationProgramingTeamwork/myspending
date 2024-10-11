"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
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

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "你是一个超市小票识别程序，我会发给你一张照片让你识别，小票的格式一般如下：",
                "```\nRosten Bao Bun höyrysampyla 4,78\n  ALENNUS 30% -1,39\nPizza vegetariana 4,78\n  Lidl Plus -saästösi -1,39\n```\n前面没有缩进的行是商品信息，紧随其后的是价格；前面有缩进的行是打折或者补充信息，紧随其后的数字一般是优惠价格",
                "我需要生成这样的JSON结构，需要这些信息：超市名称，超市地址，商品名称，商品翻译成英文的名称，商品翻译成中文的名称，商品价格(数字格式,默认值为0)，商品折扣(数字格式,默认值为0)，小票总价(数字格式,默认值为0)，时间日期(iso格式时间日期字符串)。你直接返回我json",
                "```json\n{\n  \"storeName\": \"Lidl\",\n  \"storeAddress\": \"Lidl Suomi Ky Turku-Keskusta Eerikinkatu 4\",\n  \"items\": [\n    {\n      \"name\": \"Rostin Bao Bun höyry­sämpy­lä\",\n      \"nameEnglish\": \"Steamed Bao Bun\",\n      \"nameChinese\": \"蒸笼包\",\n      \"price\": 2.39,\n      \"discount\": 0.29\n    },\n],\n  \"totalPrice\": 12.96,\n  \"date\": \"2024-09-28T17:02:00Z\"\n}\n```",
            ],
        }
    ]
)


def send_message_to_gemini(message):
    response = chat_session.send_message(message)
    return response.text


def send_photo_to_gemini(photo):
    return send_message_to_gemini(upload_to_gemini(photo))
