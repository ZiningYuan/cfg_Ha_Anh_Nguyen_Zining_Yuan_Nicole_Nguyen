from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

# Display the form
@app.route("/")
def mainpage():
    return render_template("design.html")

@app.route("/american")
def american():
    return render_template("result1.html")



@app.route("/caribbean")

def caribbean():
    caribbean = requests.post("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?cuisine=caribbean&number=10&offset=0&type=main+course&query=meat",
     headers={
       "X-RapidAPI-Key": "84e499cdd1mshf3881fa78dee15cp132dbejsn0f44dfa5ad57"
     }
    )

    return render_template("result2.html", data= caribbean)




@app.route("/british")
def british():
    british = requests.post("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?cuisine=british&number=10&offset=0&type=main+course&query=meat",
    headers={
    "X-RapidAPI-Key": "84e499cdd1mshf3881fa78dee15cp132dbejsn0f44dfa5ad57"
    }
    )
    return render_template("result3.html")

@app.route("/getherfeedback", methods= ["POST"])

def gather_feedback():
    form_data = request.form
    # Print out all the form data in the terminal
    print(form_data)

    requests.post(
        "https://api.mailgun.net/v3/sandbox535ff5098b3143119f6cc2a229881dd8.mailgun.org/messages",
        auth=("api", "4fffb398d544c6af0fa4501ed3d8c4a0-7caa9475-dc56fb0d"),
        data={"from": "Excited User <mailgun@sandbox535ff5098b3143119f6cc2a229881dd8.mailgun.org>",
              "to": "Excited User <mailgun@sandbox535ff5098b3143119f6cc2a229881dd8.mailgun.org>",
              "subject" : "Feedback forms",
              "text": form_data["body"]})


    return "All OK"


app.run(debug=True)








app.run(debug=True)
