import wolframalpha
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
question=input('question: ')
app_id='8LT2TR-UE3L7L6LJQ'
client=wolframalpha.Client(app_id)
res=client.query(question)
answer=next(res.results).text
print(answer)