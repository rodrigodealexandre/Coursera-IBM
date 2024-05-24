const fetch = require('node-fetch'); // Use the CommonJS version
const { OpenAIAPIKey } = require('./config'); 

class OpenAIAPI {
    static async generateResponse(userMessage) {
        const apiKey = OpenAIAPIKey;
        const endpoint = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions';
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`,
            },
            body: JSON.stringify({
                prompt: userMessage,
                max_tokens: 150,
            }),
        });
        const responseData = await response.json();
        console.log('Response from OpenAI API:', responseData);
        if (responseData.choices && responseData.choices.length > 0) {
            return responseData.choices[0].text.trim();
        } else {
            console.error('Error: No valid response from OpenAI API');
            return 'Sorry, I couldn\'t understand that.';
        }
    }
}
module.exports = { OpenAIAPI };
