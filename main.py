import os
import openai
from pypdf import PdfReader

reader = PdfReader("2212.08073.pdf")
number_of_pages = len(reader.pages)
text = ''.join([page.extract_text() for page in reader.pages])
print(text[:2155])


client = openai.OpenAI(api_key=os.environ['API_KEY'])
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2, 
        max_tokens=1000
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

prompt = f"""

Here is an academic paper: <paper>{text[:200]}</paper>

Please do the following:
1. Summarize the abstract at a kindergarten reading level. (In <kindergarten_abstract> tags.)
2. Write the Methods section as a recipe from the Moosewood Cookbook. (In <moosewood_methods> tags.)
3. Compose a short poem epistolizing the results in the style of Homer. (In <homer_results> tags.)
4. Write a grouchy critique of the paper from a wizened PI. (In <grouchy_critique> tags.)

"""
response = get_completion(prompt)
print(response)