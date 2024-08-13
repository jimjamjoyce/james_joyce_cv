#!/usr/bin/env python
# coding: utf-8

#### IMPORTS ####
import os
import streamlit as st
import pandas as pd
import numpy as np
import base64
import requests
import json


##########################################
##  GLOBAL PARAMETERS                   ##
##########################################

st.set_page_config(page_title="James Joyce CV",
                   page_icon="📄",
                   initial_sidebar_state="collapsed",
                   layout = "centered")

image_path = os.path.join(os.getcwd(), 'media')
downloadfile_path = os.path.join(os.getcwd(), 'download_files')
css_path = os.path.join(os.getcwd(), 'styles')
css_file = os.path.join(css_path, 'main.css')

##########################################
##  STYLE & FORMATTING                  ##
##########################################

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# CSS for tables

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>   """
center_heading_text = """
    <style>
        .col_heading   {text-align: center !important}
    </style>          """
center_row_text = """
    <style>
        td  {text-align: center !important}
    </style>      """

# Inject CSS with Markdown

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(os.path.join(image_path,'changing-pastel2.gif'))

# # Expander Styling
st.markdown(
"""
<style>
.streamlit-expanderHeader {
 #   font-weight: bold;
    background: aliceblue;
    font-size: 18px;
}
</style>
""",
    unsafe_allow_html=True,
)

##########################################
##  Title, Tabs, and Sidebar            ##
##########################################

st.image(os.path.join(image_path, 'JAMES-JOYCE-title.png'), use_column_width = True)
st.write('''##### <span style="color:white"><div style="text-align: center;">Come with us now on a journey through time and space
            ''', unsafe_allow_html=True)
# st.image("https://i.gifer.com/NCqX.gif")
tab_intro, tab_cv, tab_personality, tab_contact = st.tabs(["**INTRODUCTION**",
                                                              "**CV**",
                                                              "**PERSONALITY**",
                                                              "**CONTACT**",
                                                              ])

#########################################
##             HELLO! TAB              ##
#########################################
with tab_intro:
    st.markdown(" #### Hello!")
    st.markdown('''<div style="text-align: justify;">
    My name is James, welcome to my digital CV! Python-coded by yours truly (with smatterings of CSS styling here and there), and
    brought to life through the medium of Streamlit.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    It's now incumbent upon me to reduce the full scope of 8+ years of experience down to a few palatable bullet points,
    demonstrating my diverse range of expertise across hospitality, entertainment and most recently data analytics and coding.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    As seemingly daunting and bizarre an endeavour as this is, I can assure you that I have tried my utmost to make
    sure your time isn't wasted, and that your experience is both smooth and enlightening.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    Along the top in the tabs are all the core elements of my profile for an application. All
    documents are available to download via the 'Export' buttons, so please feel free should you require any of them.
    If you have any questions, my contact details are available on the 'Contact' tab above.
    </div>''', unsafe_allow_html=True)
    ""
    col1, col2, col3 = st.columns([1,1,1])
    st.markdown(" ##### Past")
    st.markdown('''<div style="text-align: justify;">
    Up until last year, my career has been within the Events and Hospitality sectors. This varied and dynamic
    industry has inculcated in me a host of soft skills, most notably Teamwork, Communication, Dilligence,
    and Tenacity.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    My progression culminated as Production & Projects Manager at Dabbers Social Bingo. I feel like the
    whimsiscal nature of Bingo often prejudiced people as to the seriousness the role demanded, where my main
    achievements and responsibilities were: the most.
    </div>''', unsafe_allow_html=True)
    ""
    #
    st.markdown("- 📝 Project Managing the £250k roll out of a second venue within an 8-week turnaround time.")
    st.markdown("- 📆 Managing and booking talent for over 100 slots each month.")
    st.markdown("- 💰 Monthly reconciliation of the Production department expenditure and budget.")
    st.markdown("- 🎪 Liaising with festivals and third parties on external events to ensure seamless delivery of shows.")
    st.markdown('''- 🎨 Graphic Design - creating digital assets for social channels / website as well as physical collateral
                in the form of food & drink menus, venue posters, promo flyers, venue artwork.''')
    st.markdown("- 👁 Designing and creating visual content to supplement the shows on PowerPoint and iMovie")
    st.markdown("- 🚙 Driving and delivering our external shows all over the country.")
    st.markdown("- 🌟 Dressing the venue for seasonal periods (Christmas, Halloween, Valentines Day etc.).")
    st.markdown("- 🛠 Making props for our shows to increase production value and enhance customer experience.")
    ""
    st.markdown('''<div style="text-align: justify;">
    The most common follow-up question, upon being asked what I do, by far was "So, do you call the numbers?". In an ideal world,
    I'd reel off the above list above so that my inquisitor would know that it's not all fun and games. Alas in the real world,
    and within the confines of idle chit-chat it's much quicker and easier to respond with a simple "No, I just book Drag Queens
    and stuff."
    </div>''', unsafe_allow_html=True)
    ""
    # CSS to indent list:
    st.markdown('''<style>
    [data-testid="stMarkdownContainer"] ul{padding-left:40px;}
    </style>
    ''', unsafe_allow_html=True)
    #
    ""
    st.markdown(" ##### Present")
    st.markdown('''<div style="text-align: justify;">
    Currently I am living the lavish existence of a multi-faceted freelancer. Although I left Dabbers permanently in June 2023,
    I have since continued to provide ad-hoc Graphic Design (see portfolio tab) and Event Management services when their show is
    contracted externally (festivals, offices, corporate away days etc.).
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    I also provide Bar Operations and Management expertise to Columbia Events, a start-up bar company that provides white-label
    bar operations services to a multiude of Events, most notably Formula 1, Moto GP, Cambridge Folk Festival, Pub in the Park,
    and Field Maneuvers Festival.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    My main duties include:
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown("- ⏲ Preparing bar for service - line clean, arrange bar displays, configure tills for staff to use.")
    st.markdown("- ✅ To brief and be responsible for all personnel working on my bar.")
    st.markdown("- 🧮 Stock Management throughout the event.")
    st.markdown("- 👮‍♂️ Managing and enforcing the legalities of bar operation under my own Personal Alcohol License.")
    st.markdown("- 🛠 Technical maintenance of the bar (changing kegs & gas cylinders, quality control of beer pours).")

    st.markdown(" ##### Future")
    st.markdown('''<div style="text-align: justify;">
    The main thing I have learned about what excites me in my career is the idea of visual storytelling. Whether it's through
    design, spreadsheets and data, dashboards, or even cold hard copywriting, I feel I am best placed in positions where a visual explanation
    is needed in order to help a team or group understand something.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    I hope to be part of a team where storytelling is at the heart of the group endeavour, and I feel I have the skills and
    experience, albeit unorthodox and unusual, to do just that.
    </div>''', unsafe_allow_html=True)
    ""


#########################################
##               CV TAB                ##
#########################################
with tab_cv:

    cv = os.path.join(downloadfile_path, 'James_Joyce_CV_24.pdf')
    st.download_button(label="Export CV",
                       data=cv,
                       file_name="James_Joyce_CV_24.pdf")
    st.image(os.path.join(downloadfile_path, 'James_Joyce_CV_24.png'), use_column_width = True)


#########################################
## PERSONALITY TAB                     ##
#########################################
with tab_personality:
    st.markdown('''<div style="text-align: justify;">
    Nothing quite as rivetting as reading about someone else's personality test results is there? It's on par with listening
    to other people's dreams and horoscopes.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    But all jokes aside, these are NOT the results of some Buzzfeed "which type of naan bread are you?"
    style quiz. This personality assessment is based on the Big Five Aspects Scale, a scientific multi-dimensional standard
    recognised across the field across psychology, with each of the Big Five Aspects being made up of two sub-aspects,
    which are also detailed below.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    The below results show where I stand in comparison to others in the general population as a percentile. For example
    I scored 98 in Extraversion (humble brag 💅🏼). This means that in a room of 100 people, there would only be 1 person
    more extraverted than me.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    In brirf summary I'm an extremely extraverted, intelligent, and creative team-player (that you should definitely hire into your
    team 😁), whose shortcomings lie predominantly in emotional volatility and industriousness. But you can't have it all can you?
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    This assessment really helped me to understand myself better in terms of playing to my strengths and being aware in the areas I
    am lacking in.
    </div>''', unsafe_allow_html=True)
    ""
    st.divider()
    #### CREATING DATAFRAMES TO BE DISPLAYED ####
    aggreableness_df = pd.DataFrame({"Dimension": ["Aggreableness", "Compassion", "Politeness"],
                                    "Percentile": [94, 93, 89]})

    conscientiousness_df = pd.DataFrame({"Dimension": ["Conscientiousness", "Industriousness", "Orderliness"],
                                         "Percentile": [59, 32, 80]})

    extraversion_df = pd.DataFrame({"Dimension": ["Extraversion", "Enthusiasm", "Assertiveness"],
                                    "Percentile": [98, 95, 98]})

    neuroticism_df = pd.DataFrame({"Dimension": ["Neuroticism", "Withdrawal", "Volatility"],
                                   "Percentile": [64, 19, 93]})

    openness_df = pd.DataFrame({"Dimension": ["Openness", "Intellect", "Aesthetics"],
                                "Percentile": [87, 86, 80]})

    #### 1. AGREEABLENESS SECTION ####
    st.markdown("##### 1. AGREEABLENESS")
    ""
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(aggreableness_df, hide_index=True)

    with col2:
        st.bar_chart(aggreableness_df, x = "Dimension", y = "Percentile", horizontal=True)

    st.markdown('''<div style="text-align: justify;">
    Agreeableness is the primary dimension of interpersonal interaction in the Big Five personality
    trait scientific model. It is a very complex trait, with marked positive and negative elements all along
    its distribution.
    </div>''', unsafe_allow_html=True)
    ""
    st.divider()


    #### 2. CONSCIENTIOUSNESS SECTION ####
    st.markdown("##### 2. CONSCIENTIOUSNESS")
    ""
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(conscientiousness_df, hide_index=True)

    with col2:
        st.bar_chart(conscientiousness_df, x = "Dimension", y = "Percentile", horizontal=True)

    st.markdown('''<div style="text-align: justify;">
    Conscientiousness is the primary dimension of dutiful achievement in the Big Five personality trait scientific model.
    It measures sense of obligation, attention to detail, hard work, persistence, cleanliness, effciency, as well as
    adherence to rules, standards and processes.
    </div>''', unsafe_allow_html=True)
    ""
    st.divider()

    #### 3. EXTRAVERSION SECTION ####
    ""
    st.markdown("##### 3. EXTRAVERSION")
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(extraversion_df, hide_index=True)

    with col2:
        st.bar_chart(extraversion_df, x = "Dimension", y = "Percentile", horizontal=True)

    st.markdown('''<div style="text-align: justify;">
    Extraversion is the primary dimension of positive emotion in the Big Five model. Extraversion is a measure of
    general sensitivity to positive emotions such as hope, joy, anticipation and approach, particularly in social situations.
    The two aspects of extraversion are enthusiasm and assertiveness.
    </div>''', unsafe_allow_html=True)
    ""
    st.divider()

    #### 4. NEUROTICISM SECTION ####
    ""
    st.markdown("##### 4. NEUROTICISM")
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(neuroticism_df, hide_index=True)

    with col2:
        st.bar_chart(neuroticism_df, x = "Dimension", y = "Percentile", horizontal=True)

    st.markdown('''<div style="text-align: justify;">
    Neuroticism is the primary dimension of negative emotion in the Big Five personality model. Neuroticism is a measure of
    general sensitivity to negative emotions such as pain, sadness, irritable or defensive anger, fear and anxiety.
    The two aspects of neuroticism are withdrawal and volatility.
    </div>''', unsafe_allow_html=True)
    ""
    st.divider()

    #### 5. OPENNESS ####
    ""
    st.markdown("##### 5. OPENNESS")
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(openness_df, hide_index=True)

    with col2:
        st.bar_chart(openness_df, x = "Dimension", y = "Percentile", horizontal=True)

    st.markdown('''<div style="text-align: justify;">
    Openness is the primary dimension of creativity, artistic interest and intelligence, particularly verbal. Openness is
    a measure of interest in novelty, art, literature, abstract thinking, philosophy as well as sensitivity to aesthetic
    emotions and beauty. The two aspects of openness are intellect and aesthetics.
    </div>''', unsafe_allow_html=True)
    ""
    st.divider()


#########################################
## CONTACT TAB                         ##
#########################################
with tab_contact:
    st.markdown('''<div style="text-align: justify;">
    EMAIL: jimjoywork@live.com
    </div>''', unsafe_allow_html=True)
    ""
    ""
    st.markdown('''<div style="text-align: justify;">
    PHONE: +44 7535 358 691
    </div>''', unsafe_allow_html=True)
    ""
    st.page_link("http://www.google.com", label="Google", icon="🌎")
    st.link("http://www.linkedin.com/in/jj-james-joyce", label="LinkedIn")
    st.link_button("Get in touch", "mailto:jimjoywork@live.com", type = "primary")
