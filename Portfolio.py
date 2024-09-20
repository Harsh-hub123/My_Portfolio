import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Harsh Vardhan Mishra's Portfolio", page_icon=":star:", layout="wide")

# Portfolio Data
portfolio_data = {
    "name": "Harsh Vardhan Mishra",
    "email": "harshvmishra123@gmail.com",
    "phone": "+91 6387557185",
    "education": [
        {"degree": "BCA Data Science", "year": "2021-2024", "institution": "SRM University, Kattankulathur", "gpa": "8.22/10"},
        {"degree": "Class 12th", "year": "2020-2021", "institution": "Sant Atulanand Convent School, Varanasi", "percentage": "86.7%"}
    ],
    "work_experience": [
        {
            "role": "Data Science Intern",
            "company": "Deepsphere.ai",
            "duration": "Jun 2022 - Jul 2022",
            "description": [
                "Developed insightful analyses to inform business decisions.",
                "Engineered ML algorithms improving accuracy and performance by 10%."
            ]
        },
        {
            "role": "Data Science Intern",
            "company": "Corizo",
            "duration": "Jul 2022 - Sep 2022",
            "description": [
                "Performed data analysis and improved decision-making processes.",
                "Reduced data retrieval time by 35% using Python."
            ]
        }
    ],
    "projects": [
        {
            "title": "Google Stock Price Prediction",
            "description": "Developed an RNN-LSTM model achieving 75% accuracy."
        },
        {
            "title": "Sales Analytics",
            "description": "Created Power BI dashboards to analyze sales and profit data."
        },
        {
            "title": "Iris-2D Dataset ML Algorithm",
            "description": "Achieved 95% accuracy in classifying Iris flowers using machine learning."
        }
    ],
    "skills": ["Python", "Generative AI","Google Palm", "Hugging Face", "Prompt Engineering","Azure Services" ,"Pandas", "Scikit-learn", "OpenCV", "TensorFlow"],
    "achievements": [
        "Participated in PowerBI Workshop by Growth School",
        "Presented research paper at ICADRIIA'23",
        "Committee Head in Milan'23 event at SRMIST"
    ]
}

# Custom CSS for better design and technical background
st.markdown("""
    <style>
        /* Custom Font */
        @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;500;700&display=swap');
        body {
            font-family: 'Raleway', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #2C3E50;
        }
        .main-header {
            font-size: 50px;
            color: #2C3E50;
            font-weight: bold;
            text-align: center;
            padding-top: 50px;
        }
        .sub-header {
            font-size: 25px;
            color: #2980b9;
            margin-bottom: 20px;
        }
        .section {
            background-color: white;
            padding: 30px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            list-style-type: none;
            padding: 0;
        }
        .skills-list li {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            margin: 5px;
            transition: background-color 0.3s ease;
        }
        .skills-list li:hover {
            background-color: #2980b9;
        }
        .contact-info {
            font-size: 18px;
            color: #3498DB;
        }
        img {
            border-radius: 50%;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #95a5a6;
        }
        /* Icon styling */
        .fa {
            margin-right: 8px;
            font-size: 18px;
            color: #3498DB;
        }
    </style>
""", unsafe_allow_html=True)

# Add a title and subtitle to the portfolio
st.markdown("<h1 class='main-header'>Harsh Vardhan Mishra's Portfolio</h1>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigate")
nav = st.sidebar.radio("Go to", ["Home", "Education", "Work Experience", "Projects", "Skills", "Achievements"])

# Home Section
if nav == "Home":
    st.markdown("<h2 class='sub-header'>Welcome!</h2>", unsafe_allow_html=True)
    st.image("https://avatars.githubusercontent.com/u/67681885?v=4", width=200)  # Replace with your own image
    st.write("I am Harsh Vardhan Mishra, a passionate data scientist eager to explore and apply new technologies.")
    st.markdown(f"<p class='contact-info'>📧 <a href='mailto:{portfolio_data['email']}'>{portfolio_data['email']}</a></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='contact-info'>📱 {portfolio_data['phone']}</p>", unsafe_allow_html=True)
    st.markdown("[GitHub](https://github.com/Harsh-hub123) | [LinkedIn](https://www.linkedin.com/in/harsh4744/)")

# Education Section
if nav == "Education":
    st.markdown("<h2 class='sub-header'>Education</h2>", unsafe_allow_html=True)
    for edu in portfolio_data["education"]:
        st.markdown(f"""
        <div class="section">
            <strong>{edu['degree']}</strong> - {edu['institution']} <br>
            <i>{edu['year']}</i> <br>
            GPA: {edu.get('gpa', edu.get('percentage'))}
        </div>
        """, unsafe_allow_html=True)

# Work Experience Section with expanders
if nav == "Work Experience":
    st.markdown("<h2 class='sub-header'>Work Experience</h2>", unsafe_allow_html=True)
    for job in portfolio_data["work_experience"]:
        with st.expander(f"{job['role']} at {job['company']} ({job['duration']})"):
            for desc in job["description"]:
                st.write(f"- {desc}")

# Projects Section with clickable links
if nav == "Projects":
    st.markdown("<h2 class='sub-header'>Projects</h2>", unsafe_allow_html=True)
    for project in portfolio_data["projects"]:
        st.markdown(f"""
        <div class="section">
            <strong>{project['title']}</strong>: {project['description']} <br>
            {f'[View on GitHub](https://github.com/Harsh-hub123/Stock-market-prediction-system-RNN-LSTM)' if project['title'] == 'Google Stock Price Prediction' else ''}
        </div>
        """, unsafe_allow_html=True)

# Skills Section with tags and hover effects
if nav == "Skills":
    st.markdown("<h2 class='sub-header'>Technical Skills</h2>", unsafe_allow_html=True)
    st.markdown("<ul class='skills-list'>", unsafe_allow_html=True)
    for skill in portfolio_data["skills"]:
        st.markdown(f"<li>{skill}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

# Achievements Section
if nav == "Achievements":
    st.markdown("<h2 class='sub-header'>Achievements and Participation</h2>", unsafe_allow_html=True)
    for achievement in portfolio_data["achievements"]:
        st.markdown(f"""
        <div class="section">
            <strong>{achievement}</strong>
        </div>
        """, unsafe_allow_html=True)

# Footer Section
st.sidebar.markdown("---")
st.sidebar.write("Designed with ❤️ using Streamlit")

st.markdown("<div class='footer'>Built by Harsh Vardhan Mishra | Powered by Streamlit</div>", unsafe_allow_html=True)
