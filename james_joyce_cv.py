#!/usr/bin/env python
# coding: utf-8

import os
import streamlit as st
import pdf_viewer

# from st_files_connection import FilesConnection
import pandas as pd
import numpy as np
import base64

# import gcsfs
import requests
import json
from fractions import Fraction

st.set_page_config(page_title="James Joyce",
                   page_icon="🙋🏼‍♂️",
                   initial_sidebar_state="expanded",
                   layout = 'wide'
                   )

##########################################
##  GLOBAL PARAMETERS                   ##
##########################################

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

set_background(os.path.join(image_path,'base-background.jpg'))

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
tab_hello, tab_cv, tab_coverletter, tab_personality = st.tabs(["**HELLO!**",
                                                              "**CV**",
                                                              "**COVERING LETTER**",
                                                              "**PERSONALITY**"
                                                              ])

#########################################
##             HELLO! TAB              ##
#########################################
with tab_hello:
    st.markdown(" #### Hello!")
    st.markdown('''<div style="text-align: justify;">
    My name is James, welcome to my digital CV, thank you for taking the time to view my profile.
    It's now incumbent upon me to reduce the full scope and scale of my own Human experience down
    to a series of palatable bullet points that make me seem a desirable candidate. A seemingly
    daunting and bizarre endeavour as this is, its the game we find ourselves playing. I can assure
    you that I have tried my utmost to make sure your time isn't wasted!
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    Along the top are all the core elements of my profile for an application. All are available to download
    from the respective PDF viewer, so please feel free to do so should you require it.
    </div>''', unsafe_allow_html=True)
    ""
    # st.image('https://user-images.githubusercontent.com/74038190/241765440-80728820-e06b-4f96-9c9e-9df46f0cc0a5.gif',  use_column_width=True)
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
    whimsiscal nature of Bingo often prejudiced people as to the seriousness the role demanded; the most
    common follow-up question by far was "So do you call the numbers?". If by "calling the numbers" you mean:
    </div>''', unsafe_allow_html=True)
    ""
    #
    st.markdown("- 📝 Project Managing the £250k roll out of a second venue within an 8-week turnaround time.")
    st.markdown("- 📆 Managing and booking talent for over 100 slots each month.")
    st.markdown("- 💰 Monthly reconciliation of the Production department expenditure and budget.")
    st.markdown("- 🎪 Liaising with festivals and third parties on external events to ensure seemless delivery of shows.")
    st.markdown('''- 🎨 Graphic Design - creating digital assets for social channels / website as well as physical collateral
                in the form of food & drink menus, venue posters, promo flyers, venue artwork.''')
    st.markdown("- 👁 Designing and creating visual content to supplement the shows on PowerPoint and iMovie")
    st.markdown("- 🚙 Driving and delivering our external shows all over the country.")
    st.markdown("- 🌟 Dressing the venue for seasonal periods (Christmas, Halloween, Valentines Day etc.).")
    st.markdown("- 🛠 Making props for our shows to increase production value and enhance customer experience.")

    st.markdown('''<div style="text-align: justify;">
    Then yes, I "called the numbers"... Although it's a lot easier and more succinct to off the simple reply of "no" within the
    confines of idle chit-chat.
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
    and Field Maneuvres.
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown('''<div style="text-align: justify;">
    My main duties include:
    </div>''', unsafe_allow_html=True)
    ""
    st.markdown("- ⏲ Preparing bar for service - beer line clean, arrange bar displays, configure tills for staff to use.")
    st.markdown("- ✅ To brief and be responsible for all personel working on my bar.")
    st.markdown("- 🧮 Stock Management throughout the event.")
    st.markdown("- 👮‍♂️ Managing and enforcing the legalities of bar operation under my own Personal Alcohol License.")
    st.markdown("- 🛠 Technical maintenance of the bar (changing kegs & gas cylinders, quality control of beer pours).")

    st.markdown(" ##### Future")
    st.markdown('''<div style="text-align: justify;">
    XXX
    </div>''', unsafe_allow_html=True)
    ""


#########################################
##               CV TAB                ##
#########################################
with tab_cv:

    # def displayPDF(file):
    # # Opening file from file path
    #     with open(file, "rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # # Embedding PDF in HTML
    #     pdf_display = F'''<iframe src="data:application/pdf;base64,{base64_pdf}"
    #     width="700" height="1000" type="application/pdf"></iframe>'''

    # # Displaying File
    #     st.markdown(pdf_display, unsafe_allow_html=True)

    # displayPDF(os.path.join(downloadfile_path, 'James_Joyce_CV_24.pdf'))

  pdf_viewer(os.path.join(downloadfile_path, 'James_Joyce_CV_24.pdf'), render_text=True)


#########################################
## COVERING LETTER TAB                 ##
#########################################
with tab_coverletter:

    def displayPDF(file):
    # Opening file from file path
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
        pdf_display = F'''<iframe src="data:application/pdf;base64,{base64_pdf}"
        width="700" height="1000" type="application/pdf"></iframe>'''

    # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    displayPDF(os.path.join(downloadfile_path, 'James_Joyce_Cover_Letter_24.pdf'))


#########################################
## PERSONALITY TAB                     ##
#########################################
with tab_personality:
    st.markdown("XXX")
