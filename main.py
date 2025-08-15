# Necessary imports
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configures the default settings of the page
st.set_page_config(page_title="Statistics Dashboard", page_icon="more_power_logo.png", layout="wide")

# Power Plant image
power_plant_image = Image.open('power-plant-logo.png')
buffered_2 = BytesIO()
power_plant_image.save(buffered_2, format="PNG")
power_plant_img_str = base64.b64encode(buffered_2.getvalue()).decode()

# Electric Meter Image
image = Image.open('meter-logo.png')
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Sales image
sales_image = Image.open('sales-logo.png')
buffered_3 = BytesIO()
sales_image.save(buffered_3, format="PNG")
sales_img_str = base64.b64encode(buffered_3.getvalue()).decode()

# System Loss image
systemloss_image = Image.open('systemloss-logo.png')
buffered_4 = BytesIO()
systemloss_image.save(buffered_4, format="PNG")
systemloss_img_str = base64.b64encode(buffered_4.getvalue()).decode()

# Arrow image
arrow_image = Image.open('arrow-icon.png')
buffered_5 = BytesIO()
arrow_image.save(buffered_5, format="PNG")
arrow_img_str = base64.b64encode(buffered_5.getvalue()).decode()

# Column titles
first_column_title = "Energy Offtake"
second_column_title = "DU Metering"
third_column_title = "Sales"
third_column_title_2 = "System Loss"

hide_streamlit_style = """
           <style>
           header {visibility: hidden;}
           footer {visibility: hidden;}
           </style>
           """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
    <style>
        .main {
            padding: 0px;  /* Removes default padding */
        }
        .block-container {
            padding-top: 0px; 
            padding-bottom: 0px;
        }
    </style>
""", unsafe_allow_html=True)

# Set custom CSS to change the background color of the dashboard
st. markdown("""
    <style>
        .stApp {
            background-color: #81A263;   
        }
    </style>
    """, unsafe_allow_html=True)

# Adds a logo with text to the sidebar, maintaining aspect ratio
def add_logo_with_text(logo_path, text, max_width=None, max_height=None, text_size=16, font_family="Arial"):
    try:
        logo = Image.open(logo_path)
        original_width, original_height = logo.size

        if max_width and max_height:
            width_ratio = max_width / original_width
            height_ratio = max_height / original_height
            scale_factor = min(width_ratio, height_ratio)
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)
            logo = logo.resize((new_width, new_height), Image.LANCZOS)
        elif max_width:
            new_height = int(original_height * (max_width / original_width))
            logo = logo.resize((max_width, new_height), Image.LANCZOS)
        elif max_height:
            new_width = int(original_width * (max_height / original_height))
            logo = logo.resize((new_width, max_height), Image.LANCZOS)

        # Center the logo and text within the sidebar with a custom font
        sidebar_content = f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{get_base64_from_image(logo)}" style="max-width: 100%; max-height: {max_height if max_height else 'auto'}px;" />
            <p style="font-size: {text_size}px; margin-top: 10px; font-family: {font_family};">{text}</p>
        </div>
        """

        st.sidebar.markdown(sidebar_content, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error(f"Logo not found at {logo_path}")
    except Exception as e:
        st.error(f"Error displaying logo or text: {e}")

# Converts image to base64 for embedding in HTML
def get_base64_from_image(image):
    import base64
    from io import BytesIO

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

add_logo_with_text("more_power_logo.png", "Statistics Dashboard", max_width=150, text_size=20, font_family="Helvetica")

tabs = st.sidebar.radio("For the month of", ["January 2024", "February 2024", "March 2024", "April 2024", "May 2024", "June 2024", "July 2024", "August 2024", "September 2024", "October 2024", "November 2024", "December 2024", "January 2025", "February 2025", "March 2025", "April 2025", "May 2025",  "June 2025", "July 2025", "August 2025"], index=0)

# January 2024
if tabs == "January 2024":    
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">63,108,547 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-cc-jan {
            background-color: #8861A8; /* Example color */
            color: white; /* Text color */
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%; /* Matching width with the parent */
            height: 11.08%; /* Use percentage to fit based on parent height */
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            margin: 0;  /* Remove margin */
            box-sizing: border-box;  /* Ensure padding and border are included in element size */
            position: relative;  /* Allows child to be positioned relative to this */
            z-index: 10;  /* Ensure it is on top of other elements */
            pointer-events: auto;  /* Ensure interaction is enabled */
            font-size: 85%;
        }
        .vertical-rectangle-cc-jan:hover .tooltip-jan {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 357.20px;
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            padding-bottom: -30px;
        }
        .tooltip-jan {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-jan2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 50.88%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jan2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.89%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jan2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 27.23%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-kspc-jan {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 17.82%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-jan {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 29.52%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-jan {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.83%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-jan {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 26.75%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-residential-jan {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 38.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-jan {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-jan {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.24%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 65%;
        }
        .vertical-rectangle-power-jan {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 43.65%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-jan {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.45%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 75%;
        }
        .vertical-rectangle-othergovernment-jan {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.02%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-jan {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.75%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 55%;
        }
        .vertical-rectangle-stss-jan {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 70%;  
        }
        .vertical-rectangle-eou-jan {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 70%;  
        }
        .vertical-rectangle-feeder-jan {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 5.93%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 5;
            font-size: 60%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .net-metering-jan {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-jan"> 
                    Contestables (6,992,365)
                    <button class="mini-button">11.08%</button>
                <div class="tooltip-jan">
                    <div class="arrow"></div>SM Delgado - 464,921<br>SM City - 2,381,612<br>Golden Portals -  634,825<br>QHP -  395,239<br>Mary Mart -  275,059<br>HEVA -  414,681<br>Marriott -  419,552<br>Festive Walk Mall -  655,735<br>Smart Communications -  326,431<br>HEVA ICC -  125,321<br>KAREILA -  214,966<br>One Fintech -  298,937<br>Seda Hotel -  119,976<br>Innove Communications -  179,489<br>Adauge (The Shops) -  85,622
                </div>
            </div>
            <div class="vertical-rectangle-scpc-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SCPC (16,882,500)
                <button class="mini-button">26.75%</button>
            </div>
            <div class="vertical-rectangle-kspc-jan" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                KSPC (11,245,000)
                <button class="mini-button">17.82%</button>
            </div>
            <div class="vertical-rectangle-edc-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                EDC (9,360,000)
                <button class="mini-button">14.83%</button>
            </div>
            <div class="vertical-rectangle-wesm-jan" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                WESM (18,628,682)
                <button class="mini-button">29.52%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">63,108,547 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-jan2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (32,109,152)
                <button class="mini-button">50.88%</button>
            </div>
            <div class="vertical-rectangle-jan2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,817,384)
                <button class="mini-button">21.89%</button>
            </div>
            <div class="vertical-rectangle-jan2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,182,011)
                <button class="mini-button">27.23%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-jan" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (133,622)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">59,119,620 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jan" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (22,612,876)
                        <button class="mini-button">38.25%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (4,370,276)
                        <button class="mini-button-2">7.39%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-jan" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (143,182)
                        <button class="mini-button-2">0.24%</button>
                    </div>
                    <div class="vertical-rectangle-power-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (25,804,037)
                        <button class="mini-button">43.65%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-jan" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (859,156)
                        <button class="mini-button-2">1.45%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-jan" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (600,334)
                        <button class="mini-button-2">1.02%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jan" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (446,277)
                        <button class="mini-button-2">0.75%</button>
                    </div>
                    <div class="vertical-rectangle-eou-jan" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        EOU (19,262)
                        <button class="mini-button-2">0.03%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-jan" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (3,505,359)
                        <button class="mini-button-2">5.93%</button>
                    </div>
                    <div class="vertical-rectangle-stss-jan" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (758,861)
                        <button class="mini-button-2">1.28%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -140px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -355px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

# February 2024
elif tabs == "February 2024": 
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])
    
    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">58,981,068 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        .net-metering-feb {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
                font-size: 12px; /* Make the text small */
                padding: 2px 5 px; /* Adjust padding for a smaller button */
                background-color: white; /* Green background */
                color: black; /* White text color */
                border: none; /* Remove border */
                border-radius: 5px; /* Slightly rounded corners */
                cursor: pointer; /* Change cursor to pointer on hover */
                margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-extra {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .vertical-rectangle-feb2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 50.93%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-feb2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.60%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-feb2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 27.47%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 381px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .vertical-rectangle-cc-feb:hover .tooltip-feb {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .tooltip-feb {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-kspc-feb {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 23.99%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-feb {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 19.15%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-feb {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.89%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-feb {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 30.16%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-feb {
            background-color: #8861A8;
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 10.81%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-feb {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 37.59%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-feb {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.51%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-feb {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-feb {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 45.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-feb {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.62%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 75%;
        }
        .vertical-rectangle-othergovernment-feb {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.02%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-feb {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.76%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-feb {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-stss-feb {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.37%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-feeder-feb {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.76%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-feb">
                        Contestables (6,373,843)
                        <button class="mini-button">10.81%</button>
                        <div class="tooltip-feb">
                            <div class="arrow"></div>SM Delgado - 412,418<br>SM City - 2,133,582<br>Golden Portals - 517,279<br>QHP - 373,970<br>Mary Mart - 242,663<br>HEVA - 372,596<br>Marriott - 283,046<br>Festive Walk Mall - 624,995<br>Smart Communications - 316,744<br>HEVA ICC - 116,031<br>KAREILA - 200,944<br>One Fintech - 410,240<br>Seda Hotel - 110,157<br>Innove Communications - 174,634<br>Adauge (The Shops) - 84,544
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-feb" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,790,400)
                        <button class="mini-button">30.16%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-feb" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,151,400)
                        <button class="mini-button">23.99%</button>
                    </div>
                    <div class="vertical-rectangle-edc-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,372,300)
                        <button class="mini-button">15.89%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (11,293,125)
                        <button class="mini-button">19.15%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">58,981,068 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-feb2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (30,039,371)
                <button class="mini-button">50.93%</button>
            </div>
            <div class="vertical-rectangle-feb2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (12,737,984)
                <button class="mini-button">21.60%</button>
            </div>
            <div class="vertical-rectangle-feb2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,203,712)
                <button class="mini-button">27.47%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-feb" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (138,552)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 222px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">59,600,352 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (22,402,208)
                        <button class="mini-button">37.59%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-feb" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,474,132)
                        <button class="mini-button-2">7.51%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-feb" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (148,940)
                        <button class="mini-button-2">0.25%</button>
                    </div>
                    <div class="vertical-rectangle-power-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (26,872,241)
                        <button class="mini-button">45.09%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (965,591)
                        <button class="mini-button-2">1.62%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (607,960)
                        <button class="mini-button-2">1.02%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (452,367)
                        <button class="mini-button-2">0.76%</button>
                    </div>
                    <div class="vertical-rectangle-eou-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (18,227)
                        <button class="mini-button-2">0.03%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,839,645)
                        <button class="mini-button-2">4.76%</button>
                    </div>
                    <div class="vertical-rectangle-stss-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (819,041)
                        <button class="mini-button-2">1.37%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -150px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -380px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# March 2024
elif tabs == "March 2024": 
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">59,434,800 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .net-metering-mar {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .vertical-rectangle-mar2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 51.01%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-mar2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.91%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-mar2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 27.08%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-mar {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-mar:hover .tooltip-mar {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  
            height: 362px; 
            background-color: white; 
            border: 1px solid transparent; 
            margin-bottom: 100px;
        }
        .vertical-rectangle-kspc-mar {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 22.77%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-mar {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 19.74%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-mar {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 16.12%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-mar {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 29.78%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-mar {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.59%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-mar {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 41.85%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-mar {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.85%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-intermediate-mar {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-power-mar {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 44.69%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-mar {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.63%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-othergovernment-mar {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.08%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-citystreetlights-mar {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.68%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 50%;
        }
        .vertical-rectangle-eou-mar {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 60%;
        }
        .vertical-rectangle-stss-mar {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 60%;
        }
        .vertical-rectangle-feeder-mar {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.58%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (6,886,562)
                        <button class="mini-button">11.59%</button>
                        <div class="tooltip-mar">
                            <div class="arrow"></div>SM Delgado - 419,025<br>SM City - 2,133,598<br>Golden Portals - 682,832<br>QHP - 377,284<br>Mary Mart - 237,082<br>HEVA - 401,585<br>Marriott - 448,332<br>Festive Walk Mall - 634,036<br>Smart Communications - 333,804<br>HEVA ICC - 132,857<br>KAREILA - 208,988<br>One Fintech - 288,040<br>Seda Hotel - 114,442<br>Innove Communications - 185,419<br>Adauge (The Shops) - 102,167<br>Sunnyfield - 187,073
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-mar" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,535,500)
                        <button class="mini-button">22.77%</button>
                    </div>
                    <div class="vertical-rectangle-edc-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,579,400)
                        <button class="mini-button">16.12%</button>
                    </div>
                    <div class="vertical-rectangle-scpc-mar" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,698,200)
                        <button class="mini-button">29.78%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (11,735,138)
                        <button class="mini-button">19.74%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">59,434,800 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-mar2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (30,315,442)
                <button class="mini-button">51.01%</button>
            </div>
            <div class="vertical-rectangle-mar2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,023,080)
                <button class="mini-button">21.91%</button>
            </div>
            <div class="vertical-rectangle-mar2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,096,277)
                <button class="mini-button">27.08%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-mar" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (165,551)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 220px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">60,703,159 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (25,402,152)
                        <button class="mini-button">41.85%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-mar" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,763,443)
                        <button class="mini-button-2">7.85%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-mar" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (166,078)
                        <button class="mini-button-2">0.27%</button>
                    </div>
                    <div class="vertical-rectangle-power-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (27,125,240)
                        <button class="mini-button">44.69%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (986,917)
                        <button class="mini-button-2">1.63%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (653,259)
                        <button class="mini-button-2">1.08%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (414,691)
                        <button class="mini-button-2">0.68%</button>
                    </div>
                    <div class="vertical-rectangle-eou-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (20,931)
                        <button class="mini-button-2">0.03%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (354,998)
                        <button class="mini-button-2">0.58%</button>
                    </div>
                    <div class="vertical-rectangle-stss-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (815,450)
                        <button class="mini-button-2">1.34%</button>
                    </div>
                <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -140px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -361px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
             """,
            unsafe_allow_html=True
        )

# April 2024
elif tabs == "April 2024": 
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">60,492,498 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .net-metering-apr {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-apr2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.38%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-apr2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.39%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-apr2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.23%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-apr {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-apr:hover .tooltip-apr {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 410px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-apr {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.43%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-apr {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.56%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-apr {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-apr {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 27.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-apr {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 10.75%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-apr {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 42.21%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-apr {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.44%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-apr {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-apr {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 41.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-apr {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.29%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-apr {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.99%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-apr {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.63%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-apr {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-stss-apr {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.49%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-feeder-apr {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.63%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (6,505,632)
                        <button class="mini-button">10.75%</button>
                        <div class="tooltip-apr">
                            <div class="arrow"></div>SM Delgado - 404,103<br>SM City - 2,050,316<br>Golden Portals - 611,192<br>QHP - 360,829<br>Mary Mart - 224,742<br>HEVA - 362,058<br>Marriott - 396,130<br>Festive Walk Mall - 594,367<br>Smart Communications - 314,155<br>HEVA ICC - 110,785<br>KAREILA - 210,198<br>One Fintech - 289,569<br>Seda Hotel - 107,910<br>Innove Communications - 175,184<br>Adauge (The Shops) - 106,909<br>Sunnyfield - 187,186
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-apr" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (12,962,200)
                        <button class="mini-button">21.43%</button>
                    </div>
                    <div class="vertical-rectangle-edc-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,022,100)
                        <button class="mini-button">14.91%</button>
                    </div>
                    <div class="vertical-rectangle-scpc-apr" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (16,540,600)
                        <button class="mini-button">27.34%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (15,461,966)
                        <button class="mini-button">25.56%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">60,492,497 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-apr2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (32,290,271)
                <button class="mini-button">53.38%</button>
            </div>
            <div class="vertical-rectangle-apr2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (12,939,584)
                <button class="mini-button">21.39%</button>
            </div>
            <div class="vertical-rectangle-apr2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (15,262,642)
                <button class="mini-button">25.23%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-apr" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (210,662)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 248px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">71,649,692 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (30,242,166)
                        <button class="mini-button">42.21%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-apr" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,330,890)
                        <button class="mini-button-2">7.44%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-apr" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (192,821)
                        <button class="mini-button-2">0.27%</button>
                    </div>
                    <div class="vertical-rectangle-power-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (29,397,040)
                        <button class="mini-button">41.03%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (924,248)
                        <button class="mini-button-2">1.29%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (710,324)
                        <button class="mini-button-2">0.99%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (448,175)
                        <button class="mini-button-2">0.63%</button>
                    </div>
                    <div class="vertical-rectangle-eou-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (21,309)
                        <button class="mini-button-2">0.03%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,316,900)
                        <button class="mini-button-2">4.63%</button>
                    </div>
                    <div class="vertical-rectangle-stss-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (1,065,819)
                        <button class="mini-button-2">1.49%</button>
                    </div>
                <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -163px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -410px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# May 2024
elif tabs == "May 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">71,453,962 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .net-metering-may {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-may2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 55.23%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-may2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 19.23%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-may2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.54%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-may {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-may:hover .tooltip-may {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 407px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-may {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 19.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-may {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 31.21%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-may {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 13.57%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-may {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.16%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-may {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 10.15%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-may {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 41.86%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-may {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-may {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-may {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 40.50%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-may {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.33%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-may {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.05%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-may {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.57%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-may {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.16%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-may {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.11%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-may {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 5.81%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,254,088)
                        <button class="mini-button">10.15%</button>
                        <div class="tooltip-may">
                            <div class="arrow"></div>SM Delgado - 451,882<br>SM City - 2,166,781<br>Golden Portals - 595,754<br>QHP - 404,974<br>Mary Mart - 248,199<br>HEVA - 363,478<br>Marriott - 440,699<br>Festive Walk Mall - 660,892<br>Smart Communications - 337,731<br>HEVA ICC - 113,843<br>KAREILA - 220,966<br>One Fintech - 358,314<br>Seda Hotel - 119,053<br>Innove Communications - 191,918<br>Adauge (The Shops) - 116,183<br>Sunnyfield - 218,283<br>Two Fintech - 245,138
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-may" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,230,000)
                        <button class="mini-button">19.91%</button>
                    </div>
                    <div class="vertical-rectangle-edc-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,695,000)
                        <button class="mini-button">13.57%</button>
                    </div>
                    <div class="vertical-rectangle-scpc-may" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,975,000)
                        <button class="mini-button">25.16%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (22,299,874)
                        <button class="mini-button">31.21%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:
    # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">71,453,961 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-may2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (39,465,072)
                <button class="mini-button">55.23%</button>
            </div>
            <div class="vertical-rectangle-may2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,741,924)
                <button class="mini-button">19.23%</button>
            </div>
            <div class="vertical-rectangle-may2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (18,246,965)
                <button class="mini-button">25.54%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-may" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (195,731)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 245px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">76,788,209 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (32,143,692)
                        <button class="mini-button">41.86%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-may" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,635,237)
                        <button class="mini-button-2">7.34%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-may" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (208,063)
                        <button class="mini-button-2">0.27%</button>
                    </div>
                    <div class="vertical-rectangle-power-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (31,103,059)
                        <button class="mini-button">40.50%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,021,343)
                        <button class="mini-button-2">1.33%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (806,996)
                        <button class="mini-button-2">1.05%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (434,690)
                        <button class="mini-button-2">0.57%</button>
                    </div>
                    <div class="vertical-rectangle-eou-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (121,974)
                        <button class="mini-button-2">0.16%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (4,458,153)
                        <button class="mini-button-2">5.81%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (855,002)
                        <button class="mini-button-2">1.11%</button>
                    </div>
                <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -165px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -405px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# June 2024
elif tabs == "June 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">76,626,701 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .tooltip-jun {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .net-metering-jun {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-cc-jun:hover .tooltip-jun {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 345px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-jun2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.90%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jun2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 20.21%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jun2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.89%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-kspc-jun {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 18.53%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-jun {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 35.38%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-jun {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 12.65%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-jun {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 23.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-jun {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 10.18%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-jun {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 40.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-jun {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.36%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-jun {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-jun {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 43.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-jun {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-othergovernment-jun {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-citystreetlights-jun {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.64%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-jun {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.06%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-stss-jun {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.01%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-feeder-jun {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.98%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,800,150)
                        <button class="mini-button">10.18%</button>
                        <div class="tooltip-jun">
                            <div class="arrow"></div>SM Delgado - 498,748<br>SM City - 2,354,727<br>Golden Portals - 551,244<br>QHP - 425,955<br>Mary Mart - 278,924<br>HEVA - 394,472<br>Marriott - 469,620<br>Festive Walk Mall - 718,441<br>Smart Communications - 327,853<br>HEVA ICC - 126,367<br>KAREILA - 225,506<br>One Fintech - 392,809<br>Seda Hotel - 121,354<br>Innove Communications - 188,774<br>Adauge (The Shops) - 121,735<br>Sunnyfield - 224,792<br>Two Fintech - 378,828
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-jun" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,825,000)
                        <button class="mini-button">23.26%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-jun" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,200,000)
                        <button class="mini-button">18.53%</button>
                    </div>
                    <div class="vertical-rectangle-edc-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,692,000)
                        <button class="mini-button">12.65%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (27,109,551)
                        <button class="mini-button">35.38%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">76,626,701 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-jun2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (41,305,036)
                <button class="mini-button">53.90%</button>
            </div>
            <div class="vertical-rectangle-jun2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (15,483,608)
                <button class="mini-button">20.21%</button>
            </div>
            <div class="vertical-rectangle-jun2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (19,838,057)
                <button class="mini-button">25.89%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-jun" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (161,508)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 193px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">68,196,439 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (27,326,241)
                        <button class="mini-button">40.07%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-jun" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,017,783)
                        <button class="mini-button-2">7.36%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-jun" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (182,714)
                        <button class="mini-button-2">0.27%</button>
                    </div>
                    <div class="vertical-rectangle-power-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (29,492,327)
                        <button class="mini-button">43.25%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (875,200)
                        <button class="mini-button-2">1.28%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (732,954)
                        <button class="mini-button-2">1.07%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (434,829)
                        <button class="mini-button-2">0.64%</button>
                    </div>
                    <div class="vertical-rectangle-eou-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (43,692)
                        <button class="mini-button-2">0.06%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,398,984)
                        <button class="mini-button-2">4.98%</button>
                    </div>
                    <div class="vertical-rectangle-stss-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (691,715)
                        <button class="mini-button-2">1.01%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -130px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -345px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# July 2024
elif tabs == "July 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">68,054,095 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .vertical-rectangle-jul2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .net-metering-jul {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .vertical-rectangle-jul2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 20.72%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jul2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.94%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-jul {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-jul:hover .tooltip-jul {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 348px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-jul {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.31%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-jul {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 26.46%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-jul {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.22%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-jul {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 26.63%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-jul {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.38%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-jul {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 40.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-jul {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.66%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-jul {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-jul {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 44.54%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-jul {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.31%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-jul {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-jul {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.65%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-jul {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-stss-jul {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.88%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-feeder-jul {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 3.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,742,896)
                        <button class="mini-button">11.38%</button>
                        <div class="tooltip-jul">
                            <div class="arrow"></div>SM Delgado - 487,208<br>SM City - 2,402,620<br>Golden Portals - 566,921<br>QHP - 435,601<br>Mary Mart - 283,328<br>HEVA - 404,338<br>Marriott - 438,771<br>Festive Walk Mall - 692,681<br>Smart Communications - 324,408<br>HEVA ICC - 181,363<br>KAREILA - 230,556<br>One Fintech - 339,034<br>Seda Hotel - 117,790<br>Innove Communications - 189,532<br>Adauge (The Shops) - 112,040<br>Sunnyfield - 203,348<br>Two Fintech - 333,356
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-jul" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (18,125,000)
                        <button class="mini-button">26.63%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-jul" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,500,000)
                        <button class="mini-button">21.31%</button>
                    </div>
                    <div class="vertical-rectangle-edc-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,678,000)
                        <button class="mini-button">14.22%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (18,008,199)
                        <button class="mini-button">26.46%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:  
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">68,054,094 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-jul2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (36,302,166)
                <button class="mini-button">53.34%</button>
            </div>
            <div class="vertical-rectangle-jul2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,100,097)
                <button class="mini-button">20.72%</button>
            </div>
            <div class="vertical-rectangle-jul2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,651,831)
                <button class="mini-button">25.94%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-jul" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (142,344)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">63,850,921 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (25,719,097)
                        <button class="mini-button">40.28%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-jul" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,892,858)
                        <button class="mini-button-2">7.66%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-jul" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (168,171)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (28,442,028)
                        <button class="mini-button">44.54%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (836,197)
                        <button class="mini-button-2">1.31%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (680,647)
                        <button class="mini-button-2">1.07%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (412,060)
                        <button class="mini-button-2">0.65%</button>
                    </div>
                    <div class="vertical-rectangle-eou-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (43,981)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,092,143)
                        <button class="mini-button-2">3.28%</button>
                    </div>
                    <div class="vertical-rectangle-stss-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (563,739)
                        <button class="mini-button-2">0.88%</button>
                    </div>
                <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -139px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -343px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# August 2024
elif tabs == "August 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">63,708,922 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .net-metering-aug {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .vertical-rectangle-aug2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.60%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-aug2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 20.68%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-aug2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.73%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-aug {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-aug:hover .tooltip-aug {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 404px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-aug {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.96%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-aug {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 23.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-aug {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.70%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-aug {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 27.45%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-aug {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.80%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-aug {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 39.88%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-aug {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-aug {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-aug {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 42.60%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-aug {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.56%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-aug {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.23%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-aug {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.62%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-aug {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-aug {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 2.63%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-feeder-aug {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 3.89%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,519,190)
                        <button class="mini-button">11.80%</button>
                        <div class="tooltip-aug">
                            <div class="arrow"></div>SM Delgado - 462,079<br>SM City - 2,353,111<br>Golden Portals - 521,017<br>QHP - 403,050<br>Mary Mart - 269,805<br>HEVA - 401,757<br>Marriott - 430,391<br>Festive Walk Mall - 731,992<br>Smart Communications - 324,970<br>HEVA ICC - 156,644<br>KAREILA - 222,950<br>One Fintech - 326,749<br>Seda Hotel - 105,723<br>Innove Communications - 184,324<br>Adauge (The Shops) - 109,197<br>Sunnyfield - 194,022<br>Two Fintech - 321,409
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-aug" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,487,500)
                        <button class="mini-button">27.45%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-aug" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,990,000)
                        <button class="mini-button">21.96%</button>
                    </div>
                    <div class="vertical-rectangle-edc-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (10,002,500)
                        <button class="mini-button">15.70%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (14,709,732)
                        <button class="mini-button">23.09%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">63,708,922 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-aug2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (34,147,315)
                <button class="mini-button">53.60%</button>
            </div>
            <div class="vertical-rectangle-aug2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,171,900)
                <button class="mini-button">20.68%</button>
            </div>
            <div class="vertical-rectangle-aug2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,389,707)
                <button class="mini-button">25.73%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-aug" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (141,998)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 240px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )
        
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">69,458,394 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (27,699,354)
                        <button class="mini-button">39.88%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-aug" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,041,468)
                        <button class="mini-button-2">7.26%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-aug" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (182,203)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (29,592,103)
                        <button class="mini-button">42.60%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,084,803)
                        <button class="mini-button-2">1.56%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (854,535)
                        <button class="mini-button-2">1.23%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (430,198)
                        <button class="mini-button-2">0.62%</button>
                    </div>
                    <div class="vertical-rectangle-eou-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (46,523)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,701,268)
                        <button class="mini-button-2">3.89%</button>
                    </div>
                    <div class="vertical-rectangle-stss-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (1,825,939)
                        <button class="mini-button-2">2.63%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -162px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -403px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# September 2024
elif tabs == "September 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">69,285,360 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .net-metering-sep {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .vertical-rectangle-sep2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-sep2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.04%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-sep2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.87%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-sep {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-sep:hover .tooltip-sep {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 360px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-sep {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 19.41%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-sep {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 30.17%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-sep {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 13.96%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-sep {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 24.93%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-sep {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.52%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-sep {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 39.05%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-sep {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.35%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-sep {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-sep {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 44.30%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-sep {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.54%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-sep {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.33%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-sep {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.80%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-sep {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-stss-sep {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.90%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-sep {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.40%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,981,778)
                        <button class="mini-button">11.52%</button>
                        <div class="tooltip-sep">
                            <div class="arrow"></div>SM Delgado - 499,415<br>SM City - 2,514,803<br>Golden Portals - 595,414<br>QHP - 417,255<br>Mary Mart - 283,283<br>HEVA - 412,157<br>Marriott - 418,028<br>Festive Walk Mall - 699,974<br>Smart Communications - 344,200<br>HEVA ICC - 139,041<br>KAREILA - 221,593<br>One Fintech - 347,894<br>Seda Hotel - 115,010<br>Innove Communications - 193,378<br>Adauge (The Shops) - 116,084<br>Sunnyfield - 217,471<br>Two Fintech - 346,897<br>Festive Walk 2 - 99,881
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-sep" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,275,000)
                        <button class="mini-button">24.93%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-sep" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,450,000)
                        <button class="mini-button">19.41%</button>
                    </div>
                    <div class="vertical-rectangle-edc-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,674,000)
                        <button class="mini-button">13.96%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (20,904,582)
                        <button class="mini-button">30.17%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">69,285,360 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-sep2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (36,781,635)
                <button class="mini-button">53.09%</button>
            </div>
            <div class="vertical-rectangle-sep2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,577,080)
                <button class="mini-button">21.04%</button>
            </div>
            <div class="vertical-rectangle-sep2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,926,645)
                <button class="mini-button">25.87%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-sep" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (173,035)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 205px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">66,163,711 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (25,836,637)
                        <button class="mini-button">39.05%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-sep" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,860,307)
                        <button class="mini-button-2">7.35%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-sep" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (171,989)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (29,312,602)
                        <button class="mini-button">44.30%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,020,489)
                        <button class="mini-button-2">1.54%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (881,758)
                        <button class="mini-button-2">1.33%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (526,798)
                        <button class="mini-button-2">0.80%</button>
                    </div>
                    <div class="vertical-rectangle-eou-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (44,179)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,912,053)
                        <button class="mini-button-2">4.40%</button>
                    </div>
                    <div class="vertical-rectangle-stss-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (596,899)
                        <button class="mini-button-2">0.90%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -145px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -355px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div> 
            """,
            unsafe_allow_html=True
        )

# October 2024
elif tabs == "October 2024":
    col1, col2, col3, col4, col5= st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">66,003,977 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .vertical-rectangle-oct2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .net-metering-oct {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .vertical-rectangle-oct2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 20.73%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-oct2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.60%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-oct {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-oct:hover .tooltip-oct {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 381px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-oct {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 20.15%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-oct {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 28.40%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-oct {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.66%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-oct {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 24.73%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-oct {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 12.06%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-oct {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 39.21%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-oct {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.35%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-oct {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-oct {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 43.92%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-oct {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-oct {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.37%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-oct {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.66%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-oct {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-oct {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.57%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-oct {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.94%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,958,002)
                        <button class="mini-button">12.06%</button>
                        <div class="tooltip-oct">
                            <div class="arrow"></div>SM Delgado - 495,935<br>SM City - 2,447,375<br>Golden Portals - 572,551<br>QHP - 409,942<br>Mary Mart - 278,523<br>HEVA - 407,636<br>Marriott - 393,030<br>Festive Walk Mall - 648,333<br>Smart Communications - 344,777<br>HEVA ICC - 141,546<br>KAREILA - 230,704<br>One Fintech - 344,818<br>Seda Hotel - 122,471<br>Innove Communications - 190,941<br>Adauge (The Shops) - 108,446<br>Sunnyfield - 212,502<br>Two Fintech - 337,632<br>Festive Walk 2 - 270,841
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-oct" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (16,325,000)
                        <button class="mini-button">24.73%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-oct" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,300,000)
                        <button class="mini-button">20.15%</button>
                    </div>
                    <div class="vertical-rectangle-edc-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,673,000)
                        <button class="mini-button">14.66%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (18,747,975)
                        <button class="mini-button">28.40%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">66,003,976 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-oct2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,423,892)
                <button class="mini-button">53.67%</button>
            </div>
            <div class="vertical-rectangle-oct2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,681,823)
                <button class="mini-button">20.73%</button>
            </div>
            <div class="vertical-rectangle-oct2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,898,261)
                <button class="mini-button">25.60%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-oct" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (159,735)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )

        with col4:
            st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
                <img src="data:image/png;base64,{arrow_img_str}" width="100%">
            </div>
            ''', 
            unsafe_allow_html=True
        )

            st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 220px; z-index:2;">
                <img src="data:image/png;base64,{arrow_img_str}" width="100%">
            </div>
            ''', 
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )
        
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">66,416,388 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (26,039,704)
                        <button class="mini-button">39.21%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-oct" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,880,754)
                        <button class="mini-button-2">7.35%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-oct" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (172,949)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (29,168,182)
                        <button class="mini-button">43.92%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,112,136)
                        <button class="mini-button-2">1.67%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (907,607)
                        <button class="mini-button-2">1.37%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (435,889)
                        <button class="mini-button-2">0.66%</button>
                    </div>
                    <div class="vertical-rectangle-eou-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (45,167)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,278,701)
                        <button class="mini-button-2">4.94%</button>
                    </div>
                    <div class="vertical-rectangle-stss-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (375,299)
                        <button class="mini-button-2">0.57%</button>
                    </div>
                <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -150px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -380px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# November 2024
elif tabs == "November 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">66,243,078 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .net-metering-nov {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-nov2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 53.16%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-nov2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.71%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-nov2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.13%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-nov {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-nov:hover .tooltip-nov {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 382px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-nov {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 18.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-nov {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 33.00%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-nov {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.13%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-nov {
            background-color: #cc3333; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 22.79%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-nov {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.81%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-nov {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 39.50%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-nov {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.47%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-nov {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-nov {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 43.14%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-nov {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.57%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-nov {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-nov {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.65%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-nov {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-nov {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.37%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-nov {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.61%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables (7,822,466)
                        <button class="mini-button">11.81%</button>
                        <div class="tooltip-nov">
                            <div class="arrow"></div>SM Delgado - 412,418<br>SM Delgado - 460,159<br>SM City - 2,370,681<br>Golden Portals - 583,385<br>QHP - 406,496<br>Mary Mart - 252,063<br>HEVA - 392,500<br>Marriott - 430,235<br>Festive Walk Mall - 651,642<br>Smart Communications - 340,873<br>HEVA ICC - 139,782<br>KAREILA - 221,555<br>One Fintech - 346,065<br>Seda Hotel - 122,340<br>Innove Communications - 183,604<br>Adauge (The Shops) - 108,707<br>Sunnyfield - 214,031<br>Two Fintech - 332,917<br>Festive Walk 2 - 265,430
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-nov" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (15,100,000)
                        <button class="mini-button">22.79%</button>
                    </div>
                    <div class="vertical-rectangle-kspc-nov" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (12,100,000)
                        <button class="mini-button">18.27%</button>
                    </div>
                    <div class="vertical-rectangle-edc-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,360,000)
                        <button class="mini-button">14.13%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (21,860,612)
                        <button class="mini-button">33.00%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">66,243,078 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-nov2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,213,673)
                <button class="mini-button">53.16%</button>
            </div>
            <div class="vertical-rectangle-nov2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,381,906)
                <button class="mini-button">21.71%</button>
            </div>
            <div class="vertical-rectangle-nov2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,647,499)
                <button class="mini-button">25.13%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-nov" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (173,309)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 225px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">67,391,969 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (26,621,291)
                        <button class="mini-button">39.50%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-nov" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,034,110)
                        <button class="mini-button-2">7.47%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-nov" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (174,857)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (29,076,012)
                        <button class="mini-button">43.14%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,060,257)
                        <button class="mini-button-2">1.57%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (902,769)
                        <button class="mini-button-2">1.34%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (439,117)
                        <button class="mini-button-2">0.65%</button>
                    </div>
                    <div class="vertical-rectangle-eou-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EOU (58,595)
                        <button class="mini-button-2">0.09%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,104,654)
                        <button class="mini-button-2">4.61%</button>
                    </div>
                    <div class="vertical-rectangle-stss-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS (920,307)
                        <button class="mini-button-2">1.37%</button>
                    </div>
                <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -150px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -381px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div>
                </div>
            </div> 
            """,
            unsafe_allow_html=True
        )

# December 2024
elif tabs == "December 2024":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">67,204,899 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .vertical-rectangle-dec2024-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 52.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .net-metering-dec {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-dec2024-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 21.70%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-dec2024-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.91%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-dec {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-dec:hover .tooltip-dec {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 367px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-dec {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 18.93%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-dec {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 46.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-dec {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-pedc-dec {
            background-color: #FFA500; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 8.62%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-cc-dec {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.81%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-dec {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 38.75%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-dec {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-dec {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-dec {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 44.49%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-dec {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.52%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-dec {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.34%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-dec {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.68%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-dec {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-dec {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.04%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-dec {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 4.52%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-dec" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Contestables (7,928,521)
                        <button class="mini-button">11.81%</button>
                        <div class="tooltip-dec">
                            <div class="arrow"></div>SM Delgado - 467,927<br>SM City - 2,395,474<br>Golden Portals - 597,285<br>QHP - 416,100<br>Mary Mart - 248,980<br>HEVA - 389,432<br>Marriott - 436,659<br>Festive Walk Mall - 667,290<br>Smart Communications - 350,653<br>HEVA ICC - 131,164<br>KAREILA - 225,575<br>One Fintech - 358,438<br>Seda Hotel - 119,322<br>Innove Communications - 190,648<br>Adauge (The Shops) - 109,907<br>Sunnyfield - 219,858<br>Two Fintech - 341,476<br>Festive Walk 2 - 262,334
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-dec" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (12,720,000)
                        <button class="mini-button">18.93%</button>
                    </div>
                    <div class="vertical-rectangle-edc-dec" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,674,000)
                        <button class="mini-button">14.39%</button>
                    </div>
                    <div class="vertical-rectangle-pedc-dec" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        PEDC (5,795,000)
                        <button class="mini-button">8.62%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-dec" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (31,087,378)
                        <button class="mini-button">46.26%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:  
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">67,204,899 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-dec2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,206,677)
                <button class="mini-button">52.39%</button>
            </div>
            <div class="vertical-rectangle-dec2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,584,192)
                <button class="mini-button">21.70%</button>
            </div>
            <div class="vertical-rectangle-dec2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,414,030)
                <button class="mini-button">25.91%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-dec" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (187,070)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 215px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">65,229,255 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-dec" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (25,273,704)
                        <button class="mini-button">38.75%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-dec" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (4,785,379)
                        <button class="mini-button-2">7.34%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-dec" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (162,601)
                        <button class="mini-button-2">0.25%</button>
                    </div>
                    <div class="vertical-rectangle-power-dec" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (29,023,526)
                        <button class="mini-button">44.49%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-dec" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (990,510)
                        <button class="mini-button-2">1.52%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-dec" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (873,958)
                        <button class="mini-button-2">1.34%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-dec" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (446,366)
                        <button class="mini-button-2">0.68%</button>
                    </div>
                    <div class="vertical-rectangle-eou-dec" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        EOU (47,727)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-dec" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (2,949,895)
                        <button class="mini-button-2">4.52%</button>
                    </div>
                    <div class="vertical-rectangle-stss-dec" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (675,589)
                        <button class="mini-button-2">1.04%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -149px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -362px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

elif tabs == "January 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">65,058,655 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 463.08px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .net-metering-jan2025 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jan2025-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 28.02%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jan2025-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.97%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-jan2025-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 57.01%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-jan2025 {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-cc-jan2025:hover .tooltip-jan2025 {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 365px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-jan2025 {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 17.29%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-jan2025 {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 48.40%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-jan2025 {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-pedc-jan2025 {
            background-color: #FFA500; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.74%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 75%;
        }
        .vertical-rectangle-cc-jan2025 {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 12.18%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-residential-jan2025 {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 39.80%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-jan2025 {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.47%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-jan2025 {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-jan2025 {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 43.11%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-jan2025 {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.46%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-jan2025 {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.29%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-jan2025 {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.72%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-jan2025 {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-stss-jan2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.56%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-jan2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 5.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-jan2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Contestables (7,922,998)
                         <button class="mini-button">12.18%</button>
                        <div class="tooltip-jan2025">
                            <div class="arrow"></div>SM Delgado - 467,062<br>SM City -  2,390,840<br>Golden Portals -  598,483<br>QHP - 412,327<br>Mary Mart -  299,040<br>HEVA -  371,143<br>Marriott -  430,726<br>Festive Walk Mall -  691,189<br>Smart Communications -  335,295<br>HEVA ICC -  143,161<br>KAREILA - 226,504<br>One Fintech - 338,900<br>Seda Hotel - 118,901<br>Innove Communications -  184,472<br>Adauge (The Shops) - 107,332<br>Sunnyfield - 215,340<br>Two Fintech -  331,058<br>Festive Walk 2 - 261,226
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-jan2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (11,250,000)
                        <button class="mini-button">17.29%</button>
                    </div>
                    <div class="vertical-rectangle-edc-jan2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,360,000)
                        <button class="mini-button">14.39%</button>
                    </div>
                    <div class="vertical-rectangle-pedc-jan2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        PEDC (5,035,000)
                        <button class="mini-button">7.74%</button>
                    </div>
                    <div class="vertical-rectangle-wesm-jan2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (31,490,657)
                        <button class="mini-button">48.40%</button>
                    </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">65,058,655 kWh</p>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-jan2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (18,226,411)
                <button class="mini-button">28.02%</button>
            </div>
            <div class="vertical-rectangle-jan2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (9,741,102)
                <button class="mini-button">14.97%</button>
            </div>
            <div class="vertical-rectangle-jan2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (37,091,142)
                <button class="mini-button">57.01%</button>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-jan2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (170,601)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 210px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">62,810,250 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jan2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (24,998,326)
                        <button class="mini-button">39.80%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-jan2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (4,694,133)
                        <button class="mini-button-2">7.47%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-jan2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (165,725)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-jan2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (27,076,440)
                        <button class="mini-button">43.11%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-jan2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (914,391)
                        <button class="mini-button-2">1.46%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-jan2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (810,819)
                        <button class="mini-button-2">1.29%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jan2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (450,518)
                        <button class="mini-button-2">0.72%</button>
                    </div>
                    <div class="vertical-rectangle-eou-jan2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        EOU (45,106)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-jan2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (3,304,777)
                        <button class="mini-button-2">5.26%</button>
                    </div>
                    <div class="vertical-rectangle-stss-jan2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (350,015)
                        <button class="mini-button-2">0.56%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -143px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -364px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

# February 2025
elif tabs == "February 2025":    
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">62,605,135 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .net-metering-feb2025 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 410px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-feb2025-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 56.54%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-feb2025-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.23%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-feb2025-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 28.24%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-kspc-feb2025 {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 16.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-feb2025 {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 50.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-feb2025 {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.45%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-pedc-feb2025 {
            background-color: #FFA500; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 6.08%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 75%;
        }
        .vertical-rectangle-cc-feb2025 {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 12.12%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-cc-feb2025:hover .tooltip-feb2025 {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .tooltip-feb2025 {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-residential-feb2025 {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 37.41%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-feb2025 {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.18%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-feb2025 {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-feb2025 {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 42.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-feb2025 {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.58%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-feb2025 {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-feb2025 {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.68%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-feb2025 {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.06%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-stss-feb2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.22%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-feb2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 8.56%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-feb2025"> 
                    Contestables (7,586,883)
                    <button class="mini-button">12.12%</button>
                <div class="tooltip-feb2025">
                    <div class="arrow">SM Delgado - 430,899<br>SM City - 2,281,597<br>Golden Portals - 514,124<br>QHP - 405,708<br>Mary Mart - 272,815<br>HEVA - 340,042<br>Marriott - 442,930<br>Festive Walk Mall - 686,451<br>Smart Communications - 335,489<br>HEVA ICC - 131,015<br>KAREILA - 212,838<br>One Fintech - 325,235<br>Seda Hotel - 115,367<br>Innove Communications - 188,836<br>Adauge (The Shops) - 105,976<br>Sunnyfield - 209,496<br>Two Fintech - 326,634<br>Festive Walk 2 - 261,432</div>
                </div>
            </div>
            <div class="vertical-rectangle-kspc-feb2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                KSPC (10,060,000)
                <button class="mini-button">16.07%</button>
            </div>
            <div class="vertical-rectangle-edc-feb2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                EDC (9,672,000)
                <button class="mini-button">15.45%</button>
            </div>
            <div class="vertical-rectangle-pedc-feb2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                PEDC (3,809,212)
                <button class="mini-button">6.08%</button>
            </div>
            <div class="vertical-rectangle-wesm-feb2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                WESM (31,477,040)
                <button class="mini-button">50.28%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )
        
    with col3:
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">62,605,135 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-feb2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,395,035)
                <button class="mini-button">56.54%</button>
            </div>
            <div class="vertical-rectangle-feb2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (9,533,300)
                <button class="mini-button">15.23%</button>
            </div>
            <div class="vertical-rectangle-feb2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,676,800)
                <button class="mini-button">28.24%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-feb2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (205,115)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
        
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 245px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">64,424,274 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-feb2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (24,100,555)
                        <button class="mini-button">37.41%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-feb2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (4,628,295)
                        <button class="mini-button-2">7.18%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-feb2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (158,944)
                        <button class="mini-button-2">0.25%</button>
                    </div>
                    <div class="vertical-rectangle-power-feb2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (27,489,760)
                        <button class="mini-button">42.67%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-feb2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (1,017,458)
                        <button class="mini-button-2">1.58%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-feb2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (895,762)
                        <button class="mini-button-2">1.39%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-feb2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (437,070)
                        <button class="mini-button-2">0.68%</button>
                    </div>
                    <div class="vertical-rectangle-eou-feb2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        EOU (38,798)
                        <button class="mini-button-2">0.06%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-feb2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (5,515,061)
                        <button class="mini-button-2">8.56%</button>
                    </div>
                    <div class="vertical-rectangle-stss-feb2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (142,571)
                        <button class="mini-button-2">0.22%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -165px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -410px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

# March 2025
elif tabs == "March 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">64,204,158 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 345px; Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-mar2025 {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 16.43%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-mar2025 {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 50.93%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-mar2025 {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.08%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-pedc-mar2025 {
            background-color: #FFA500; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 5.79%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 75%;
        }
        .vertical-rectangle-cc-mar2025 {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 11.76%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-cc-mar2025:hover .tooltip-mar2025 {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .tooltip-mar2025 {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-mar2025-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 55.30%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-mar2025-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 16.34%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-mar2025-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 28.36%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .net-metering-mar2025 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-residential-mar2025 {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 41.31%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-mar2025 {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-mar2025 {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-mar2025 {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 45.41%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-mar2025 {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-mar2025 {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.42%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-mar2025 {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-mar2025 {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-mar2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.86%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-mar2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-mar2025"> 
                    Contestables (7,553,298)
                    <button class="mini-button">11.76%</button>
                <div class="tooltip-mar2025">
                    <div class="arrow">SM Delgado - 431,311<br>SM City - 2,209,085<br>Golden Portals - 621,268<br>QHP - 399,976<br>Mary Mart - 271,505<br>HEVA - 325,528<br>Marriott - 458,338<br>Festive Walk Mall - 642,397<br>Smart Communications - 330,532<br>HEVA ICC - 124,204<br>KAREILA - 219,096<br>One Fintech - 322,511<br>Seda Hotel - 116,777<br>Innove Communications - 187,916<br>Adauge (The Shops) - 108,633<br>Sunnyfield - 216,327<br>Two Fintech - 312,917<br>Festive Walk 2 - 254,976</div>
                </div>
            </div>
            <div class="vertical-rectangle-kspc-mar2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                KSPC (10,550,000)
                <button class="mini-button">16.43%</button>
            </div>
            <div class="vertical-rectangle-edc-mar2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                EDC (9,684,000)
                <button class="mini-button">15.08%</button>
            </div>
            <div class="vertical-rectangle-pedc-mar2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                PEDC (3,717,553)
                <button class="mini-button">5.79%</button>
            </div>
            <div class="vertical-rectangle-wesm-mar2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                WESM (32,699,307)
                <button class="mini-button">50.93%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )
        
    with col3:
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">64,204,158 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-mar2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,504,746)
                <button class="mini-button">55.30%</button>
            </div>
            <div class="vertical-rectangle-mar2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (10,490,088)
                <button class="mini-button">16.34%</button>
            </div>
            <div class="vertical-rectangle-mar2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (18,209,324)
                <button class="mini-button">28.36%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-mar2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (220,115)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
        
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 210px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">60,299,624 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-mar2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (24,911,214)
                        <button class="mini-button">41.31%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-mar2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (4,771,171)
                        <button class="mini-button-2">7.91%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-mar2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (166,087)
                        <button class="mini-button-2">0.28%</button>
                    </div>
                    <div class="vertical-rectangle-power-mar2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (27,384,519)
                        <button class="mini-button">45.41%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-mar2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (1,009,547)
                        <button class="mini-button-2">1.67%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-mar2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (854,496)
                        <button class="mini-button-2">1.42%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-mar2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (402,736)
                        <button class="mini-button-2">0.67%</button>
                    </div>
                    <div class="vertical-rectangle-eou-mar2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        EOU (44,521)
                        <button class="mini-button-2">0.07%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-mar2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (236,695)
                        <button class="mini-button-2">0.39%</button>
                    </div>
                    <div class="vertical-rectangle-stss-mar2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (518,638)
                        <button class="mini-button-2">0.86%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -135px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; text-align: center; align-items: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -340px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

# April 2025
elif tabs == "April 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">60,056,730 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 410px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-apr2025 {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 17.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-apr2025 {
            background-color: #cc3333;
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.44%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-apr2025 {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 33.89%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-apr2025 {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 14.55%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-pedc-apr2025 {
            background-color: #FFA500; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 5.93%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 75%;
        }
        .vertical-rectangle-cc-apr2025 {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 13.16%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-cc-apr2025:hover .tooltip-apr2025 {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .tooltip-apr2025 {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-apr2025-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 55.44%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-apr2025-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 16.20%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-apr2025-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 28.36%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .net-metering-apr2025 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-residential-apr2025 {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 40.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-apr2025 {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.04%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-apr2025 {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-apr2025 {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 40.59%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-apr2025 {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.21%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-apr2025 {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.31%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-apr2025 {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.59%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-apr2025 {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.06%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-stss-apr2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.70%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-feeder-apr2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.99%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-apr2025"> 
                    Contestables (7,902,637)
                    <button class="mini-button">13.16%</button>
                <div class="tooltip-apr2025">
                    <div class="arrow">SM Delgado - 403,218<br>SM City - 1,997,124<br>Golden Portals - 553,032<br>QHP - 372,377<br>Mary Mart - 252,316<br>HEVA - 301,033<br>Marriott - 410,285<br>Festive Walk Mall - 598,134<br>Smart Communications - 301,842<br>HEVA ICC - 117,149<br>KAREILA - 190,737<br>One Fintech - 311,571<br>Seda Hotel - 104,990<br>Innove Communications - 171,515<br>Adauge (The Shops) - 97,553<br>Sunnyfield - 200,472<br>Two Fintech - 298,100<br>Festive Walk 2 - 231,736<br>Robinsons City - 573,650<br>Robinsons Jaro - 359,371<br>Foremost - 56,431</div>
                </div>
            </div>
            <div class="vertical-rectangle-kspc-apr2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                KSPC (10,229,000)
                <button class="mini-button">17.03%</button>
            </div>
            <div class="vertical-rectangle-scpc-apr2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SCPC (9,275,000)
                <button class="mini-button">15.44%</button>
            </div>
            <div class="vertical-rectangle-edc-apr2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                EDC (8,736,000)
                <button class="mini-button">14.55%</button>
            </div>
            <div class="vertical-rectangle-pedc-apr2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                PEDC (3,558,634)
                <button class="mini-button">5.93%</button>
            </div>
            <div class="vertical-rectangle-wesm-apr2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                WESM (20,355,459)
                <button class="mini-button">33.89%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">60,056,730 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-apr2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (33,294,650)
                <button class="mini-button">55.44%</button>
            </div>
            <div class="vertical-rectangle-apr2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (9,730,714)
                <button class="mini-button">16.20%</button>
            </div>
            <div class="vertical-rectangle-apr2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,031,366)
                <button class="mini-button">28.36%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-apr2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (242,895)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )

    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 245px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">72,037,516 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-apr2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (28,996,976)
                        <button class="mini-button">40.25%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-apr2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (5,068,020)
                        <button class="mini-button-2">7.04%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-apr2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (185,696)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-apr2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (29,237,095)
                        <button class="mini-button">40.59%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-apr2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (872,672)
                        <button class="mini-button-2">1.21%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-apr2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (945,423)
                        <button class="mini-button-2">1.31%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-apr2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (422,536)
                        <button class="mini-button-2">0.59%</button>
                    </div>
                    <div class="vertical-rectangle-eou-apr2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                       EOU (45,056)
                        <button class="mini-button-2">0.06%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-apr2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (5,758,070)
                        <button class="mini-button-2">7.99%</button>
                    </div>
                    <div class="vertical-rectangle-stss-apr2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (505,972)
                        <button class="mini-button-2">0.70%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -170px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -405px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

# May 2025
elif tabs == "May 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">71,735,154 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
    """
    <style>
        /* Force small gap between rectangles */
        .rectangle-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .mini-button {
            font-size: 12px; /* Make the text small */
            padding: 2px 5 px; /* Adjust padding for a smaller button */
            background-color: white; /* Green background */
            color: black; /* White text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Slightly rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            margin-left: 5px; /* Space between text and button */
        }
        .mini-button-2 {
            font-size: 8px; /* Even smaller text */
            padding: 2px 5px; /* Smaller padding for a more compact button */
            background-color: white; /* White background */
            color: black; /* Black text color */
            border: none; /* No border */
            border-radius: 3px; /* Smaller rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            margin-left: 5px; /* Reduced space between text and button */
        }
        .rectangle-container-2 {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px !important; /* Minimal gap */
            margin-top: 15px;
            padding: 0 !important; /* Remove container padding */
        }
        .invisible-rectangle-1st-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 480px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 410px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-kspc-may2025 {
            background-color: #4682B4; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 15.14%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-scpc-may2025 {
            background-color: #cc3333;
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 10.52%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-wesm-may2025 {
            background-color: #FFDB58; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 42.46%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-edc-may2025 {
            background-color: #228B22; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 13.48%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-pedc-may2025 {
            background-color: #FFA500; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 5.23%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 75%;
        }
        .vertical-rectangle-cc-may2025 {
            background-color: #8861A8; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 13.16%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            position: relative;
            pointer-events: auto;
            font-size: 85%;
        }
        .vertical-rectangle-cc-may2025:hover .tooltip-may2025 {
            display: block;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
            z-index: 15;
        }
        .tooltip-may2025 {
            display: none;
            position: absolute;
            top: -65px;
            left: 105%;
            width: 135%;
            margin-left: 10px;
            background-color: #8861A8;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 15;
            opacity: 100%;
        }
        .vertical-rectangle-may2025-ilomore01 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 45.84%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-may2025-sbamore02 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 25.39%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-may2025-sbamore03 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 28.76%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .net-metering-may2025 {
            background-color: #365E32; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 90%;
            height: 100%;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            font-size: 85%;
        }
        .vertical-rectangle-residential-may2025 {
            background-color: #3A4C61; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 42.12%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-commercial-may2025 {
            background-color: #7A4B56; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 7.54%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 60%;
        }
        .vertical-rectangle-intermediate-may2025 {
            background-color: #556B2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.26%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 65%;
        }
        .vertical-rectangle-power-may2025 {
            background-color: #5D3F66; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 42.25%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 85%;
        }
        .vertical-rectangle-citygovernment-may2025 {
            background-color: #7A5A2F; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.28%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-othergovernment-may2025 {
            background-color: #7A4A29; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 70%;
        }
        .vertical-rectangle-citystreetlights-may2025 {
            background-color: #6B4F3B; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.60%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 55%;
        }
        .vertical-rectangle-eou-may2025 {
            background-color: #C0B97B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 0.05%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 70%;
        }
        .vertical-rectangle-stss-may2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 2.88%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
            font-size: 65%;
        }
        .vertical-rectangle-feeder-may2025 {
            background-color: #C09C9B; /* Example color */
            color: black !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 100%;
            height: 1.70%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
            font-size: 63%;
        }
        .invisible-rectangle-3rd-column {
            width: 90%;  /* Set the width of the rectangle */
            height: 360px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-cc-may2025"> 
                    Contestables (9,442,641)
                    <button class="mini-button">13.16%</button>
                <div class="tooltip-may2025">
                    <div class="arrow">SM Delgado - 457,543<br>SM City - 2,122,617<br>Golden Portals - 592,316<br>QHP - 424,323<br>Mary Mart - 253,519<br>HEVA - 337,050<br>Marriott - 427,379<br>Festive Walk Mall - 655,861<br>Smart Communications - 339,631<br>HEVA ICC - 122,027<br>KAREILA - 209,105<br>One Fintech - 366,798<br>Seda Hotel - 123,793<br>Innove Communications - 188,516<br>Adauge (The Shops) - 111,095<br>Sunnyfield - 225,691<br>Two Fintech - 354,734<br>Festive Walk 2 - 277,394<br>Robinsons City - 958,617<br>Robinsons Jaro - 588,853<br>Foremost - 305,779</div>
                </div>
            </div>
            <div class="vertical-rectangle-kspc-may2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                KSPC (10,860,000)
                <button class="mini-button">15.14%</button>
            </div>
            <div class="vertical-rectangle-scpc-may2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SCPC (7,550,000)
                <button class="mini-button">10.52%</button>
            </div>
            <div class="vertical-rectangle-edc-may2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                EDC (9,672,000)
                <button class="mini-button">13.48%</button>
            </div>
            <div class="vertical-rectangle-pedc-may2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                PEDC (3,750,000)
                <button class="mini-button">5.23%</button>
            </div>
            <div class="vertical-rectangle-wesm-may2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                WESM (30,460,513)
                <button class="mini-button">42.46%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">71,735,154 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-may2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (32,885,805)
                <button class="mini-button">45.84%</button>
            </div>
            <div class="vertical-rectangle-may2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (18,216,953)
                <button class="mini-button">25.39%</button>
            </div>
            <div class="vertical-rectangle-may2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (20,632,397)
                <button class="mini-button">28.76%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-may2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (302,361)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
        
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 210px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )
        
    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">70,762,097 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-may2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (29,805,946)
                        <button class="mini-button">42.12%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-may2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (5,335,889)
                        <button class="mini-button-2">7.54%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-may2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (185,918)
                        <button class="mini-button-2">0.26%</button>
                    </div>
                    <div class="vertical-rectangle-power-may2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (29,894,455)
                        <button class="mini-button">42.25%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-may2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (904,407)
                        <button class="mini-button-2">1.28%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-may2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (936,886)
                        <button class="mini-button-2">1.32%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-may2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (421,558)
                        <button class="mini-button-2">0.60%</button>
                    </div>
                     <div class="vertical-rectangle-eou-may2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        EOU (34,123)
                        <button class="mini-button-2">0.05%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-may2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (1,205,862)
                        <button class="mini-button-2">1.70%</button>
                    </div>
                    <div class="vertical-rectangle-stss-may2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (2,037,053)
                        <button class="mini-button-2">2.88%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -140px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -358px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# June 2025
elif tabs == "June 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">70,484,700 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
        """
        <style>
            /* Force small gap between rectangles */
            .rectangle-container {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 10px !important; /* Minimal gap */
                margin: 0 !important; /* Remove container margin */
                padding: 0 !important; /* Remove container padding */
            }

            .mini-button {
                font-size: 12px; /* Make the text small */
                padding: 2px 5 px; /* Adjust padding for a smaller button */
                background-color: white; /* Green background */
                color: black; /* White text color */
                border: none; /* Remove border */
                border-radius: 5px; /* Slightly rounded corners */
                cursor: pointer; /* Change cursor to pointer on hover */
                margin-left: 5px; /* Space between text and button */
            }

            .mini-button-2 {
                font-size: 8px; /* Even smaller text */
                padding: 2px 5px; /* Smaller padding for a more compact button */
                background-color: white; /* White background */
                color: black; /* Black text color */
                border: none; /* No border */
                border-radius: 3px; /* Smaller rounded corners */
                cursor: pointer; /* Pointer cursor on hover */
                margin-left: 5px; /* Reduced space between text and button */
            }

            .rectangle-container-2 {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 10px !important; /* Minimal gap */
                margin-top: 15px;
                padding: 0 !important; /* Remove container padding */
            }

            .invisible-rectangle-1st-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 480px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            }

            .invisible-rectangle-2nd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 480px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }

            .invisible-rectangle-3rd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 410px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }

            .vertical-rectangle-kspc-june2025 {
                background-color: #4682B4; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 15.63%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-scpc-june2025 {
                background-color: #cc3333;
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 8.62%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-wesm-june2025 {
                background-color: #FFDB58; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 42.63%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-edc-june2025 {
                background-color: #228B22; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 13.73%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-pedc-june2025 {
                background-color: #FFA500; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 5.74%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 75%;
            }

            .vertical-rectangle-cc-june2025 {
                background-color: #8861A8; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 13.64%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                position: relative;
                pointer-events: auto;
                font-size: 85%;
            }

            .vertical-rectangle-cc-june2025:hover .tooltip-june2025 {
                display: block;
                transform: scale(1.05);
                transition: background-color 0.3s, transform 0.3s;
                z-index: 15;
            }

            .tooltip-june2025 {
                display: none;
                position: absolute;
                top: -65px;
                left: 105%;
                width: 135%;
                margin-left: 10px;
                background-color: #8861A8;
                color: white;
                padding: 10px;
                border: 1px solid #ddd;
                z-index: 15;
                opacity: 100%;
            }

            .vertical-rectangle-june2025-ilomore01 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 33.95%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .vertical-rectangle-june2025-sbamore02 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 34.65%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .vertical-rectangle-june2025-sbamore03 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 31.40%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .net-metering-june2025 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 90%;
                height: 100%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }
            .vertical-rectangle-residential-jun2025 {
                background-color: #3A4C61; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 40.74%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }
            .vertical-rectangle-commercial-jun2025 {
                background-color: #7A4B56; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 7.44%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 60%;
            }
            .vertical-rectangle-intermediate-jun2025 {
                background-color: #556B2F; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 0.27%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 65%;
            }
            .vertical-rectangle-power-jun2025 {
                background-color: #5D3F66; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 43.25%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }
            .vertical-rectangle-citygovernment-jun2025 {
                background-color: #7A5A2F; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.49%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 70%;
            }
            .vertical-rectangle-othergovernment-jun2025 {
                background-color: #7A4A29; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.47%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 65%;
            }
            .vertical-rectangle-citystreetlights-jun2025 {
                background-color: #6B4F3B; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 0.62%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 55%;
            }
            .vertical-rectangle-eou-jun2025 {
                background-color: #C0B97B; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 0.06%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;    
                font-size: 70%;
            }
            .vertical-rectangle-stss-jun2025 {
                background-color: #C09C9B; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 2.93%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;    
                font-size: 65%;
            }
            .vertical-rectangle-feeder-jun2025 {
                background-color: #C09C9B; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.73%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 63%;
            }
            .invisible-rectangle-3rd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 360px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }
        }
        </style>
        <div class="rectangle-container">
            <div class="invisible-rectangle-1st-column">
                <div class="vertical-rectangle-cc-june2025"> 
                        Contestables (9,615,208)
                        <button class="mini-button">13.64%</button>
                    <div class="tooltip-june2025">
                        <div class="arrow">SM Delgado - 501,318<br>SM City - 2,280,416<br>Golden Portals - 541,890<br>QHP - 427,565<br>Mary Mart - 273,526<br>HEVA - 316,999<br>Marriott - 419,145<br>Festive Walk Mall - 674,361<br>Smart Communications - 328,048<br>HEVA ICC - 122,990<br>KAREILA - 205,348<br>One Fintech - 341,076<br>Seda Hotel - 117,553<br>Innove Communications - 184,559<br>Adauge (The Shops) - 113,692<br>Sunnyfield - 182,004<br>Two Fintech - 348,317<br>Festive Walk 2 - 274,185<br>Robinsons City - 1,030,696<br>Robinsons Jaro - 614,393<br>Foremost - 317,127</div>
                    </div>
                </div>
                <div class="vertical-rectangle-kspc-june2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    KSPC (11,020,000)
                    <button class="mini-button">15.63%</button>
                </div>
                <div class="vertical-rectangle-scpc-june2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    SCPC (6,075,000)
                    <button class="mini-button">8.62%</button>
                </div>
                <div class="vertical-rectangle-edc-june2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    EDC (9,680,000)
                    <button class="mini-button">13.73%</button>
                </div>
                <div class="vertical-rectangle-pedc-june2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    PEDC (4,045,000)
                    <button class="mini-button">5.74%</button>
                </div>
                <div class="vertical-rectangle-wesm-june2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    WESM (30,049,492)
                    <button class="mini-button">42.63%</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">70,484,700 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-june2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (23,927,687)
                <button class="mini-button">33.95%</button>
            </div>
            <div class="vertical-rectangle-june2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (24,422,146)
                <button class="mini-button">34.65%</button>
            </div>
            <div class="vertical-rectangle-june2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (22,134,866)
                <button class="mini-button">31.40%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-june2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (277,398)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
        
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 210px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )
        
    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">69,527,152 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jun2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (28,326,290)
                        <button class="mini-button">40.74%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-jun2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (5,173,877)
                        <button class="mini-button-2">7.44%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-jun2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (186,622)
                        <button class="mini-button-2">0.27%</button>
                    </div>
                    <div class="vertical-rectangle-power-jun2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (30,069,505)
                        <button class="mini-button">43.25%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-jun2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (1,034,397)
                        <button class="mini-button-2">1.49%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-jun2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (1,020,707)
                        <button class="mini-button-2">1.47%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jun2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (433,806)
                        <button class="mini-button-2">0.62%</button>
                    </div>
                    <div class="vertical-rectangle-eou-jun2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        EOU (39,033)
                        <button class="mini-button-2">0.06%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-jun2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (1,205,862)
                        <button class="mini-button-2">1.73%</button>
                    </div>
                    <div class="vertical-rectangle-stss-jun2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (2,037,053)
                        <button class="mini-button-2">2.93%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -140px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -358px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# July 2025
elif tabs == "July 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">70,784,514 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
        """
        <style>
            /* Force small gap between rectangles */
            .rectangle-container {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 10px !important; /* Minimal gap */
                margin: 0 !important; /* Remove container margin */
                padding: 0 !important; /* Remove container padding */
            }

            .mini-button {
                font-size: 12px; /* Make the text small */
                padding: 2px 5 px; /* Adjust padding for a smaller button */
                background-color: white; /* Green background */
                color: black; /* White text color */
                border: none; /* Remove border */
                border-radius: 5px; /* Slightly rounded corners */
                cursor: pointer; /* Change cursor to pointer on hover */
                margin-left: 5px; /* Space between text and button */
            }

            .mini-button-2 {
                font-size: 8px; /* Even smaller text */
                padding: 2px 5px; /* Smaller padding for a more compact button */
                background-color: white; /* White background */
                color: black; /* Black text color */
                border: none; /* No border */
                border-radius: 3px; /* Smaller rounded corners */
                cursor: pointer; /* Pointer cursor on hover */
                margin-left: 5px; /* Reduced space between text and button */
            }

            .rectangle-container-2 {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 10px !important; /* Minimal gap */
                margin-top: 15px;
                padding: 0 !important; /* Remove container padding */
            }

            .invisible-rectangle-1st-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 480px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            }

            .invisible-rectangle-2nd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 480px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }

            .invisible-rectangle-3rd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 410px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }

            .vertical-rectangle-kspc-jul2025 {
                background-color: #4682B4; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 15.33%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-scpc-jul2025 {
                background-color: #cc3333;
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 11.04%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-wesm-jul2025 {
                background-color: #FFDB58; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 40.38%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-edc-jul2025 {
                background-color: #228B22; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 13.67%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-pedc-jul2025 {
                background-color: #FFA500; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 5.47%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 75%;
            }

            .vertical-rectangle-cc-jul2025 {
                background-color: #8861A8; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 14.12%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                position: relative;
                pointer-events: auto;
                font-size: 85%;
            }

            .vertical-rectangle-cc-jul2025:hover .tooltip-jul2025 {
                display: block;
                transform: scale(1.05);
                transition: background-color 0.3s, transform 0.3s;
                z-index: 15;
            }

            .tooltip-jul2025 {
                display: none;
                position: absolute;
                top: -65px;
                left: 105%;
                width: 135%;
                margin-left: 10px;
                background-color: #8861A8;
                color: white;
                padding: 10px;
                border: 1px solid #ddd;
                z-index: 15;
                opacity: 100%;
            }

            .vertical-rectangle-jul2025-ilomore01 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 34.81%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .vertical-rectangle-jul2025-sbamore02 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 33.95%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .vertical-rectangle-jul2025-sbamore03 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 31.23%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .net-metering-jul2025 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 90%;
                height: 100%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }
            .vertical-rectangle-residential-jul2025 {
                background-color: #3A4C61; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 41.04%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }
            .vertical-rectangle-commercial-jul2025 {
                background-color: #7A4B56; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 7.71%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 60%;
            }
            .vertical-rectangle-intermediate-jul2025 {
                background-color: #556B2F; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 0.28%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 65%;
            }
            .vertical-rectangle-power-jul2025 {
                background-color: #5D3F66; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 44.13%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }
            .vertical-rectangle-citygovernment-jul2025 {
                background-color: #7A5A2F; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.68%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 70%;
            }
            .vertical-rectangle-othergovernment-jul2025 {
                background-color: #7A4A29; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.31%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 65%;
            }
            .vertical-rectangle-citystreetlights-jul2025 {
                background-color: #6B4F3B; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 0.64%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 55%;
            }
            .vertical-rectangle-eou-jul2025 {
                background-color: #C0B97B; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 0.06%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;    
                font-size: 70%;
            }
            .vertical-rectangle-stss-jul2025 {
                background-color: #C09C9B; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.41%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;    
                font-size: 65%;
            }
            .vertical-rectangle-feeder-jul2025 {
                background-color: #C09C9B; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 1.74%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 63%;
            }
            .invisible-rectangle-3rd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 315px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }
        }
        </style>
        <div class="rectangle-container">
            <div class="invisible-rectangle-1st-column">
                <div class="vertical-rectangle-cc-jul2025"> 
                        Contestables (9,994,803)
                        <button class="mini-button">14.12%</button>
                    <div class="tooltip-jul2025">
                        <div class="arrow">SM Delgado - 498,018<br>SM City - 2,371,800<br>Golden Portals - 622,976<br>QHP - 443,990<br>Mary Mart - 301,976<br>HEVA - 331,283<br>Marriott - 427,593<br>Festive Walk Mall - 709,974<br>Smart Communications - 338,951<br>HEVA ICC - 127,550<br>KAREILA - 232,380<br>One Fintech - 342,097<br>Seda Hotel - 121,222<br>Innove Communications - 187,877<br>Adauge (The Shops) - 119,830<br>Sunnyfield - 185,564<br>Two Fintech - 350,171<br>Festive Walk 2 - 283,737<br>Robinsons City - 1,029,774<br>Robinsons Jaro - 655,441<br>Foremost - 312,599</div>
                    </div>
                </div>
                <div class="vertical-rectangle-kspc-jul2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    KSPC (10,850,000)
                    <button class="mini-button">15.33%</button>
                </div>
                <div class="vertical-rectangle-scpc-jul2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    SCPC (7,812,500)
                    <button class="mini-button">11.04%</button>
                </div>
                <div class="vertical-rectangle-edc-jul2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    EDC (9,675,000)
                    <button class="mini-button">13.67%</button>
                </div>
                <div class="vertical-rectangle-pedc-jul2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    PEDC (3,870,000)
                    <button class="mini-button">5.47%</button>
                </div>
                <div class="vertical-rectangle-wesm-jul2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    WESM (28,582,211)
                    <button class="mini-button">40.38%</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">70,784,515 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-jul2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (24,642,498)
                <button class="mini-button">34.81%</button>
            </div>
            <div class="vertical-rectangle-jul2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (24,032,596)
                <button class="mini-button">33.95%</button>
            </div>
            <div class="vertical-rectangle-jul2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (22,109,421)
                <button class="mini-button">31.23%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-jul2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (237,780)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )
        
    with col4:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 200px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 198px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )
        
    with col5:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{sales_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 8px">
                <div style="background-color: #517d8b; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{third_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 10px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">67,244,222 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jul2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Residential (27,599,335)
                        <button class="mini-button">41.04%</button>
                    </div>
                    <div class="vertical-rectangle-commercial-jul2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Commercial (5,186,758)
                        <button class="mini-button-2">7.71%</button>
                    </div>
                    <div class="vertical-rectangle-intermediate-jul2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Intermediate (186,905)
                        <button class="mini-button-2">0.28%</button>
                    </div>
                    <div class="vertical-rectangle-power-jul2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Power (29,676,133)
                        <button class="mini-button">44.13%</button>
                    </div>
                    <div class="vertical-rectangle-citygovernment-jul2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        City Govt. (1,127,150)
                        <button class="mini-button-2">1.68%</button>
                    </div>
                    <div class="vertical-rectangle-othergovernment-jul2025" onclick="fetch('/?rect=6').then(() => window.location.reload())">
                        Other Govt. (877,737)
                        <button class="mini-button-2">1.31%</button>
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jul2025" onclick="fetch('/?rect=7').then(() => window.location.reload())">
                        City Streetlights (430,165)
                        <button class="mini-button-2">0.64%</button>
                    </div>
                    <div class="vertical-rectangle-eou-jul2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        EOU (39,476)
                        <button class="mini-button-2">0.06%</button>
                    </div>
                    <div class="vertical-rectangle-feeder-jul2025" onclick="fetch('/?rect=8').then(() => window.location.reload())">
                        DSL_Feeder (1,171,087)
                        <button class="mini-button-2">1.74%</button>
                    </div>
                    <div class="vertical-rectangle-stss-jul2025" onclick="fetch('/?rect=9').then(() => window.location.reload())">
                        DSL_ST+SS (949,476)
                        <button class="mini-button-2">1.41%</button>
                    </div>
                    <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 0%; margin-top: -120px; z-index:2;">
            <img src="data:image/png;base64,{systemloss_img_str}" width="35%">
        </div>
            <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; text-align: center; height: 100%; margin-left: 30%; font-family: Arial; margin-top: -312px; margin-bottom: 10px">
                <div style="background-color: #496615; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 20px; font-weight: bold; color: white; margin: 0;">{third_column_title_2}</p>
                </div>
            </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# August 2025
elif tabs == "August 2025":
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

    with col1:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index: 2;">
            <img src="data:image/png;base64,{power_plant_img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #932c27; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{first_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">67,007,407 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
        """
        <style>
            /* Force small gap between rectangles */
            .rectangle-container {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 10px !important; /* Minimal gap */
                margin: 0 !important; /* Remove container margin */
                padding: 0 !important; /* Remove container padding */
            }

            .mini-button {
                font-size: 12px; /* Make the text small */
                padding: 2px 5 px; /* Adjust padding for a smaller button */
                background-color: white; /* Green background */
                color: black; /* White text color */
                border: none; /* Remove border */
                border-radius: 5px; /* Slightly rounded corners */
                cursor: pointer; /* Change cursor to pointer on hover */
                margin-left: 5px; /* Space between text and button */
            }

            .mini-button-2 {
                font-size: 8px; /* Even smaller text */
                padding: 2px 5px; /* Smaller padding for a more compact button */
                background-color: white; /* White background */
                color: black; /* Black text color */
                border: none; /* No border */
                border-radius: 3px; /* Smaller rounded corners */
                cursor: pointer; /* Pointer cursor on hover */
                margin-left: 5px; /* Reduced space between text and button */
            }

            .rectangle-container-2 {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                gap: 10px !important; /* Minimal gap */
                margin-top: 15px;
                padding: 0 !important; /* Remove container padding */
            }

            .invisible-rectangle-1st-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 480px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            }

            .invisible-rectangle-2nd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 480px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }

            .invisible-rectangle-3rd-column {
                width: 90%;  /* Set the width of the rectangle */
                height: 410px; /* Set the height of the rectangle */
                background-color: white; /* Make the rectangle invisible */
                border: 1px solid transparent; /* Optional: Add a border (invisible here) */
                position: relative;  /* Allows child elements to be positioned relative to this */
                z-index: 1; /* Ensure that the parent has lower stacking order than the children */
            }

            .vertical-rectangle-kspc-aug2025 {
                background-color: #4682B4; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 16.98%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-scpc-aug2025 {
                background-color: #cc3333;
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 7.24%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 75%;
            }

            .vertical-rectangle-wesm-aug2025 {
                background-color: #FFDB58; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 42.00%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-edc-aug2025 {
                background-color: #228B22; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 13.97%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 85%;
            }

            .vertical-rectangle-pedc-aug2025 {
                background-color: #FFA500; /* Example color */
                color: black !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 5.67%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                font-size: 75%;
            }

            .vertical-rectangle-cc-aug2025 {
                background-color: #8861A8; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 14.14%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                z-index: 10;
                position: relative;
                pointer-events: auto;
                font-size: 85%;
            }

            .vertical-rectangle-cc-aug2025:hover .tooltip-aug2025 {
                display: block;
                transform: scale(1.05);
                transition: background-color 0.3s, transform 0.3s;
                z-index: 15;
            }

            .tooltip-aug2025 {
                display: none;
                position: absolute;
                top: -65px;
                left: 105%;
                width: 135%;
                margin-left: 10px;
                background-color: #8861A8;
                color: white;
                padding: 10px;
                border: 1px solid #ddd;
                z-index: 15;
                opacity: 100%;
            }

            .vertical-rectangle-aug2025-ilomore01 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 37.09%;
                top: 0;
                left: 0;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .vertical-rectangle-aug2025-sbamore02 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 31.63%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .vertical-rectangle-aug2025-sbamore03 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 100%;
                height: 31.28%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }

            .net-metering-aug2025 {
                background-color: #365E32; /* Example color */
                color: white !important;;
                padding: 10px;
                border: 2px solid #ccc;
                font-weight: bold;
                width: 90%;
                height: 100%;
                display: flex;
                font-size: 12px;
                border-radius: 5px;
                text-align: center;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                margin: 0 !important; /* Remove rectangle margin */
                box-sizing: border-box; /* Ensure consistent sizing */
                font-size: 85%;
            }
        }
        </style>
        <div class="rectangle-container">
            <div class="invisible-rectangle-1st-column">
                <div class="vertical-rectangle-cc-aug2025"> 
                        Contestables (9,471,603)
                        <button class="mini-button">14.14%</button>
                    <div class="tooltip-aug2025">
                        <div class="arrow">SM Delgado - 472,120<br>SM City - 2,173,491<br>Golden Portals - 647,236<br>QHP - 432,249<br>Mary Mart - 289,473<br>HEVA - 339,620<br>Marriott - 404,249<br>Festive Walk Mall - 668,947<br>Smart Communications - 325,823<br>HEVA ICC - 97,657<br>KAREILA - 231,525<br>One Fintech - 315,374<br>Seda Hotel - 113,017<br>Innove Communications - 180,973<br>Adauge (The Shops) - 113,257<br>Sunnyfield - 185,484<br>Two Fintech - 341,256<br>Festive Walk 2 - 277,880<br>Robinsons City - 963,653<br>Robinsons Jaro - 608,613<br>Foremost - 289,706</div>
                    </div>
                </div>
                <div class="vertical-rectangle-kspc-aug2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    KSPC (11,380,000)
                    <button class="mini-button">16.98%</button>
                </div>
                <div class="vertical-rectangle-scpc-aug2025" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    SCPC (4,850,000)
                    <button class="mini-button">7.24%</button>
                </div>
                <div class="vertical-rectangle-edc-aug2025" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    EDC (9,360,000)
                    <button class="mini-button">13.97%</button>
                </div>
                <div class="vertical-rectangle-pedc-aug2025" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    PEDC (3,800,000)
                    <button class="mini-button">5.67%</button>
                </div>
                <div class="vertical-rectangle-wesm-aug2025" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    WESM (28,145,804)
                    <button class="mini-button">42.00%</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    with col2:
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; height: 100%; margin-top: 300px; z-index:2;">
            <img src="data:image/png;base64,{arrow_img_str}" width="100%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

    with col3:    
        # Second column icon
        st.markdown(
        f'''
        <div style="position: relative; display: flex; justify-content: flex-start; align-items: center; height: 100%; margin-left: 30%; z-index:2;">
            <img src="data:image/png;base64,{img_str}" width="45%">
        </div>
        ''', 
        unsafe_allow_html=True
    )

        # Second column title
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; text-align: center; height: 100%; margin-left: -20px; margin-top: -9px; font-family: Arial; margin-bottom: 20px">
                <div style="background-color: #88778d; padding: 2px 15px; border-radius: 100px; z-index:1;">
                    <p style="font-size: 24px; font-weight: bold; color: white; margin: 0;">{second_column_title}</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        # Show total     
        st.markdown(
            f'''
            <div style="position: relative; display: flex; justify-content: center; align-items: center; height: 100%; margin-left: -12%; margin-top: 0px; font-family: Arial;">
                <div style="text-decoration-line: underline;">
                    <p style="font-size: 18px; font-weight: bold; color: white; margin: 0;">67,007,406 kWh</p>
                </div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rectangle-container">
        <div class="invisible-rectangle-2nd-column">
            <div class="vertical-rectangle-aug2025-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (24,852,715)
                <button class="mini-button">37.09%</button>
            </div>
            <div class="vertical-rectangle-aug2025-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (21,192,752)
                <button class="mini-button">31.63%</button>
            </div>
            <div class="vertical-rectangle-aug2025-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (20,961,939)
                <button class="mini-button">31.28%</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
        st.markdown(
                f"""    
            <div class="rectangle-container-2">
                <div class="net-metering-aug2025" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Net Metering (236,814)
            </div>
            </div>
        """,
        unsafe_allow_html=True
    )