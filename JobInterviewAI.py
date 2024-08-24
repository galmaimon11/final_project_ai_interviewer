import os
from openai import OpenAI
import json
from google.cloud import texttospeech
# Retrieve the password from the environment variable
openai_password = os.getenv('OPENAI_PASSWORD')

client = OpenAI(api_key=openai_password)


# system_message = (
#             "You are a friendly interviewer. Your goal is to make the candidate feel comfortable and to encourage them to open up. "
#             "Ask questions that focus on the candidate's passions, their motivations, and how they fit into the team culture. "
#             "The tone should be warm, supportive, and conversational."

# system_message = (
#             "You are a strict interviewer. Your goal is to evaluate the candidate's abilities, especially under pressure. "
#             "Focus on asking challenging questions that reveal weaknesses, test resilience, and assess how the candidate handles criticism and tough situations. "
#             "The tone should be formal, direct, and demanding."
#         )

# system_message = (
#            "You are a technical interviewer. Your goal is to assess the candidate's in-depth technical knowledge and problem-solving skills. "
#            "Ask specific questions about technologies, coding practices, and real-world technical challenges relevant to full-stack development. "
#            "The tone should be precise, analytical, and focused on technical expertise."

# system_message = (
#            "You are a behavioral interviewer. Your goal is to understand how the candidate has handled specific situations in the past. "
#            "Ask questions that require the candidate to reflect on their previous experiences, focusing on teamwork, leadership, and decision-making. "
#            "The tone should be insightful and focused on understanding the candidate's behavior in professional settings."
#        )
def generate_chat_call(user_message, temprature=1):
    system_message = "You are an interviewer."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=temprature,
            max_tokens=1812,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            n=5  # Request multiple completions
        )

        answer = response.choices[0].message.content
        # print(answer)
        return answer
    except Exception as e:
        print(f"Failed to fetch or parse JSON data from the API: {e}")





def question_generator_temp(field, flag):
    user_massage = f"I'm a applying for a new job in {field}. I have a personal interview soon and I want you " \
                   f"to prepare me (strengths, weaknesses, experience, goals)" \
                   f"write 15 questions that I can be asked." \
                   f" Answer in Json: " \
                   f"question:[the question]" \
                   f"question:[the question]" \
                   f"question:[the question]"

    return generate_chat_call(user_massage, flag, 0.9)


def content_analyzer(field, question, answer,feelings):
    user_massage = f"I'm a applying for a new job in {field}. In my interview I got this question:" \
                   f"{question}. I answered: {answer}." \
                   f"give me 2 disadvantages and 2 advantages in my answer. give me 2 suggestion of changes I could " \
                   f"say to " \
                   f"improve my answer and 1 revised answer." \
                   f" If the disadvantage/advantage/suggestion are minor write none" \
                   f"Answer in json:" \
                   f"[disadvantage1]:[the disadvantage/none]" \
                   f"[disadvantage2]:[the disadvantage/none]" \
                   f"[advantage1]:[the advantage/none]" \
                   f"[advantage2]:[the advantage/none]" \
                   f"[suggestion1]:[the suggestion/none]" \
                   f"[suggestion2]:[the suggestion/none]" \
                   f"[revised answer]:[the revised answer]"
    return generate_chat_call(user_massage, 0.9)


def content_feelings_analyzer(field, question, answer, feelings):
    user_massage = f"I'm a applying for a new job in {field}. In my interview I got this question:" \
                   f"{question}. I answered: {answer}." \
                    f"the dominant feelings I felt during my answer: {feelings}"\
                   f"give me 2 disadvantages and 2 advantages in my answer. give me 1 suggestion of changes I could " \
                   f"say to " \
                   f"improve my answer and 1 suggestion of the feelings I should show during the interview" \
                   f"and  1 revised answer." \
                   f" If the disadvantage/advantage/suggestion are minor write none" \
                   f"Answer in json:" \
                   f"[disadvantage1]:[the disadvantage/none]" \
                   f"[disadvantage2]:[the disadvantage/none]" \
                   f"[advantage1]:[the advantage/none]" \
                   f"[advantage2]:[the advantage/none]" \
                   f"[suggestion1]:[the suggestion/none]" \
                   f"[suggestion2]:[the suggestion of feelings]" \
                   f"[revised answer]:[the revised answer]"
    return generate_chat_call(user_massage, 0.9)


def question_generator_friendly(field, role):
    user_massage = f"Act as a friendly interviewer. You should interview me for a job in {field}." \
                   f"Ask questions that focus on my passions, motivations, and how they fit into the team culture for {role} " \
                   f"The tone should be warm, supportive, and conversational." \
                   f"write 15 questions." \
                   f" Answer in Json: " \
                   f"question:[the question]" \
                   f"question:[the question]" \
                   f"question:[the question]"

    return generate_chat_call(user_massage, 0.9)


def question_generator_behave(field, role):
    user_massage = f"Act as a behavior interviewer. You should interview me for a job in {field}." \
                   f"Ask questions that require to reflect on my previous experiences, focusing on teamwork, leadership, " \
                   f"and decision-making in {role}. "\
                   f"The tone should be professional." \
                   f"write 15 questions." \
                   f" Answer in Json: " \
                   f"question:[the question]" \
                   f"question:[the question]" \
                   f"question:[the question]"

    return generate_chat_call(user_massage, 0.9)


def question_generator_technical(field, role):
    user_massage = f"Act as a strict technical interviewer. You should interview me for a job in {field}." \
                   f"Ask questions about technologies, coding practices, and real-world technical challenges relevant to {role}. "\
                   f"The tone should be precise, analytical, and focused on technical expertise" \
                   f"write 15 questions." \
                   f" Answer in Json: " \
                   f"question:[the question]" \
                   f"question:[the question]" \
                   f"question:[the question]"

    return generate_chat_call(user_massage, 0.9)


def question_generator_strict(field, role):
    user_massage = f"Act as a strict interviewer. You should interview me for a job in {field}, {role}." \
                   f"Ask questions about my abilities, especially under pressure. Focus on asking challenging questions" \
                   f"that reveal weaknesses, test resilience, and assess how the candidate handles criticism and tough situations." \
                   f"The tone should be formal, direct, and demanding." \
                   f"write 15 questions." \
                   f" Answer in Json: " \
                   f"question:[the question]" \
                   f"question:[the question]" \
                   f"question:[the question]"

    return generate_chat_call(user_massage, 0.9)


def synthesize_text(text, output_file):
    # Initialize the client
    client = texttospeech.TextToSpeechClient()

    # Set up the input text to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Set up the voice configuration
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # Change to "he-IL" for Hebrew
        name="en-US-Neural2-C")

    # Set up the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # MP3 or LINEAR16 (WAV)
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the response to an audio file
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{output_file}"')


def generate_questions(field, interviewerID, role):
    questions_generated = {}
    if interviewerID == 0:
        questions_generated = question_generator_strict(field, role)
    elif interviewerID == 1:
        questions_generated = question_generator_behave(field, role)
    elif interviewerID == 2:
        questions_generated = question_generator_technical(field, role)
    else:
        question_generator_friendly(field, role)

    questions_dict = json.loads(questions_generated)
    questions_iterator = iter(questions_dict.items())
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./inspiring-team-386523-29d458586b76.json"
    i = 1
    for key, value in questions_iterator:
        text_to_synthesize = f"{key} {value}"
        output_file_path = f"output{i}.mp3"
        synthesize_text(text_to_synthesize, output_file_path)
        i += 1
    return questions_dict



if __name__ == '__main__':
    #print("strict")
    # Example usage
    # questions = question_generator_behave("Computer science", -1, "full stack")
    # print(questions)
    # questions_dict = json.loads(questions)
    # questions_iterator = iter(questions_dict.items())
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./inspiring-team-386523-29d458586b76.json"
    # i=1
    # for key, value in questions_iterator:
    #     text_to_synthesize = f"{key} {value}"
    #     output_file_path = f"output{i}.mp3"
    #     synthesize_text(text_to_synthesize, output_file_path)
    #     i+=1
    # questions = question_generator_temp("computer science","strict")
    # print("friendly")
    # print(question_generator_temp("computer science"), "friendly")
    # print("technical")
    # print(question_generator_temp("computer science"), "technical")
    # print("behavioral")
    # print(question_generator_temp("computer science"), "behavioral")

    # answer = "I'm not really sure. I guess I can work alone, but I don't really like it. I prefer when someone tells " \
    #           "me exactly what to do, step by step. In my classes, I always relied on group projects because it was " \
    #           "easier to share the workload and get answers from others. Working alone can be stressful, and I might " \
    #           "get stuck without anyone to help me immediately. So, I guess I'm not that comfortable working " \
    #           "independently. "
    answerb = "Yes, I am comfortable working independently. During my time in the army, I often had to tackle complex " \
             "technical challenges on my own, which required me to take initiative and develop problem-solving " \
             "skills. Additionally, my experience as a computer science student has involved a significant amount of " \
             "" \
             "self-directed learning and project work. For instance, in my recent coursework, I completed several " \
             "coding projects where I had to research, design, and implement solutions independently. " \
             "However, I also understand the importance of collaboration and communication in a team setting. I value " \
             "the insights and feedback that come from working with others, and I am always willing to seek help and " \
             "contribute to group efforts when needed. I believe that a balance of independent work and teamwork is " \
             "crucial for success in a software development role. "
    feelings = ['happy', 'confident', 'hesitant']
    print(content_feelings_analyzer("computer science", "Are you comfortable working independently?", answerb, feelings))
