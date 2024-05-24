import fetch from 'node-fetch';

const apiKey = '';  // Replace with your actual API key

class OpenAIAPI {
    static async generateResponse(userMessage, conversationHistory = []) {
        const endpoint = 'https://api.openai.com/v1/chat/completions';

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${apiKey}`,
                },
                body: JSON.stringify({
                    model: "gpt-3.5-turbo-1106",
                    messages: conversationHistory.concat([{ role: 'user', content: userMessage }]),
                    max_tokens: 150
                }),
            });

            const responseData = await response.json();

            // Log the entire API response for debugging
            console.log('Response from OpenAI API:', responseData);

            // Check if choices array is defined and not empty
            if (responseData.choices && responseData.choices.length > 0 && responseData.choices[0].message) {
                return responseData.choices[0].message.content;
            } else {
                // Handle the case where choices array is undefined or empty
                console.error('Error: No valid response from OpenAI API');
                return 'Sorry, I couldn\'t understand that.';
            }
        } catch (error) {
            console.error('Error fetching response from OpenAI API:', error);
            return 'Sorry, there was an error processing your request.';
        }
    }
}

export { OpenAIAPI };
