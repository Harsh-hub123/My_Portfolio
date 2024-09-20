import streamlit as st
from PIL import Image
import platform

def is_mobile():
    return platform.system().lower() in ['ios', 'android']

def display_content(content):
    if is_mobile():
        st.markdown(content, unsafe_allow_html=True)
    else:
        st.write(content)

# Set page configuration
st.set_page_config(page_title="Harsh Vardhan Mishra's Portfolio", page_icon=":rocket:", layout="wide")

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
            "description": [
                "Developed an RNN-LSTM model achieving 75% accuracy.",
                "This project involved extensive data preprocessing and hyperparameter tuning."
            ],
            "link": "https://github.com/Harsh-hub123/Stock-market-prediction-system-RNN-LSTM"
        },
        {
            "title": "Customer Churn Prediction Project",
            "description": [
                "Designed and trained a neural network model capable of processing complex, multi-dimensional customer data.",
                "Implemented advanced data preprocessing techniques, including one-hot encoding, label encoding, and feature scaling."
            ],
            "link": "https://github.com/Harsh-hub123/Customer-Churn-Prediction"
        },
        {
            "title": "Iris-2D Dataset ML Algorithm",
            "description": [
                "Achieved 95% accuracy in classifying Iris flowers using machine learning.",
                "Focused on applying supervised learning techniques to derive insights."
            ]
        }
    ],
    "skills": ["Python", "Pandas", "Generative AI", "Prompt Engineering", "Google Palm", "Hugging Face", "Langchain", "Machine Learning", "Scikit-learn", "OpenCV", "TensorFlow", "Keras"],
    "achievements": [
        "Participated in PowerBI Workshop by Growth School",
        "Presented research paper at ICADRIIA'23",
        "Committee Head in Milan'23 event at SRMIST"
    ]
}

# Custom CSS for better design and technical background
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;
            color: #333;
        }
        .main-header {
            font-size: 2.8rem;
            color: #1a237e;
            font-weight: 700;
            text-align: center;
            padding-top: 2rem;
            margin-bottom: 1rem;
        }
        .sub-header {
            font-size: 1.8rem;
            color: #283593;
            margin-bottom: 1.5rem;
            font-weight: 500;
        }
        .section {
            background-color: #ffffff;
            padding: 2rem;
            margin: 1.5rem 0;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .section:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            list-style-type: none;
            padding: 0;
            justify-content: center;
        }
        .skills-list li {
            background-color: #e8eaf6;
            color: #3f51b5;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.5rem;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        .skills-list li:hover {
            background-color: #3f51b5;
            color: #ffffff;
            transform: scale(1.05);
        }
        .contact-info {
            font-size: 1.1rem;
            color: #3f51b5;
        }
        img {
            border-radius: 50%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: 3px solid #3f51b5;
        }
        .footer {
            text-align: center;
            padding: 2rem;
            font-size: 1rem;
            color: #ffffff;
            background-color: #1a237e;
            border-radius: 8px;
            margin-top: 2rem;
        }
        .custom-button {
            background-color: #3f51b5;
            color: #ffffff;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            border: none;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .custom-button:hover {
            background-color: #1a237e;
            transform: scale(1.05);
        }
        .stSelectbox [data-baseweb=select] {
            background-color: #ffffff;
            border-radius: 8px;
            color: #333;
            border: 1px solid #3f51b5;
        }
        .stSelectbox [data-baseweb=select]:hover {
            border-color: #1a237e;
        }
        .highlight {
            color: #3f51b5;
            font-weight: 500;
        }
        .project-title {
            color: #1a237e;
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
        }
        .experience-title {
            color: #1a237e;
            font-size: 1.2rem;
            margin-bottom: 0.3rem;
        }
    </style>
""", unsafe_allow_html=True)

# Add a title and subtitle to the portfolio
st.markdown("<h1 class='main-header'>Harsh Vardhan Mishra</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3rem; color: #3f51b5;'>Aspiring Data Scientist | ML Enthusiast | Innovative Problem Solver</p>", unsafe_allow_html=True)

# Sidebar navigation with custom dropdown
st.sidebar.markdown("<h2 style='color: #1a237e;'>Portfolio Navigation</h2>", unsafe_allow_html=True)
nav = st.sidebar.selectbox("", ["Home", "Education", "Work Experience", "Projects", "Skills", "Achievements"], key="nav")

# Home Section with your own image
if nav == "Home":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://github.com/Harsh-hub123/My_Portfolio/blob/main/harsh_portfolio.jpeg", width=250)
    with col2:
        st.markdown("<h2 class='sub-header'>Welcome to My Professional Portfolio</h2>", unsafe_allow_html=True)
        st.write("As an aspiring data scientist, I combine analytical prowess with a passion for innovative problem-solving. My expertise lies in leveraging cutting-edge AI and ML techniques to extract meaningful insights from complex datasets, driving data-informed decision-making across various domains.")
        st.markdown(f"<p class='contact-info'>📧 <a href='mailto:{portfolio_data['email']}' style='color: #3f51b5;'>{portfolio_data['email']}</a></p>", unsafe_allow_html=True)
        st.markdown(f"<p class='contact-info'>📱 {portfolio_data['phone']}</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<a href='https://github.com/Harsh-hub123' target='_blank'><button class='custom-button'>GitHub Profile</button></a>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<a href='https://www.linkedin.com/in/your-profile' target='_blank'><button class='custom-button'>LinkedIn Profile</button></a>", unsafe_allow_html=True)

# Education Section
elif nav == "Education":
    st.header("Education")
    for item in portfolio_data["education"]:
        st.subheader(item["degree"])
        st.write(f"Institution: {item['institution']}")
        st.write(f"Year: {item['year']}")
        if "gpa" in item:
            st.write(f"GPA: {item['gpa']}")
        elif "percentage" in item:
            st.write(f"Percentage: {item['percentage']}")

# Work Experience Section
elif nav == "Work Experience":
    st.header("Work Experience")
    for item in portfolio_data.get("work_experience", []):
        st.subheader(item.get("role", ""))
        st.write(f"Company: {item.get('company', '')}")
        st.write(f"Duration: {item.get('duration', '')}")
        for description in item.get("description", []):
            st.write(f"- {description}")

# Projects Section
elif nav == "Projects":
    st.header("Projects")
    for item in portfolio_data.get("projects", []):
        st.subheader(item.get("title", ""))
        for description in item.get("description", []):
            st.write(f"- {description}")
        if item.get("link"):
            st.markdown(f"[View on GitHub]({item['link']})", unsafe_allow_html=True)

# Skills Section
elif nav == "Skills":
    st.header("Skills")
    skills_list = portfolio_data.get("skills", [])
    st.write("Technical skills:")
    for skill in skills_list:
        st.write(f"- {skill}")

# Achievements Section
elif nav == "Achievements":
    st.header("Achievements")
    achievements_list = portfolio_data.get("achievements", [])
    for achievement in achievements_list:
        st.write(f"- {achievement}")

# Footer
st.markdown("<div class='footer'>Thanks for visiting! Feel free to connect with me on LinkedIn or GitHub.</div>", unsafe_allow_html=True)
