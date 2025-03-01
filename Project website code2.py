!pip install gradio pandas scikit-learn
import gradio as gr
import pandas as pd

# Define teams and cities
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Ahmedabad', 'Sharjah'
]

# Prediction function
def predict_probability(batting_team, bowling_team, city, target, score, overs, wickets):
    try:
        # Derived inputs
        runs_left = target - score
        balls_left = (20 - overs) * 6
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        # Create input DataFrame
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [10 - wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Make prediction
        result = pipe.predict_proba(input_df)
        win_prob = result[0][1] * 100  # Probability for batting team
        loss_prob = result[0][0] * 100  # Probability for bowling team

        return (
            f"{batting_team} Winning Probability: {round(win_prob, 2)}% \n"
            f"{bowling_team} Winning Probability: {round(loss_prob, 2)}%"
        )
    except Exception as e:
        return str(e)

# Gradio Interface
with gr.Blocks(css=".gradio-container {background-color: black;}") as demo:
    gr.Markdown("<h1 style='color:white;'>IPL Win Predictor</h1>")

    with gr.Row():
        batting_team = gr.Dropdown(choices=teams, label="Select Batting Team")
        bowling_team = gr.Dropdown(choices=teams, label="Select Bowling Team")
        city = gr.Dropdown(choices=cities, label="Select Host City")

    with gr.Row():
        target = gr.Number(label="Target Score")
        score = gr.Number(label="Current Score")
        overs = gr.Number(label="Overs Completed")
        wickets = gr.Number(label="Wickets Fallen")

    predict_btn = gr.Button("Predict Probability")
    output = gr.Textbox(label="Prediction Result", interactive=False)

    predict_btn.click(
        predict_probability,
        inputs=[batting_team, bowling_team, city, target, score, overs, wickets],
        outputs=[output]
    )

# Launch the app
demo.launch()
