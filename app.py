from flask import Flask,request,jsonify
import googletrans
#import nltk
translator=googletrans.Translator()
print(googletrans.LANGUAGES)
app=Flask(__name__)
@app.route('/' ,methods=['POST'])
def helloworld():
    data=request.get_json()

    text=str(data['queryResult']['queryText'])

    text = text.lower()


    dict1=googletrans.LANGUAGES
   # # def GetKey(val):
   #      for key, value in dict1.items():
   #          if val == value:
   #              return key
   #  langcode=GetKey(lang)

    # text=text.replace('translate',"")
    # text=text.replace('translate ',"")

   # a=translator.translate(text,dest=langcode)

    #let=str(a)
    #a1=let.split(",")[2]
    #a2=a1.split("=")[1]

    #response={
    #    "fulfillmentText":"{}".format(a2)
    #}
    print(text)
    rep=""
    a=str(translator.detect(text))

    a1 = a.split(",")[0]
    a2=a1.split("=")[1]
    print(a2)
    if(a2 !="en"):
        res=translator.translate(text,dest='en')
        if (a2 != "ja"):

            rep = translator.translate(text, dest='ja')
            let1 = str(rep)
            a11 = let1.split(",")[2]
            a21 = a11.split("=")[1]

    if(a2=="en"):

        res=translator.translate(text,dest='ja')

    let = str(res)
    a1=let.split(",")[2]
    a2=a1.split("=")[1]


    response = {
      "fulfillmentText":"{} ".format(a2)

    }
    if rep!="":
        response = {
            "fulfillmentText": "{}    ({})".format(a21,a2)

        }


    return jsonify(response)

if __name__=="__main__":
    app.run(debug=True)