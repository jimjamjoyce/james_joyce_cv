import os
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import base64
import requests
import json

st.set_page_config(page_title="Design Portfolio",
                   page_icon="🎨",
                   initial_sidebar_state="expanded",
                   layout = 'centered'
                   )

##########################################
##  GLOBAL PARAMETERS                   ##
##########################################

#### FILE PATH CREATION ####
image_path = os.path.join(os.getcwd(), 'media')
downloadfile_path = os.path.join(os.getcwd(), 'download_files')
css_path = os.path.join(os.getcwd(), 'styles')
css_file = os.path.join(css_path, 'main.css')
graphic_path = os.path.join(image_path, 'graphic')
dabbers_path = os.path.join(graphic_path, 'dabbers')
di_path = os.path.join(graphic_path, 'diamond_island')
eurostars_path = os.path.join(graphic_path, 'eurostars')
las_fabulous_path = os.path.join(graphic_path, 'las_fabulous')
shot_wed_path = os.path.join(graphic_path, 'shotgun_wedding')


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

set_background(os.path.join(image_path,'changing-pastel3.gif'))

# # Expander Styling
st.markdown("""<style>.streamlit-expanderHeader {
 #   font-weight: bold;
    background: aliceblue;
    font-size: 18px;
}
</style>
""",
    unsafe_allow_html=True,
)
st.image(os.path.join(image_path, 'JAMES-JOYCE-title.png'), use_column_width = True)
st.write('''##### <span style="color:white"><div style="text-align: center;">DESIGN PORTFOLIO
            ''', unsafe_allow_html=True)
tab_graphic, tab_physical, = st.tabs(["**GRAPHIC DESIGN**",
                                     "**PROP & SET DESIGN**",
                                     ])
st.markdown('''<div style="text-align: justify;">
Ooh, Fancy seeing you here!
</div>''', unsafe_allow_html=True)
""
st.markdown('''<div style="text-align: justify;">
This is my Portfolio section where I've selected a portion of my design work that I've both enjoyed most
and am most proud of. I've had the pleasure of creating posters, menus, flyers, corporate decks,
venue artwork, digital assets, and graphics for props, to name a few.
</div>''', unsafe_allow_html=True)
""
st.markdown('''<div style="text-align: justify;">
Unfortunately however, this section of my profile is still under construction - I was hoping to utilise all manner of
digital display techniques and push Streamlit to its abosolute limit to showcase my portfolio. I'm talking carousels,
interactive images, widget, you name it, so watch this space 👀.
</div>''', unsafe_allow_html=True)
""
st.markdown('''<div style="text-align: justify;">
Alas, all is not lost. Instead I'll provide you with my portfoliio in its entirety through the medium of the 'Export' button below
that will download a .zip file with my most notable work.
</div>''', unsafe_allow_html=True)
""
st.markdown('''<div style="text-align: justify;">
I have essnetially grouped everything together by project in respective folders. The 'dabbers' folder contains a whole host of
various works from the past 3 years.
</div>''', unsafe_allow_html=True)
""
st.markdown('''<div style="text-align: justify;">
If you have any questions about any of the work, please feel free to get in contact; my information can be found in the "Contact"
tab on my CV Page.
</div>''', unsafe_allow_html=True)
""
st.markdown('''<div style="text-align: justify;">
Happy perusing!
</div>''', unsafe_allow_html=True)
""
""
col1, col2, col3 = st.columns([1,1,1])
with col1:
  design_portfolio = os.path.join(downloadfile_path, 'JAMES_JOYCE_Design_Portfolio.zip')
  with open(design_portfolio, "rb") as fp:
      btn = st.download_button(
          label="Export Portfolio PNGs",
          data=fp,
          file_name="JAMES_JOYCE_Portfolio_pngs.zip",
          mime="application/zip"
      )
with col2:
  portfolio_pdf = os.path.join(downloadfile_path, 'portfolio_pdfs.zip')
  with open(portfolio_pdf, "rb") as fp:
      btn = st.download_button(
          label="Export Portfolio PDFs",
          data=fp,
          file_name="JAMES_JOYCE_Portfolio_pdfs.zip",
          mime="application/zip"
      )
