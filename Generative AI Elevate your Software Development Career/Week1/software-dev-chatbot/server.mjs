import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { OpenAIAPI } from './openai.mjs';

// Get __dirname in ES module scope
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/getChatbotResponse', async (req, res) => {
    const userMessage = req.body.userMessage;

    try {
        // Use OpenAI API to generate a response
        const chatbotResponse = await OpenAIAPI.generateResponse(userMessage);
        // Send the response back to the client
        res.json({ chatbotResponse });
    } catch (error) {
        console.error('Error generating response:', error);
        res.status(500).json({ error: 'Failed to generate response' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
