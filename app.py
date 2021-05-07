# packages
import streamlit as st
import streamlit.components.v1 as stc


# importing the smaller apps
from eda_app import run_eda_app
from ml_app import run_ml_app

html_temp = """
		<div style="background-color:#FFDA0F;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Diabetes Health Risk Prediction App </h1>
		<h4 style="color:white;text-align:center;">ASR - The Data Guy </h4>
		</div>
		"""

def main():
	#st.title("Main App")
	stc.html(html_temp)

	menu = ["Home", "EDA", "ML", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":
		st.subheader("Home")
		st.write("""
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
	elif choice=="EDA":
		run_eda_app()
	elif choice == "ML":
		run_ml_app()
	else:
		st.subheader("About")
		
		st.write("### Adith Sreeram - The Data Guy")
		st.text("""
		My ambitious dream to become a data scientist is soon to be a reality. Spending hours 
		looking for the most appropriate content for you never makes me tired, which will 
		obviously be preceded by long and passionate reading, writing, and prosperity in 
		sharing my wisdom brought me here. 
		As I am pursuing computer engineering, I build computer applications and muscles too.
		I strive to use my energy in data science to make significant contributions to society by 
		tackling complex problems through research and cutting edge technologies.
		Creative problem solver with strong interpersonal skills. Dreaming of taking the world 
		towards a safer and healthier future.
		I love meeting people working on exciting things. If there is any suitable role for me, 
		don't hesitate. I am open to communication on all channels. Let's discuss.

""")
		socials = ["LinkedIn", "Youtube", "Github", "GMail", "Website"]
		linkedin = "http://www.linkedin.com/in/asr373"
		youtube = "https://www.youtube.com/channel/UCo2uuNGUZbHyX3hmuJuraVQ?sub_confirmation=1"
		github = "https://github.com/ASR373"
		mail = "vishra373@gmail.com"
		website = "https://fittechie.in/"
		with st.beta_expander("Links to all my Socials"):
			a = st.selectbox("Socials", socials)
			if a =="LinkedIn":
				st.write(linkedin)
			elif a =="Youtube":
				st.write(youtube)
			elif a =="Github":
				st.write(github)
			elif a=="GMail":
				st.write(mail)
			elif a =="Website":
				st.write(website)
			

			
			


main()

