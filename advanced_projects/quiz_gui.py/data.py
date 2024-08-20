#data=[{"response_code":0,"results":[{"type":"boolean","difficulty":"medium","category":"History","question":"If you grab the bladed end of a longsword in a specific way, you will not cut yourself.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"hard","category":"History","question":"The Kingdom of Prussia briefly held land in Estonia.","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"&quot;Ananas&quot; is mostly used as the word for Pineapple in other languages.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"Entertainment: Music","question":"Stevie Wonder&#039;s real name is Stevland Hardaway Morris.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"Geography","question":"Vatican City is a country.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"Entertainment: Board Games","question":"The card game &quot;Munchkin&quot; won the 2001 Origins Award for Best Traditional Card Game.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"medium","category":"Entertainment: Television","question":"Klingons respect their disabled comrades, and those who are old, injuried, and helpless.","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"Adolf Hitler was born in Australia. ","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"Entertainment: Books","question":"&quot;Elementary, my dear Watson&quot; is a phrase that is never truly said within the Conan Doyle books of Sherlock Holmes.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"medium","category":"Science &amp; Nature","question":"Sugar contains fat.","correct_answer":"False","incorrect_answers":["True"]}]}]
import requests

parameter={
    'amount':10,
    'type':'boolean'
}
respone =requests.get('https://opentdb.com/api.php',params=parameter)
respone.raise_for_status()
data=respone.json()
questiondata=data['results']
print(questiondata)