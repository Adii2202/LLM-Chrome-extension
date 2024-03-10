import requests
import json

def generate_text(sel_text):
    print("selected text : {}".format(sel_text))
    try:
        payload={
            "model":"mistral",
            "prompt": f"summarize the text inside the square brackets not more than 10 words [{sel_text}]",
            "stream":False
        }
        api_url="http://localhost:11434/api/generate"
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            responses = response.content.split(b'\n')
            generated_text = ''
            for obj in responses:
                if obj:
                    response_data = json.loads(obj.decode())
                    response = response_data.get("response")
                    if response:
                        if response.strip():
                            if response==" ":
                                generated_text+=response
                            else:
                                if generated_text:
                                    generated_text+=' '
                                generated_text += response.strip()
            print(generated_text)
            return generated_text
        else:
            print(f"Error : Failed to generate text. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error : {e}")
        raise e