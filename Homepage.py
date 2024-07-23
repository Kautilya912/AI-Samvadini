import streamlit as st
#im=st.image("icon.png")
from streamlit_option_menu import option_menu
from app_utils import switch_page
#import streamlit as st
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "AI Samvadini", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English", "Comming Soon!"])

if lan == "English":
    home_title = "AI Samvadini"
    home_introduction = "Welcome to AI Samvadini, empowering your Podcaste with generative AI."
    with st.sidebar:
        st.markdown('AI Samvadini  - S1.0.0')
        st.markdown(""" 
        #### Let's contact:
        [Kautilya Utkarsh](https://www.linkedin.com/in/kautilya-utkarsh-mishra-187818265/)
        
        [At C# Corner ](https://www.c-sharpcorner.com/members/kautilya-utkarsh)
                         
        
        #### Product of

        [CSharp Corner](https://www.c-sharpcorner.com/)
                    
        
        #### Powered by
    
        [OpenAI](https://openai.com/)
              
        [Langchain](https://github.com/hwchase17/langchain)
            
                    """)  
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to AI Samvadini! 👏 AI Samvadini is your personal podcaste interviewer powered by generative AI that conducts Podcaste."
                " You can upload your resume and enter job profile, and AI Samvadini will ask you customized questions. Additionally, you can configure your own Podcast Interviewer!")
    st.markdown("""\n""")
    with st.expander("Updates"):
        st.write("""
        07/10/2024
        - Fix the error that was occuring on the Behavioral page """)
    with st.expander("What's coming next?"):
        st.write("""
        Improved voice interaction for a seamless experience. """)
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Customize!"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚In this session, the AI Samvadini will assess your technical skills as they relate to the proived description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the AI Samvadini will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ """
        )
        if st.button("Start Interview!"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the AI Samvadini will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own AI Samvadini and practice with it!
             - Configure AI Samvadini in different specialties.
             - Configure AI Samvadini in different personalities.
             - Different tones of voice.
             
             Coming at the end of July""")
    st.markdown("""\n""")
    st.markdown("#### Kautilya Utkarsh")
  