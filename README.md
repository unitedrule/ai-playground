# GPT Text Summarizer and Rephraser App

**Author**: Bakr Bagaber
**Date**: September 19, 2023
**Version**: 1.0.0

## Description

Welcome to the GPT Text Summarizer and Rephraser App! This Streamlit web application harnesses the power of the OpenAI GPT (Generative Pre-trained Transformer) model to perform text summarization and paraphrasing tasks. With this app, you can input text and customize various options to tailor the output to your specific needs. Whether you need a concise summary, a rephrased version, or a text tailored to a particular audience, this app has you covered.

**Note**: To use this application, ensure that you have set your OpenAI API key in a `.env` file. Please be aware that using this application may incur API usage costs for the OpenAI service.

To run the app, execute the following command in your terminal:

```shell
streamlit run PATH_TO_summarizer_app.py
```

## Features

- **Input Text**: You can input the text you want to summarize or rephrase in the provided text area.

- **Customization Options**: The app offers a range of customization options, including:

  - **Language Models**: Choose from different GPT language models, such as "gpt-3.5-turbo," "gpt-3.5-turbo-16k," "gpt-4," or "gpt-4-32k."

  - **Max Tokens**: Specify the maximum number of tokens for the output.

  - **Temperature**: Adjust the temperature parameter to control the randomness of the generated text.

  - **Nucleus Sampling**: Set the nucleus sampling parameter to influence the diversity of the responses.

  - **Frequency Penalty**: Apply a frequency penalty to encourage or discourage repeated phrases.

  - **Presence Penalty**: Use a presence penalty to control the use of certain words or phrases.

- **Target Audience**: Select your target audience from a list that includes options like "Engineering Scientific Community," "University Students," and more.

- **Tone of Voice**: Choose the desired tone of voice, whether it's "Professional," "Academic," "Simple," "Original," or a combination of styles.

- **Task Selection**: Specify the task you would like to perform, such as "Paraphrase," "Summarize," "Shorten," "Rewrite," "Combine," "Elaborate," or "Outline."

- **Custom Prompts**: If you have a specific prompt in mind, you can enter it directly, and it will override other settings.

- **Cost Estimation**: The app provides an estimated cost for using the OpenAI models based on your input and options.

## How to Use

1. Enter the text you want to summarize or rephrase in the "Enter the original text" text area.

2. Customize the options according to your preferences, including language model, max tokens, temperature, nucleus sampling, frequency penalty, and presence penalty.

3. Choose your target audience, tone of voice, and the task you'd like to perform.

4. If you have a specific prompt in mind, you can enter it in the "Enter your custom prompt" text area; otherwise, the app will generate a prompt based on your selected options.

5. Click the "Start" button to initiate the text summarization or rephrasing process.

6. The app will generate the output text, and you can view the results in the same interface.

## Disclaimer

Please keep in mind that this application is primarily for demonstration purposes. It utilizes the OpenAI GPT models, which may incur usage costs for the OpenAI service. Be sure to set up your API key and monitor your usage accordingly.

---

Thank you for using the GPT Text Summarizer and Rephraser App. We hope this tool proves helpful in summarizing and rephrasing text for your specific needs. If you have any questions or encounter issues, please feel free to reach out to the author, Bakr Bagaber.
