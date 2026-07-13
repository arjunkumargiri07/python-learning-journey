from openai import OpenAI

# pip install openai

client = OpenAI(
    api_key="<Your Key Here>"
)

command = """
[10:36 AM, 7/3/2026] +977 976-8027940: File attach garera pathau hai
[10:37 AM, 7/3/2026] Arjun Kumar Giri: Email ma harna vhana ta
[10:37 AM, 7/3/2026] +977 976-8027940: La
[10:37 AM, 7/3/2026] Arjun Kumar Giri: Natra whatapp ma pani zip file pathaii dachu
[10:37 AM, 7/3/2026] +977 976-8027940: Ok
[10:44 AM, 7/3/2026] +977 976-8027940: Background last naramro aayexa ta
[10:45 AM, 7/3/2026] +977 976-8027940: Sign haneko Haru sabai ma BG dekhiyexa
[10:50 AM, 7/3/2026] Arjun Kumar Giri: email pathau ta
[10:51 AM, 7/3/2026] Arjun Kumar Giri: https://canva.link/07sujbhrm5hpfy7
[10:51 AM, 7/3/2026] +977 976-8027940: printerslakecity@gmail.com
[10:51 AM, 7/3/2026] +977 976-8027940: Uta ko WhatsApp ma pathau ta link
[10:52 AM, 7/3/2026] +977 976-8027940: Milena ni
[10:52 AM, 7/3/2026] Arjun Kumar Giri: Add gardachu
[10:53 AM, 7/3/2026] +977 976-8027940: Milena ta
[10:54 AM, 7/3/2026] +977 976-8027940: Kati time samma chhaiyeko ho ?
[10:54 AM, 7/3/2026] Arjun Kumar Giri: Email ma pathaii dachu ho
[10:54 AM, 7/3/2026] Arjun Kumar Giri: Kati time samma chhaiyeko ho ?
10 min ma
[10:55 AM, 7/3/2026] +977 976-8027940: Yeta khuldai khulena, yei print garera aaidinxu vanesi
[10:55 AM, 7/3/2026] +977 976-8027940: Paxi milamla ani digital dimla hamile nai
[10:55 AM, 7/3/2026] Arjun Kumar Giri: Umm huncha
[10:55 AM, 7/3/2026] Arjun Kumar Giri: Tyaii gardau
"""

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": (
                "You are Arjun Kumar Giri. Analyze the WhatsApp conversation "
                "and generate a natural reply in the same language (Nepali, "
                "English, or mixed) and tone as the conversation."
            )
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)