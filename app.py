from flask import Flask, render_template, request, redirect, url_for, flash
from surveys import surveys

app= Flask(__name__)
app.secret_key = "hibbidybibiddyboo"

responses = []

satisfaction_survey = surveys["satisfaction"]

@app.route("/")
def root_page():
    """Button to redirect to survey"""
    return render_template("root_page.html", satisfaction_survey=satisfaction_survey)

@app.route("/questions/<num>", methods=["GET", "POST"])
def questions_page(num):
    """Questions and answers displayed to user"""
    num = int(num)
    current_question_num = len(responses)

    if num != current_question_num or num >= len(satisfaction_survey.questions):
        flash("Invalid option. Please answer the questions in order.", "error")
        return redirect(url_for("questions_page", num=current_question_num))

    question = satisfaction_survey.questions[num]

    if num <= len(satisfaction_survey.questions) - 1:
        return render_template("questions.html", question=question, satisfaction_survey=satisfaction_survey, num=num)
    else:
        return render_template("thank_you.html")


@app.route("/answer", methods=["POST"])
def handle_answer():
    """Capture user answers and redirect to next question"""
    current_question_num = len(responses)
    choice = request.form.get(str(current_question_num))

    if len(responses) == current_question_num:
        responses.append(choice)
        next_question_num = current_question_num + 1
        if next_question_num < len(satisfaction_survey.questions):
            return redirect(url_for("questions_page", num=next_question_num))
        else:
            return redirect(url_for("thank_you_page"))
    else:
        return redirect(url_for("questions_page", num=current_question_num))

@app.route("/thank_you", methods=["GET"])
def thank_you_page():
    """Thank you message with gif"""
    return render_template("thank_you.html")