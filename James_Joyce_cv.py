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

st.set_page_config(page_title='James Joyce CV',
                   page_icon='📄',
                   initial_sidebar_state='expanded',
                   layout = 'centered')

image_path = os.path.join(os.getcwd(), 'media')
downloadfile_path = os.path.join(os.getcwd(), 'download_files')
css_path = os.path.join(os.getcwd(), 'styles')
css_file = os.path.join(css_path, 'main.css')

##########################################
##  STYLE & FORMATTING                  ##
##########################################

with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# CSS for tables

hide_table_row_index = '''
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>   '''
center_heading_text = '''
    <style>
        .col_heading   {text-align: center !important}
    </style>          '''
center_row_text = '''
    <style>
        td  {text-align: center !important}
    </style>      '''

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
    background-image: url('data:image/png;base64,%s');
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(os.path.join(image_path,'changing-pastel2.gif'))

# # Expander Styling
st.markdown(
'''
<style>
.streamlit-expanderHeader {
 #   font-weight: bold;
    background: aliceblue;
    font-size: 18px;
}
</style>
''',
    unsafe_allow_html=True,
)

##########################################
##  Title, Tabs, and Sidebar            ##
##########################################

st.image(os.path.join(image_path, 'JAMES-JOYCE-title.png'), use_column_width = True)
tab_intro, tab_cv, tab_personality, tab_contact = st.tabs(['**INTRO**',
                                                           '**WORK EXPERIENCE**',
                                                           '**PERSONALITY**',
                                                           '**CONTACT**',
                                                           ])

#########################################
##             INTRO TAB               ##
#########################################
with tab_intro:
    st.balloons()
    st.markdown(' #### INTRODUCTION',unsafe_allow_html=True)
    st.markdown('''<div style='text-align: justify;'>
    Hello, my name is James and welcome to my digital CV!
    <br>
    <br>
    Python-coded by yours truly (with smatterings of CSS styling here and there), and brought to life
    through the medium of Streamlit.
    <br>
    <br>
    It's now incumbent upon me to reduce the full scope of 8+ years of experience down to a few palatable bullet points,
    demonstrating my diverse range of expertise across hospitality, entertainment and most recently data analytics and coding.
    <br>
    <br>
    As seemingly daunting and bizarre an endeavour as this is, I can assure you that I have tried my utmost to make
    sure your time isn't wasted, and that your experience is both smooth and enlightening.
    <br>
    <br>
    Along the top in the tabs are all the core elements of my profile for an application. All
    documents are available to download via the 'Export' buttons, so please feel free should you require any of them.
    If you have any questions, my contact details are available on the 'Contact' tab above.
    </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()
    # col1, col2, col3 = st.columns([1,1,1])
    st.markdown(' ##### PAST')
    st.markdown('''<div style='text-align: justify;'>
    Up until last year, my career has been within the Events and Hospitality sectors. This varied and dynamic
    industry has inculcated in me a host of soft skills, most notably Teamwork, Communication, Dilligence,
    and Tenacity.
    <br>
    <br>
    My progression culminated as Production & Projects Manager at Dabbers Social Bingo. I feel like the
    whimsiscal nature of Bingo often prejudiced people as to the seriousness the role demanded, where my most
    notable achievement was Project Managing the £250k roll out of a second venue within an 8-week turnaround time.
    <br>
    <br>
    During this time the most common follow-up question, upon being asked what I do, by far was
    'So, do you call the numbers?'. In an ideal world, I'd reel off a boring list of responsibilities
    trying to effect as much matyrdom in my tone as possible so that my inquisitor would know that it's
    not all fun and games. Alas in the real world, within the confines of idle chit-chat
    it's much quicker and easier to respond with a simple "No, I just book Drag Queens and stuff".
    </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()
    st.markdown(' ##### PRESENT')
    st.markdown('''<div style='text-align: justify;'>
    Currently I am living the lavish existence of a multi-faceted freelancer. Although I left Dabbers permanently in June 2023,
    I have since continued to provide ad-hoc Graphic Design (see portfolio tab) and Event Management services when their show is
    contracted externally (festivals, offices, corporate away days etc.).
    <br>
    <br>
    I also provide Bar Operations and Management expertise to Columbia Events, a start-up bar company that provides white-label
    bar operations services to a multiude of Events, most notably Formula 1, Moto GP, Cambridge Folk Festival, Pub in the Park,
    and Field Maneuvers Festival.
    </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()
    st.markdown(' ##### FUTURE')
    st.markdown('''<div style='text-align: justify;'>
    The main thing I have learned about what excites me in my career is the idea of visual storytelling. Whether it's through
    design, spreadsheets and data, dashboards, or even cold hard copywriting, I feel I am best placed in positions where a visual explanation
    is needed in order to help a team or group understand something.
    <br>
    <br>
    I hope to be part of a team where storytelling is at the heart of the group endeavour, and I feel I have the skills and
    experience, albeit unorthodox and unusual, to do just that.
    </div>''', unsafe_allow_html=True)


#########################################
##        WORK EXPERIENCE TAB          ##
#########################################
with tab_cv:

    # cv = os.path.join(downloadfile_path, 'James_Joyce_CV_24.2.pdf')
    st.download_button(label='Export CV',
                       data=os.path.join(downloadfile_path, 'James_Joyce_CV_24.2.pdf'),
                       file_name='James_Joyce_CV_24.2.pdf')

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**MAY 2023 - PRESENT**', unsafe_allow_html=True)

    with col2:
        st.write('''**DABBERS SOCIAL BINGO | London**
                 <br>
                 **Freelance Graphic Design & Marketing**''',
                 '''<div style='text-align: justify;'>
                 - Managed website content on WordPress, creating new promotional pages.
                 <br>
                 - Created newsletters in collaboration with Creative Director and Business Development Manager.
                 <br>
                 - Designed digital and print assets for various promotional campaigns (portfolio available via QR code.)
                 <br>
                 </div>''', unsafe_allow_html=True)
        ''
        st.write('''**AGENCY UNKNOWN | London**
                 <br>
                 **Freelance Graphic Design & Marketing**''',
                 '''<div style='text-align: justify;'>
                 - Produced bespoke gameshow-style events for businesses and festivals.
                 <br>
                 - Designed event assets, including puzzles, tasks, and visual aids, in collaboration with the Creative Director.
                 </div>''', unsafe_allow_html=True)
        ''
        st.write('''**COLUMBIA EVENTS | UK-wide**
                 <br>
                 **Bar Management & Operations**''',
                 '''<div style='text-align: justify;'>
                 - Managed bar operations at various high-profile events including music festivals and Formula 1.
                 <br>
                 - Supervised night shifts at Field Maneuvers Festival, overseeing 4 bars, 4 managers, and 40 staff,
                 generating six-figure revenue.
                 </div>''', unsafe_allow_html=True)
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**JAN - MAY 2024**', unsafe_allow_html=True)

    with col2:
        st.write('''**BALFOUR WINERY | Kent**
                 <br>
                 **Winery Technician**
                 <div style='text-align: justify;'>
                 - Developed a Harvest Dashboard on PowerBI for rapid information dissemination.
                 <br>
                 - Monitored vineyard data for ripeness and predicted harvest yields.
                 <br>
                 - Streamlined data management for product quality and safety control.
                 <br>
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**DEC 2024**', unsafe_allow_html=True)

    with col2:
        st.write('''**NATURAL HISTORY MUSEUM | London**
                 <br>
                 **Art Installation**
                 '<div style='text-align: justify;'>
                 - Contracted to design, create, and install a Pledge Wall for the Museum’s annual NYE event,
                 which centered on the subject of the Environment.
                 <br>
                 - The Museum wanted a Pledge Wall where people would write eco-friendly commitments for 2024.
                 <br>
                 - For my concept I used a fallen tree which I covered in gold leaf, and then I laid out 300 gold
                 tags on the floor all around the tree to make it look like the tree was dead.
                 <br>
                 - Attendees would write their pledges on the tags and hang them on the tree, thus ‘bringing
                 the tree back to life’.
                 <br>
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**NOV 2023 - JAN 2024**', unsafe_allow_html=True)

    with col2:
        st.write('''**MR. JI | London**
                 <br>
                 **Assistant General Manager**''',
                 '''<div style='text-align: justify;'>
                 - Managed floor operations at an Asian-European fusion restaurant in Camden Town.
                 <br>
                 - Contributed to a significant increase in revenue and customer satisfaction, demonstrated
                 by the amount of 4-star and 5-star reviews acquired in my time there.
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**NOV 2023**', unsafe_allow_html=True)

    with col2:
        st.write('''**Koko Camden | London**
                 <br>
                 **Artist Liaison**
                 <div style='text-align: justify;'>
                 - Provided liaison services for high-profile artists at a 1500-capacity club.
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**SEP - NOV 2023**', unsafe_allow_html=True)

    with col2:
        st.write('''**BALFOUR WINERY | Kent**
                 <br>
                 **Harvest 2023 Supervisor**
                 <div style='text-align: justify;'>
                 - 3rd Vintage, given extra responsibility to coordinate the day shift team of 4.
                 <br>
                 Setting up tanks, pumps, lines for initial pressings of the day.
                 <br>
                 - Management and operating 3 x 4-ton presses.
                 <br>
                 - Peak Harvest processing approx. 40 tons per shift
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**JUL - SEP 2023**', unsafe_allow_html=True)

    with col2:
        st.write('''** **CAREER BREAK****
                 <br>
                 **Data Science, Le Wagon**
                 <div style='text-align: justify;'>
                 I took a career break from Events and Production to upskill and change my career prospects. I chose
                 to do a Data Science Bootcamp with Le Wagon. The course provided me with a wealth of skills and knowledge:
                 <br>
                 - Python Language & Packages (Numpy, Pandas, SciPy SQL)
                 <br>
                 - Data Cleaning, Preprocessing & Engineering
                 <br>
                 - Data Visualisation (MatPlotLib & Seaborn)
                 <br>
                 - APIs (Fast API) and Docker
                 <br>
                 - Google Cloud Services (Big Query, Cloud Storage, Virtual Machines)
                 <br>
                 - Deep Learning & Machine Learning (SciKit-Learn, Keras, Tensorflow)
                 <br>
                 - Streamlit App Design, Development & Deployment
                 </div>''', unsafe_allow_html=True)

        ''

        st.write('''**FREELANCE WORK DURING CAREER BREAK**
                 <br>
                 Dabbers Social Bingo - Event Management & Graphic Design
                 <br>
                 Columbia Events - Bar Management & Operations
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**DEC 2019 - JUN 2023**', unsafe_allow_html=True)

    with col2:
        st.write('''**DABBERS SOCIAL BINGO | London**
                 <br>
                 **Projects & Production Manager**
                 <div style='text-align: justify;'>
                 - Managed the £250k rollout of a new venue in Hackney, including critical path,
                 budgeting and supplier coordination.
                 <br>
                 - Led a production team in delivering high-quality events and bespoke private events
                 Designed both digital and print marketing material.
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**MAR - SEP 2019**', unsafe_allow_html=True)

    with col2:
        st.write('''**FREELANCE STAGE MANAGEMENT & ARTIST LIAISON**
                 <br>
                 **Various Festivals & Events**
                 <div style='text-align: justify;'>
                 **Main Responsibilities**
                 <br>
                 - Collating all artists’ technical riders and checking that specs had been met.
                 <br>
                 - Acting as a runner on behalf of Stage Managers.
                 <br>
                 - Chaperoning talent to and from their respective stages, providing friendly assistance throughout.
                 <br>
                 <br>
                 **Outlook & Dimensions, Croatia**
                 <br>
                 Working with Eye Of The Storm, delivering talent Management for 2 of the most
                 revered British festival brands.
                 <br>
                 <br>
                 **Gottwood Festival, Wales**
                 <br>
                 Stage Manager at the Garden stage, the biggest and busiest at the festival.
                 <br>
                 <br>
                 **South Central, Portsmouth**
                 <br>
                 Stage Manager at the second biggest stage.
                 <br>
                 <br>
                 **AVA Festival & Conference, Printworks**
                 <br>
                 - Industry-leading Electronic Music conference, consisting of talks and workshops with
                 5000+ attendees.
                 <br>
                 - Responsible for one of four roomsas part of this Industry-leading Electronic Music
                 conference, executing a program of 6 x talks with 200+ attendance per talk.
                 <br>
                 - Led a team in efficiently executing a two-day event build and achieving a quick
                 two-hour turnover of the entire Printworks venue from conference to club for the afterparty.
                 <br>
                 <br>
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**SEP 2018 - DEC 2019**', unsafe_allow_html=True)

    with col2:
        st.write('''**BALFOUR WINERY | Kent**
                 <br>
                 **Cellar Hand, Production Supervisor**
                 <div style='text-align: justify;'>
                 - Overseeing the intricate processes within the various stages
                 of sparkling wine production, including bottling, discorging, packaging, and
                 warehouse management.
                 <br>
                 - Managing a team of 4 in an intense and dangerous winery environment.
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**JUL - OCT 2018**', unsafe_allow_html=True)

    with col2:
        st.write('''**SHELTER | Amsterdam**
                 <br>
                 **Junior Communications Manager**
                 <div style='text-align: justify;'>
                 - Preeminent club in Amsterdam's world-renowned nightlife scene.
                 <br>
                 - Learned Photoshop on the job to develop engaging social media content and
                 implemented strategic content schedules.
                 <br>
                 - Created an online presence that maximized ticket sales in the competitive
                 Summer market.
                 <br>
                 - Managed website updates and listings, ensuring accurate and up-to-date
                 information for users.
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**MAY 2018**', unsafe_allow_html=True)

    with col2:
        st.write('''**UN1T PRODUCTIONS | London**
                 <br>
                 **Artist Liaison, Mutiny Festival**
                 <div style='text-align: justify;'>
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**MAR - NOV 2017**', unsafe_allow_html=True)

    with col2:
        st.write('''**SOCIAL EVENTS WORLDWIDE | Brighton**
                 <br>
                 **Business Development**
                 <div style='text-align: justify;'>
                 - Successfully identified and secured new event locations, establishing 8
                 new Oktoberfest events.
                 <br>
                 - Collaborated with local councils and maintained strong relationships with
                 councilors to ensure compliance and safety standards were met throughout the
                 planning and execution of events.
                 <br>
                 - Event Management at renowned event brands including The Social Festival,
                 Madness, Big Day Out, and Oktoberfest.
                 </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()

    col1, col2, = st.columns([1.7,5],gap='small',vertical_alignment='top')
    with col1:
        st.write('**JAN - MAR 2017**', unsafe_allow_html=True)

    with col2:
        st.write('''**THE COLUMBO GROUP | London**
                 <br>
                 **Business Development**
                 <div style='text-align: justify;'>
                 - Reporting directly to the Press Officer, I was tasked with copywriting
                 duties for the Group's venues - PHONOX, XOYO, Jazz Cafe, Camden Assembly,
                 Blues Kitchen.
                 <br>
                 - I oversaw the management of website content across all venues on WordPress,
                 updating listings, event information, ticket links.
                 </div>''', unsafe_allow_html=True)


#########################################
##          PERSONALITY TAB            ##
#########################################
with tab_personality:
    st.markdown('''<div style='text-align: justify;'>
    Nothing quite as rivetting as reading about someone else's personality test results is there? It's on par with listening
    to other people's dreams and horoscopes.
    <br>
    <br>
    But all jokes aside, these are NOT the results of some Buzzfeed 'which type of naan bread are you?'
    style quiz. This personality assessment is based on the Big Five Aspects Scale, a scientific multi-dimensional standard
    recognised across the field across psychology, with each of the Big Five Aspects being made up of two sub-aspects,
    which are also detailed below.
    <br>
    <br>
    The below results show where I stand in comparison to others in the general population as a percentile. For example
    I scored 98 in Extraversion (humble brag 💅🏼). This means that in a room of 100 people, there would only be 1 person
    more extraverted than me.
    <br>
    <br>
    In brief summary I'm an extremely extraverted, intelligent, and creative team-player (that you should definitely hire into your
    team 😁), whose shortcomings lie predominantly in emotional volatility and industriousness. But you can't have it all can you?
    <br>
    <br>
    This assessment really helped me to understand myself better in terms of playing to my strengths and being aware in the areas I
    am lacking in.
    </div>''', unsafe_allow_html=True)
    ''
    ''
    st.divider()
    #### CREATING DATAFRAMES TO BE DISPLAYED ####
    aggreableness_df = pd.DataFrame({'Dimension': ['Aggreableness', 'Compassion', 'Politeness'],
                                    'Percentile': [94, 93, 89]})

    conscientiousness_df = pd.DataFrame({'Dimension': ['Conscientiousness', 'Industriousness', 'Orderliness'],
                                         'Percentile': [59, 32, 80]})

    extraversion_df = pd.DataFrame({'Dimension': ['Extraversion', 'Enthusiasm', 'Assertiveness'],
                                    'Percentile': [98, 95, 98]})

    neuroticism_df = pd.DataFrame({'Dimension': ['Neuroticism', 'Withdrawal', 'Volatility'],
                                   'Percentile': [64, 19, 93]})

    openness_df = pd.DataFrame({'Dimension': ['Openness', 'Intellect', 'Aesthetics'],
                                'Percentile': [87, 86, 80]})

    #### 1. AGREEABLENESS SECTION ####
    st.markdown('##### 1. AGREEABLENESS')
    ''
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(aggreableness_df, hide_index=True)

    with col2:
        st.bar_chart(aggreableness_df, x = 'Dimension', y = 'Percentile', horizontal=True)

    st.markdown('''<div style='text-align: justify;'>
    Agreeableness is the primary dimension of interpersonal interaction in the Big Five personality
    trait scientific model. It is a very complex trait, with marked positive and negative elements all along
    its distribution.
    </div>''', unsafe_allow_html=True)
    ''
    st.divider()

    #### 2. CONSCIENTIOUSNESS SECTION ####
    st.markdown('##### 2. CONSCIENTIOUSNESS')
    ''
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(conscientiousness_df, hide_index=True)

    with col2:
        st.bar_chart(conscientiousness_df, x = 'Dimension', y = 'Percentile', horizontal=True)

    st.markdown('''<div style='text-align: justify;'>
    Conscientiousness is the primary dimension of dutiful achievement in the Big Five personality trait scientific model.
    It measures sense of obligation, attention to detail, hard work, persistence, cleanliness, effciency, as well as
    adherence to rules, standards and processes.
    </div>''', unsafe_allow_html=True)
    ''
    st.divider()

    #### 3. EXTRAVERSION SECTION ####
    ''
    st.markdown('##### 3. EXTRAVERSION')
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(extraversion_df, hide_index=True)

    with col2:
        st.bar_chart(extraversion_df, x = 'Dimension', y = 'Percentile', horizontal=True)

    st.markdown('''<div style='text-align: justify;'>
    Extraversion is the primary dimension of positive emotion in the Big Five model. Extraversion is a measure of
    general sensitivity to positive emotions such as hope, joy, anticipation and approach, particularly in social situations.
    The two aspects of extraversion are enthusiasm and assertiveness.
    </div>''', unsafe_allow_html=True)
    ''
    st.divider()

    #### 4. NEUROTICISM SECTION ####
    ''
    st.markdown('##### 4. NEUROTICISM')
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(neuroticism_df, hide_index=True)

    with col2:
        st.bar_chart(neuroticism_df, x = 'Dimension', y = 'Percentile', horizontal=True)

    st.markdown('''<div style='text-align: justify;'>
    Neuroticism is the primary dimension of negative emotion in the Big Five personality model. Neuroticism is a measure of
    general sensitivity to negative emotions such as pain, sadness, irritable or defensive anger, fear and anxiety.
    The two aspects of neuroticism are withdrawal and volatility.
    </div>''', unsafe_allow_html=True)
    ''
    st.divider()

    #### 5. OPENNESS ####
    ''
    st.markdown('##### 5. OPENNESS')
    col1, col2, = st.columns([0.3, 0.7])
    with col1:
        st.dataframe(openness_df, hide_index=True)

    with col2:
        st.bar_chart(openness_df, x = 'Dimension', y = 'Percentile', horizontal=True)

    st.markdown('''<div style='text-align: justify;'>
    Openness is the primary dimension of creativity, artistic interest and intelligence, particularly verbal. Openness is
    a measure of interest in novelty, art, literature, abstract thinking, philosophy as well as sensitivity to aesthetic
    emotions and beauty. The two aspects of openness are intellect and aesthetics.
    </div>''', unsafe_allow_html=True)
    ''
    st.divider()


#########################################
##              CONTACT TAB            ##
#########################################
with tab_contact:
    st.markdown('''<div style='text-align: justify;'>
    I'll be happy to answer any questions you may have, so please feel free to use the information below should you wish to contact me.
    </div>''', unsafe_allow_html=True)
    ''
    st.markdown('''<div style='text-align: justify;'>
    EMAIL: jimjoywork@live.com
    </div>''', unsafe_allow_html=True)
    ''
    st.markdown('''<div style='text-align: justify;'>
    PHONE: +44 7535 358 691
    </div>''', unsafe_allow_html=True)
    ''
    st.link_button('🔗 LinkedIn', 'http://www.linkedin.com/in/jj-james-joyce', type = 'primary')
    ''
    st.link_button('✉️ Get in touch', 'mailto:jimjoywork@live.com', type = 'primary')
