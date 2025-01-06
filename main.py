import streamlit as st
from PIL import Image

st.set_page_config(page_title="Statistics Dashboard", page_icon="more_power_logo.png", layout="wide")

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
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

def add_logo_with_text(logo_path, text, max_width=None, max_height=None, text_size=16, font_family="Arial"):
    """Adds a logo with text to the sidebar, maintaining aspect ratio.

    Args:
        logo_path (str): Path to the logo image.
        text (str): Text to display below the logo.
        max_width (int, optional): Maximum width of the logo. Defaults to None.
        max_height (int, optional): Maximum height of the logo. Defaults to None.
        text_size (int, optional): Font size for the text. Defaults to 16.
        font_family (str, optional): Font family for the text. Defaults to "Arial".
    """
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

def get_base64_from_image(image):
    """Converts image to base64 for embedding in HTML"""
    import base64
    from io import BytesIO

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

add_logo_with_text("more_power_logo.png", "Statistics Dashboard", max_width=150, text_size=20, font_family="Helvetica")

tabs = st.sidebar.radio("Months", ["January 2024", "February 2024", "March 2024", "April 2024", "May 2024", "June 2024", "July 2024", "August 2024", "September 2024", "October 2024", "November 2024", "December 2024"], index=0)

# January 2024
if tabs == "January 2024":    
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            position: relative;  /* Allows child elements to be positioned relative to this */
            z-index: 1; /* Ensure that the parent has lower stacking order than the children */
        }
        .vertical-rectangle-cc-jan {
            background-color: #708090; /* Example color */
            color: white;  /* Text color */
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px; /* Matching width with the parent */
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
        }
        .tooltip-jan {
            display: block;
            position: absolute;
            top: -50px;
            left: 100%;
            width: 150%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-jan .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-4th-column {
            width: 165px;  /* Set the width of the rectangle */
            height: 30px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-jan2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-jan2024-ilomore01:hover {{
            background-color: #A3646A;
            color: #000;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
        }}
        .vertical-rectangle-jan2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-jan2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-kspc-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 46.66%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 9.02%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.30%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 40.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.77%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.24%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.92%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 17.80%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 82.20%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-jan2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (32,109,152)
            </div>
            <div class="vertical-rectangle-jan2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,817,384)
            </div>
            <div class="vertical-rectangle-jan2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,182,011)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-jan">
                        Contestables
                        <div class="tooltip-jan">
                            <div class="arrow"></div>SM Delgado - 464,921<br>SM City - 2,381,612<br>Golden Portals -  634,825<br>QHP -  395,239<br>Mary Mart -  275,059<br>HEVA -  414,681<br>Marriott -  419,552<br>Festive Walk Mall -  655,735<br>Smart Communications -  326,431<br>HEVA ICC -  125,321<br>KAREILA -  214,966<br>One Fintech -  298,937<br>Seda Hotel -  119,976<br>Innove Communications -  179,489<br>Adauge (The Shops) -  85,622
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        SCPC (16,882,500)
                    </div>
                    <div class="vertical-rectangle-kspc-jan" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        KSPC (11,245,000)
                    </div>
                    <div class="vertical-rectangle-edc-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        EDC (9,360,000)
                    </div>
                    <div class="vertical-rectangle-wesm-jan" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                        WESM (18,628,682)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (22,612,876)
                    </div>
                    <div class="vertical-rectangle-commercial-jan" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,370,276)
                    </div>
                    <div class="vertical-rectangle-intermediate-jan" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (143,182)
                    </div>
                    <div class="vertical-rectangle-power-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (19,430,194)
                    </div>
                    <div class="vertical-rectangle-citygovernment-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (859,156)
                    </div>
                    <div class="vertical-rectangle-othergovernment-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (600,334)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (446,277)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,505,359)
                    </div>
                    <div class="vertical-rectangle-stss-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (758,861)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
            )

# February 2024
elif tabs == "February 2024": 
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])
    
    with col1:
        st.markdown("Input")
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
        .rectangle-container-extra {
            display: flex;
            flex-direction: column;
            gap: 10px !important; /* Minimal gap */
            margin: 0 !important; /* Remove container margin */
            padding: 0 !important; /* Remove container padding */
        }
        .vertical-rectangle-feb2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-feb2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-feb2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-feb {
            display: block;
            position: absolute;
            top: -45px;
            left: 37%;
            width: 55%;
            margin-left: 10px;
            background-color: #fff;
            color: black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-feb .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 45.68%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 9.12%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.30%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 40.76%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.97%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.24%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.92%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 22.39%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-feb {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 77.61%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-feb2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (30,039,371)
            </div>
            <div class="vertical-rectangle-feb2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (12,737,984)
            </div>
            <div class="vertical-rectangle-feb2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,203,712)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-feb">
                        Contestables
                        <div class="tooltip-feb">
                            <div class="arrow"></div>SM Delgado - 412,418<br>SM City - 2,133,582<br>Golden Portals - 517,279<br>QHP - 373,970<br>Mary Mart - 242,663<br>HEVA - 372,596<br>Marriott - 283,046<br>Festive Walk Mall - 624,995<br>Smart Communications - 316,744<br>HEVA ICC - 116,031<br>KAREILA - 200,944<br>One Fintech - 410,240<br>Seda Hotel - 110,157<br>Innove Communications - 174,634<br>Adauge (The Shops) - 84,544
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-feb" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,790,400)
                    </div>
                    <div class="vertical-rectangle-kspc-feb" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,151,400)
                    </div>
                    <div class="vertical-rectangle-edc-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,372,300)
                    </div>
                    <div class="vertical-rectangle-wesm-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (11,293,125)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (22,402,208)
                    </div>
                    <div class="vertical-rectangle-commercial-feb" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,474,132)
                    </div>
                    <div class="vertical-rectangle-intermediate-feb" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (148,940)
                    </div>
                    <div class="vertical-rectangle-power-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (19,985,679)
                    </div>
                    <div class="vertical-rectangle-citygovernment-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (965,591)
                    </div>
                    <div class="vertical-rectangle-othergovernment-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (607,960)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (452,367)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,839,645)
                    </div>
                    <div class="vertical-rectangle-stss-feb" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (819,041)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# March 2024
elif tabs == "March 2024": 
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-mar2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-mar2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-mar2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-mar {
            display: block;
            position: absolute;
            top: -45px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-mar .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .hoverable-contestables-jan {
            visibility: hidden;
            background-color: white;
            color: black;
            left: 100px;
            width:200px;
            height: 200px;
        }
        .vertical-rectangle-residential-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 47.92%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.99%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.31%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 38.90%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.86%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-citystreetlights-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.78%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 69.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 30.33%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-mar2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (30,315,442)
            </div>
            <div class="vertical-rectangle-mar2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,023,080)
            </div>
            <div class="vertical-rectangle-mar2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,096,277)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-mar">
                            <div class="arrow"></div>SM Delgado - 419,025<br>SM City - 2,133,598<br>Golden Portals - 682,832<br>QHP - 377,284<br>Mary Mart - 237,082<br>HEVA - 401,585<br>Marriott - 448,332<br>Festive Walk Mall - 634,036<br>Smart Communications - 333,804<br>HEVA ICC - 132,857<br>KAREILA - 208,988<br>One Fintech - 288,040<br>Seda Hotel - 114,442<br>Innove Communications - 185,419<br>Adauge (The Shops) - 102,167<br>Sunnyfield - 187,073
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-mar" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,535,500)
                    </div>
                    <div class="vertical-rectangle-edc-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,579,400)
                    </div>
                    <div class="vertical-rectangle-scpc-mar" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,698,200)
                    </div>
                    <div class="vertical-rectangle-wesm-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (11,735,138)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (25,402,152)
                    </div>
                    <div class="vertical-rectangle-commercial-mar" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,763,443)
                    </div>
                    <div class="vertical-rectangle-intermediate-mar" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (166,078)
                    </div>
                    <div class="vertical-rectangle-power-mar" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (20,619,608)
                    </div>
                    <div class="vertical-rectangle-citygovernment-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (986,917)
                    </div>
                    <div class="vertical-rectangle-othergovernment-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (653,259)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (414,691)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (354,998)
                    </div>
                    <div class="vertical-rectangle-stss-mar" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (815,450)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# April 2024
elif tabs == "April 2024": 
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-apr2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-apr2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-apr2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;
            height: 300px;
            background-color: white;
            border: 1px solid transparent;
            margin-bottom: 100px;
        }
        .tooltip-apr {
            display: block;
            position: absolute;
            top: -48px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-apr .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 50.41%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.89%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 36.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-othergovernment-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.18%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
            z-index: 10;
        }
        .vertical-rectangle-stss-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 24.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-apr {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 75.68%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-apr2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (32,290,271)
            </div>
            <div class="vertical-rectangle-apr2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (12,939,584)
            </div>
            <div class="vertical-rectangle-apr2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (15,262,642)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-apr">
                            <div class="arrow"></div>SM Delgado - 404,103<br>SM City - 2,050,316<br>Golden Portals - 611,192<br>QHP - 360,829<br>Mary Mart - 224,742<br>HEVA - 362,058<br>Marriott - 396,130<br>Festive Walk Mall - 594,367<br>Smart Communications - 314,155<br>HEVA ICC - 110,785<br>KAREILA - 210,198<br>One Fintech - 289,569<br>Seda Hotel - 107,910<br>Innove Communications - 175,184<br>Adauge (The Shops) - 106,909<br>Sunnyfield - 187,186
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-apr" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (12,962,200)
                    </div>
                    <div class="vertical-rectangle-edc-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,022,100)
                    </div>
                    <div class="vertical-rectangle-scpc-apr" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (16,540,600)
                    </div>
                    <div class="vertical-rectangle-wesm-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (15,461,966)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (30,242,166)
                    </div>
                    <div class="vertical-rectangle-commercial-apr" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,330,890)
                    </div>
                    <div class="vertical-rectangle-intermediate-apr" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (192,821)
                    </div>
                    <div class="vertical-rectangle-power-apr" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (22,142,952)
                    </div>
                    <div class="vertical-rectangle-citygovernment-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (924,248)
                    </div>
                    <div class="vertical-rectangle-othergovernment-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (710,324)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (448,175)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,316,900)
                    </div>
                    <div class="vertical-rectangle-stss-apr" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (1,065,819)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# May 2024
elif tabs == "May 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-may2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-may2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-may2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-may {
            display: block;
            position: absolute;
            top: -53px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-may .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 50.58%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.87%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.33%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 36.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.61%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-stss-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 16.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-may {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 83.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-may2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (39,465,072)
            </div>
            <div class="vertical-rectangle-may2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,741,924)
            </div>
            <div class="vertical-rectangle-may2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (18,246,965)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-may">
                            <div class="arrow"></div>SM Delgado - 451,882<br>SM City - 2,166,781<br>Golden Portals - 595,754<br>QHP - 404,974<br>Mary Mart - 248,199<br>HEVA - 363,478<br>Marriott - 440,699<br>Festive Walk Mall - 660,892<br>Smart Communications - 337,731<br>HEVA ICC - 113,843<br>KAREILA - 220,966<br>One Fintech - 358,314<br>Seda Hotel - 119,053<br>Innove Communications - 191,918<br>Adauge (The Shops) - 116,183<br>Sunnyfield - 218,283<br>Two Fintech - 245,138
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-may" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,230,000)
                    </div>
                    <div class="vertical-rectangle-edc-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,695,000)
                    </div>
                    <div class="vertical-rectangle-scpc-may" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,975,000)
                    </div>
                    <div class="vertical-rectangle-wesm-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (22,299,874)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (32,143,692)
                    </div>
                    <div class="vertical-rectangle-commercial-may" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,635,237)
                    </div>
                    <div class="vertical-rectangle-intermediate-may" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (208,063)
                    </div>
                    <div class="vertical-rectangle-power-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (23,302,909)
                    </div>
                    <div class="vertical-rectangle-citygovernment-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,021,343)
                    </div>
                    <div class="vertical-rectangle-othergovernment-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (806,996)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (434,690)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (4,458,153)
                    </div>
                    <div class="vertical-rectangle-stss-may" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (855,002)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# June 2024
elif tabs == "June 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-jun2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-jun2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-jun2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-jun {
            display: block;
            position: absolute;
            top: -53px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-jun .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 50.58%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.87%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.33%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 36.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.61%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-stss-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 16.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-jun {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 83.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-jun2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (41,305,036)
            </div>
            <div class="vertical-rectangle-jun2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (15,483,608)
            </div>
            <div class="vertical-rectangle-jun2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (19,838,057)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-jun">
                            <div class="arrow"></div>SM Delgado - 498,748<br>SM City - 2,354,727<br>Golden Portals - 551,244<br>QHP - 425,955<br>Mary Mart - 278,924<br>HEVA - 394,472<br>Marriott - 469,620<br>Festive Walk Mall - 718,441<br>Smart Communications - 327,853<br>HEVA ICC - 126,367<br>KAREILA - 225,506<br>One Fintech - 392,809<br>Seda Hotel - 121,354<br>Innove Communications - 188,774<br>Adauge (The Shops) - 121,735<br>Sunnyfield - 224,792<br>Two Fintech - 378,828
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-jun" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,825,000)
                    </div>
                    <div class="vertical-rectangle-kspc-jun" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,200,000)
                    </div>
                    <div class="vertical-rectangle-edc-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,692,000)
                    </div>
                    <div class="vertical-rectangle-wesm-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (27,109,551)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (27,326,241)
                    </div>
                    <div class="vertical-rectangle-commercial-jun" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,017,783)
                    </div>
                    <div class="vertical-rectangle-intermediate-jun" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (182,714)
                    </div>
                    <div class="vertical-rectangle-power-jun" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (21,749,431)
                    </div>
                    <div class="vertical-rectangle-citygovernment-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (875,200)
                    </div>
                    <div class="vertical-rectangle-othergovernment-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (732,954)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (434,829)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,398,984)
                    </div>
                    <div class="vertical-rectangle-stss-jun" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (691,715)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# July 2024
elif tabs == "July 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-jul2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-jul2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-jul2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-jul {
            display: block;
            position: absolute;
            top: -53px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-jul .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 47.95%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 9.12%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.31%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 39.01%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-othergovernment-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.77%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 21.23%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-jul {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 78.77%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-jul2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (36,302,166)
            </div>
            <div class="vertical-rectangle-jul2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,100,097)
            </div>
            <div class="vertical-rectangle-jul2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,651,831)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-jul">
                            <div class="arrow"></div>SM Delgado - 487,208<br>SM City - 2,402,620<br>Golden Portals - 566,921<br>QHP - 435,601<br>Mary Mart - 283,328<br>HEVA - 404,338<br>Marriott - 438,771<br>Festive Walk Mall - 692,681<br>Smart Communications - 324,408<br>HEVA ICC - 181,363<br>KAREILA - 230,556<br>One Fintech - 339,034<br>Seda Hotel - 117,790<br>Innove Communications - 189,532<br>Adauge (The Shops) - 112,040<br>Sunnyfield - 203,348<br>Two Fintech - 333,356
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-jul" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (18,125,000)
                    </div>
                    <div class="vertical-rectangle-kspc-jul" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (14,500,000)
                    </div>
                    <div class="vertical-rectangle-edc-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,678,000)
                    </div>
                    <div class="vertical-rectangle-wesm-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (18,008,199)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (25,719,097)
                    </div>
                    <div class="vertical-rectangle-commercial-jul" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,892,858)
                    </div>
                    <div class="vertical-rectangle-intermediate-jul" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (168,171)
                    </div>
                    <div class="vertical-rectangle-power-jul" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (20,922,838)
                    </div>
                    <div class="vertical-rectangle-citygovernment-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (836,197)
                    </div>
                    <div class="vertical-rectangle-othergovernment-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (680,647)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (412,060)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,092,143)
                    </div>
                    <div class="vertical-rectangle-stss-jul" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (563,739)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# August 2024
# with tab8:
elif tabs == "August 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-aug2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-aug2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-aug2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-aug {
            display: block;
            position: absolute;
            top: -53px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-aug .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 48.68%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.86%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 37.98%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.50%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-stss-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 40.33%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-aug {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 59.67%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-aug2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (34,147,315)
            </div>
            <div class="vertical-rectangle-aug2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,171,900)
            </div>
            <div class="vertical-rectangle-aug2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,389,707)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-aug">
                            <div class="arrow"></div>SM Delgado - 462,079<br>SM City - 2,353,111<br>Golden Portals - 521,017<br>QHP - 403,050<br>Mary Mart - 269,805<br>HEVA - 401,757<br>Marriott - 430,391<br>Festive Walk Mall - 731,992<br>Smart Communications - 324,970<br>HEVA ICC - 156,644<br>KAREILA - 222,950<br>One Fintech - 326,749<br>Seda Hotel - 105,723<br>Innove Communications - 184,324<br>Adauge (The Shops) - 109,197<br>Sunnyfield - 194,022<br>Two Fintech - 321,409
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-aug" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,487,500)
                    </div>
                    <div class="vertical-rectangle-kspc-aug" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,990,000)
                    </div>
                    <div class="vertical-rectangle-edc-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (10,002,500)
                    </div>
                    <div class="vertical-rectangle-wesm-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (14,709,732)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (27,699,354)
                    </div>
                    <div class="vertical-rectangle-commercial-aug" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,041,468)
                    </div>
                    <div class="vertical-rectangle-intermediate-aug" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (182,203)
                    </div>
                    <div class="vertical-rectangle-power-aug" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (21,610,325)
                    </div>
                    <div class="vertical-rectangle-citygovernment-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,084,803)
                    </div>
                    <div class="vertical-rectangle-othergovernment-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (854,535)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (430,198)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (2,701,268)
                    </div>
                    <div class="vertical-rectangle-stss-aug" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (1,825,939)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# September 2024
# with tab9:
elif tabs == "September 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-sep2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-sep2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-sep2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-sep {
            display: block;
            position: absolute;
            top: -53px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-sep .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 47.36%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 38.97%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.87%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-citystreetlights-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.97%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 82.99%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-sep {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 17.01%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-sep2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (36,781,635)
            </div>
            <div class="vertical-rectangle-sep2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,577,080)
            </div>
            <div class="vertical-rectangle-sep2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,926,645)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-sep">
                            <div class="arrow"></div>SM Delgado - 499,415<br>SM City - 2,514,803<br>Golden Portals - 595,414<br>QHP - 417,255<br>Mary Mart - 283,283<br>HEVA - 412,157<br>Marriott - 418,028<br>Festive Walk Mall - 699,974<br>Smart Communications - 344,200<br>HEVA ICC - 139,041<br>KAREILA - 221,593<br>One Fintech - 347,894<br>Seda Hotel - 115,010<br>Innove Communications - 193,378<br>Adauge (The Shops) - 116,084<br>Sunnyfield - 217,471<br>Two Fintech - 346,897<br>Festive Walk 2 - 99,881
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-sep" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (17,275,000)
                    </div>
                    <div class="vertical-rectangle-kspc-sep" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,450,000)
                    </div>
                    <div class="vertical-rectangle-edc-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,674,000)
                    </div>
                    <div class="vertical-rectangle-wesm-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (20,904,582)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (25,836,637)
                    </div>
                    <div class="vertical-rectangle-commercial-sep" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,860,307)
                    </div>
                    <div class="vertical-rectangle-intermediate-sep" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (171,989)
                    </div>
                    <div class="vertical-rectangle-power-sep" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (21,259,541)
                    </div>
                    <div class="vertical-rectangle-citygovernment-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,020,489)
                    </div>
                    <div class="vertical-rectangle-othergovernment-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (881,758)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (526,798)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (596,899)
                    </div>
                    <div class="vertical-rectangle-stss-sep" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (2,912,053)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# October 2024
elif tabs == "October 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-oct2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-oct2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-oct2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-oct {
            display: block;
            position: absolute;
            top: -53px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-oct .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 47.44%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 8.89%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 38.88%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 2.03%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.65%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citystreetlights-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.79%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 10.27%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-oct {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 89.73%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-oct2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,423,892)
            </div>
            <div class="vertical-rectangle-oct2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (13,681,823)
            </div>
            <div class="vertical-rectangle-oct2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,898,261)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-oct">
                            <div class="arrow"></div>SM Delgado - 495,935<br>SM City - 2,447,375<br>Golden Portals - 572,551<br>QHP - 409,942<br>Mary Mart - 278,523<br>HEVA - 407,636<br>Marriott - 393,030<br>Festive Walk Mall - 648,333<br>Smart Communications - 344,777<br>HEVA ICC - 141,546<br>KAREILA - 230,704<br>One Fintech - 344,818<br>Seda Hotel - 122,471<br>Innove Communications - 190,941<br>Adauge (The Shops) - 108,446<br>Sunnyfield - 212,502<br>Two Fintech - 337,632<br>Festive Walk 2 - 270,841
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-oct" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (16,325,000)
                    </div>
                    <div class="vertical-rectangle-kspc-oct" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (13,300,000)
                    </div>
                    <div class="vertical-rectangle-edc-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,673,000)
                    </div>
                    <div class="vertical-rectangle-wesm-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (18,747,975)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (26,039,704)
                    </div>
                    <div class="vertical-rectangle-commercial-oct" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (4,880,754)
                    </div>
                    <div class="vertical-rectangle-intermediate-oct" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (172,949)
                    </div>
                    <div class="vertical-rectangle-power-oct" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (21,345,716)
                    </div>
                    <div class="vertical-rectangle-citygovernment-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,112,136)
                    </div>
                    <div class="vertical-rectangle-othergovernment-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (907,607)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (435,889)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,278,701)
                    </div>
                    <div class="vertical-rectangle-stss-oct" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (375,299)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# November 2024
elif tabs == "November 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .vertical-rectangle-nov2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-3rd-column-2 {
            width: 175px;  /* Set the width of the rectangle */
            height: 175px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-nov2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-nov2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-3rd-column {
            width: 175px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
            margin-bottom: 100px;
        }
        .tooltip-nov {
            display: block;
            position: absolute;
            top: -58px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-nov .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-scpc-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-residential-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 48.07%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-commercial-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 9.09%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-intermediate-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.32%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-power-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 38.19%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-citygovernment-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 1.91%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-othergovernment-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
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
        }
        .vertical-rectangle-citystreetlights-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 0.79%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
        .vertical-rectangle-stss-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 22.86%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;    
        }
        .vertical-rectangle-feeder-nov {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 175px;
            height: 77.14%;
            top: 0;
            left: 0;
            display: flex;
            font-size: 12px;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 0 !important; /* Remove rectangle margin */
            box-sizing: border-box; /* Ensure consistent sizing */
            z-index: 10;
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-nov2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,213,673)
            </div>
            <div class="vertical-rectangle-nov2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,381,906)
            </div>
            <div class="vertical-rectangle-nov2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (16,647,499)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-nov">
                            <div class="arrow"></div>SM Delgado - 412,418<br>SM Delgado - 460,159<br>SM City - 2,370,681<br>Golden Portals - 583,385<br>QHP - 406,496<br>Mary Mart - 252,063<br>HEVA - 392,500<br>Marriott - 430,235<br>Festive Walk Mall - 651,642<br>Smart Communications - 340,873<br>HEVA ICC - 139,782<br>KAREILA - 221,555<br>One Fintech - 346,065<br>Seda Hotel - 122,340<br>Innove Communications - 183,604<br>Adauge (The Shops) - 108,707<br>Sunnyfield - 214,031<br>Two Fintech - 332,917<br>Festive Walk 2 - 265,430
                        </div>
                    </div>
                    <div class="vertical-rectangle-scpc-nov" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (15,100,000)
                    </div>
                    <div class="vertical-rectangle-kspc-nov" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (12,100,000)
                    </div>
                    <div class="vertical-rectangle-edc-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,360,000)
                    </div>
                    <div class="vertical-rectangle-wesm-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (21,860,612)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("Sales")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-3rd-column">
                    <div class="vertical-rectangle-residential-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Residential (26,621,291)
                    </div>
                    <div class="vertical-rectangle-commercial-nov" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        Commercial (5,034,110)
                    </div>
                    <div class="vertical-rectangle-intermediate-nov" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Intermediate (174,857)
                    </div>
                    <div class="vertical-rectangle-power-nov" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Power (21,147,490)
                    </div>
                    <div class="vertical-rectangle-citygovernment-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Govt. (1,060,257)
                    </div>
                    <div class="vertical-rectangle-othergovernment-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        Other Govt. (902,769)
                    </div>
                    <div class="vertical-rectangle-citystreetlights-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        City Streetlights (439,117)
                    </div>
                </div>
                <div>System Loss</div>
                <div class="invisible-rectangle-3rd-column-2">
                    <div class="vertical-rectangle-feeder-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_Feeder (3,104,654)
                    </div>
                    <div class="vertical-rectangle-stss-nov" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        DSL_ST+SS, KWH (920,307)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# December 2024
elif tabs == "December 2024":
    # Create the rectangles
    # col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns([1, 1.65, 1, 1])

    with col1:
        st.markdown("Input")
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
        .invisible-rectangle-3rd-column-2 {
            width: 165px;  /* Set the width of the rectangle */
            height: 100px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .vertical-rectangle-dec2024-ilomore01 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-dec2024-sbamore02 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-dec2024-sbamore03 {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .invisible-rectangle-1st-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .invisible-rectangle-2nd-column {
            width: 110px;  /* Set the width of the rectangle */
            height: 530px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
        }
        .tooltip-dec {
            display: block;
            position: absolute;
            top: -58px;
            left: 37%;
            width: 58%;
            margin-left: 10px;
            background-color: #fff;
            color:black;
            padding: 10px;
            border: 1px solid #ddd;
            z-index: 10;
            opacity: 80%;
        }
        .tooltip-dec .arrow {
            position: absolute;
            top: 20%; /* Vertically center the arrow */
            left: -10px; /* Position it to the left of the tooltip box */
            width: 0;
            height: 0;
            border-top: 10px solid transparent; /* Left side of the arrow */
            border-bottom: 10px solid transparent; /* Right side of the arrow */
            border-right: 10px solid #ddd; /* Visible top part of the arrow */
            transform: translateY(-50%); /* Adjust the vertical position */
        }
        .vertical-rectangle-kspc-dec {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-wesm-dec {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-edc-dec {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-pedc-dec {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
        .vertical-rectangle-cc-dec {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
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
        }
    </style>
    <div class="rectangle-container">
        <div class="invisible-rectangle-1st-column">
            <div class="vertical-rectangle-dec2024-ilomore01" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                ILOMORE01-PN1MORE04 (35,206,677)
            </div>
            <div class="vertical-rectangle-dec2024-sbamore02" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                SBAMORE02-ILOMORE01 (14,584,192)
            </div>
            <div class="vertical-rectangle-dec2024-sbamore03" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                SBAMORE03 (17,414,030)
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    with col2:
        st.markdown("Purchase")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="invisible-rectangle-2nd-column">
                    <div class="vertical-rectangle-cc-dec" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        Contestables
                        <div class="tooltip-dec">
                            <div class="arrow"></div>SM Delgado - 467,927<br>SM City - 2,395,474<br>Golden Portals - 597,285<br>QHP - 416,100<br>Mary Mart - 248,980<br>HEVA - 389,432<br>Marriott - 436,659<br>Festive Walk Mall - 667,290<br>Smart Communications - 350,653<br>HEVA ICC - 131,164<br>KAREILA - 225,575<br>One Fintech - 358,438<br>Seda Hotel - 119,322<br>Innove Communications - 190,648<br>Adauge (The Shops) - 109,907<br>Sunnyfield - 219,858<br>Two Fintech - 341,476<br>Festive Walk 2 - 262,334
                        </div>
                    </div>
                    <div class="vertical-rectangle-kspc-dec" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (12,720,000)
                    </div>
                    <div class="vertical-rectangle-edc-dec" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,674,000)
                    </div>
                    <div class="vertical-rectangle-pedc-dec" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        PEDC (5,795,000)
                    </div>
                    <div class="vertical-rectangle-wesm-dec" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                        WESM (31,087,378)
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )