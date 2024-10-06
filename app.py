from flask import Flask, request, jsonify
import openai
import json

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'AIzaSyCotr34E5ke8YHUcMAs6hvWfQ09R4SKt2Y'

# A route to handle submissions and generate suggestions
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get the answers from the frontend

    # Generate suggestions using GPT
    prompt = generate_prompt(data)

    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use GPT-4 if you have access
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    suggestions = response.choices[0].text.strip()

    return jsonify({'status': 'success', 'message': 'Answers submitted successfully!', 'suggestions': suggestions})


# Function to create a prompt based on the collected data
def generate_prompt(data):
    prompt = "You are a retirement financial planner. Based on the following user data, provide detailed retirement suggestions.\n\n"

    for item in data:
        prompt += f"{item['question']}: {item['answer']}\n"

    prompt += "\nProvide personalized advice on investment strategy, risk management, income needs, and lifestyle choices during retirement."

    return prompt


if __name__ == '__main__':
    app.run(debug=True)
