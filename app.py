from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 设置你的OpenAI API密钥
openai.api_key = 'AIzaSyCotr34E5ke8YHUcMAs6hvWfQ09R4SKt2Y'

# 处理生成问题的请求
@app.route('/generate-question', methods=['POST'])
def generate_question():
    data = request.json
    topic = data.get('topic')

    # 调用OpenAI API生成问题
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用GPT-4的具体引擎
        prompt=f"Generate a thought-provoking question about {topic}.",
        max_tokens=50,
        temperature=0.7
    )

    question = response.choices[0].text.strip()

    return jsonify({'question': question})

if __name__ == '__main__':
    app.run(debug=True)
