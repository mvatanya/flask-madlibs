from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def madlibs_form():
    """Generate form"""
    prompts = story.prompts

    return render_template("index.html", madlib_prompts=prompts)

@app.route('/story')
def madlibs_story():
    """Generate story from inputs"""
    prompts = story.prompts
    args = request.args

    answers = {prompts[i]: args.get(str(i)+prompts[i]) for i in range(len(prompts))}
    # for i in range(len(prompts)):
    #     answers[prompts[i]] = args.get(str(i)+prompts[i])

    showing_story = story.generate(answers)

    return render_template("story.html", story_to_show=showing_story)