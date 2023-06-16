import { Configuration, OpenAIApi } from "openai";
import dotenv from "dotenv";   // load .env file variables into process.env
dotenv.config();

const openaiApiKey = process.env.OPENAI_API_KEY;

if (!openaiApiKey) {
  console.error('OPENAI_API_KEY is not set.');
  process.exit(1);
}

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
// will use object openai to make the calls to OpenAI APIs
const openai = new OpenAIApi(configuration);

export default openai;
