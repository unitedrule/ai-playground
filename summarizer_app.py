"""
GPT Text Summarizer and Rephraser App
Author: Bakr Bagaber
Date: September 25, 2023
Version: 1.0.1

Description:
This Streamlit web application uses the OpenAI GPT (Generative Pre-trained Transformer) model
to perform text summarization and paraphrasing tasks. Users can input text, select various
options for the language model, target target_audience, tone of voice, and task to be performed.
The application then generates a summary or paraphrased version of the input text based on
the user's preferences.

Usage Instructions:
1. Enter the text you want to summarize or paraphrase in the text input area.
2. Adjust the model parameters and options in the corresponding sections.
3. Click the "Start" button to initiate the text summarization or paraphrasing process.
4. The generated output will be displayed below the input and parameter sections.

Note: Ensure that you have set your OpenAI API key in a .env file to use this application.

Disclaimer:
This application is for demonstration purposes and may incur API usage costs for the OpenAI service.

RUN: streamlit run c:\phd\gpt\summarizer_app.py
"""

import openai
import os
from dotenv import load_dotenv
import streamlit as st
import tiktoken
import math


def main():

    # Call OpenAi API key from the settings environment file
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Set prompt settings
    voice_tones = {
        "Professional": "A PROFESSIONAL voice and tone, use industry-specific language and terminology, \
                    provide detailed and accurate information, and support your argument with statistics, \
                    research, and expert opinions.",
        "Academic": "An ACADEMIC voice and tone, use advanced vocabulary and grammar, \
                    and provide a thorough analysis of the subject matter. Explain complex concepts clearly \
                    and use examples from various fields. Present counterarguments objectively.",
        "Simple": "A SIMPLE voice and tone, explain using simple language, \
                    break down complex concepts into frameworks or models, and provide practical takeaways.",
        "Original": "The ORIGINAL text voice and tone, use the same writing style, wordings and terminologies as the original text.",
        "Combined": "A PROFESSIONAL ACADEMIC voice and tone, use the same writing style, wordings and terminologies as the ORIGINAL text. \
                    Improve with industry-specific language and terminology, provide detailed and accurate information, and support your argument with statistics, \
                    research, and expert opinions. Use advanced vocabulary and grammar, \
                    and provide a thorough analysis of the subject matter. Explain complex concepts clearly \
                    and use examples from various fields. Present counterarguments objectively.",
    }

    # Define OpenAI Models pricing scheme
    model_prices = [
            {
                "gpt-3.5-turbo": 0.0015,
                "gpt-3.5-turbo-16k": 0.003,
                "gpt-4": 0.03,
                "gpt-4-32k": 0.06,
            },
            {
                "gpt-3.5-turbo": 0.002,
                "gpt-3.5-turbo-16k": 0.004,
                "gpt-4": 0.06,
                "gpt-4-32k": 0.12,
            },
        ]
    
    # Define OpenAI Models max Tockens
    model_tockens = {
                "gpt-3.5-turbo": 4097,
                "gpt-3.5-turbo-16k": 16385,
                "gpt-4": 8192,
                "gpt-4-32k": 32768
            }
    
    # Set the application title
    st.title("GPT Text Paraphraser")

    # Provide the input area for text to be summarized
    input_text = st.text_area("Enter the original text:", height=500)

    # Count the number of input text tokens
    encoding = tiktoken.get_encoding("cl100k_base")
    input_tokens = len(encoding.encode(input_text))

    # Initiate three columns for section to be side-by-side
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    # Language model parameters group
    with st.container():
        # Selection box for the language model
        with col1:
            gpt_model = st.selectbox(
                "Select GPT Language Model?",
                (
                    "gpt-4",
                    "gpt-3.5-turbo",
                    "gpt-3.5-turbo-16k",
                    "gpt-4-32k",
                ),
            )

        # Estimate the cost of the task
        estimated_cost = (
            math.ceil(input_tokens / 1000) * model_prices[0][gpt_model]
            + math.ceil(input_tokens / 1000) * model_prices[1][gpt_model]
        )

        # Showing the current parameter used for the model
        with col2:
            st.write("Input Tokens :", input_tokens)
            st.write("Estimated Cost ($) :", estimated_cost)

        # Sliders to control the model hyperparameters
        with col3:
            max_tokens = st.slider(
                "Max Tokens", min_value=0, max_value=model_tockens[gpt_model], value=int(model_tockens[gpt_model]*0.9)-input_tokens, step=int(model_tockens[gpt_model]/100)
            )
            temp = st.slider(
                "Temperature", min_value=0.0, max_value=2.0, value=0.5, step=0.1
            )
            top_p = st.slider(
                "Nucleus Sampling", min_value=0.0, max_value=1.0, value=0.5, step=0.1
            )
            f_pen = st.slider(
                "Frequency Penalty", min_value=-2.0, max_value=2.0, value=0.2, step=0.1
            )
            p_pen = st.slider(
                "Presence Penalty", min_value=-2.0, max_value=2.0, value=0.3, step=0.1
            )

    # Language model task group
    with st.container():
        # Selection box to select the target target_audience
        with col4:
            target_audience = st.selectbox(
                "Select Your Target Audience",
                (
                    "Engineering Scientific Community",
                    "Electrical Engineers",
                    "Mechanical Engineers",
                    "Mechatronic Engineers",
                    "Aerospace and Avionics Engineers",
                    "Electrical, mechanical and aerospace Engineers",
                    "University Students",
                    "University Professors",
                ),
            )

        # Selection box for tone of voice
        with col5:
            target_tone = st.selectbox(
                "Select Your Tone of Voice",
                (
                    "Academic",
                    "Combined",
                    "Professional",
                    "Simple",
                    "Original",
                ),
            )

        # Selection box to select the job task
        with col6:
            job_task = st.selectbox(
                "What you would like to do?",
                (
                    "Summarize",
                    "Paraphrase",
                    "Shorten",
                    "Rewrite",
                    "Combine",
                    "Elaborate",
                    "Outline",
                ),
            )

    # Custom prompt (If filled, overrides other parameters)
    with st.container():
        custom_prompt = st.text_area("Enter your custom prompt (THis will override other settings):", height=5)

    # Select GPT prompt
    if custom_prompt.strip() == "":
        usr_command = f"{job_task} this for an target_audience of {target_audience}, using {voice_tones[target_tone]}"
    else:
        usr_command = custom_prompt

    # Creating button for execute the text summarization
    if st.button("Start"):
        output_text = generate_summarizer(
            gpt_model,
            max_tokens,
            temp,
            top_p,
            f_pen,
            p_pen,
            usr_command,
            input_text,
        )
        output_tokens = len(encoding.encode(output_text))
        actual_cost = (
            math.ceil(input_tokens / 1000) * model_prices[0][gpt_model]
            + math.ceil(output_tokens / 1000) * model_prices[1][gpt_model]
        )

        with col2:
            st.write("Output Tokens :", output_tokens)
            st.write("Actual Cost ($) :", actual_cost)

        st.write(output_text)


def generate_summarizer(
    model,
    max_tokens,
    temperature,
    top_p,
    frequency_penalty,
    presence_penalty,
    command,
    prompt,
):
    res = openai.ChatCompletion.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for text paraphrasing and summarization.",
            },
            {
                "role": "user",
                "content": f"{command}: {prompt}",
            },
        ],
    )
    return res["choices"][0]["message"]["content"]


if __name__ == "__main__":
    main()
