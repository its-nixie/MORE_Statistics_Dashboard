import streamlit as st

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

# Inject custom CSS to adjust sidebar size
st.markdown("""
    <style>
        .css-1d391kg {
            width: 350px;  /* Set the desired width here */
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("MORE Statistics Dashboard")
tabs = st.sidebar.radio("Months", ["January 2024", "February 2024", "March 2024", "April 2024", "May 2024", "June 2024", "July 2024", "August 2024", "September 2024", "October 2024", "November 2024", "December 2024"], index=0)

# January 2024
if tabs == "January 2024":    
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
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
        .vertical-rectangle-cc-jan {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 110px;
            height: 11.08%;
            top: 0;
            left: 0;
            display: flex;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
                    <div class="vertical-rectangle-cc-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
                    </div>
                    <div class="vertical-rectangle-scpc-jan" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                        SCPC (16,882,500)
                    </div>
                    <div class="vertical-rectangle-kspc-jan" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                        KSPC (11,245,000)
                    </div>
                    <div class="vertical-rectangle-edc-jan" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        EDC (9,360,000)
                    </div>
                    <div class="vertical-rectangle-wesm-jan" onclick="fetch('/?rect=4').then(() => window.location.reload())">
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
            </div>
            """,
            unsafe_allow_html=True
        )

# February 2024
elif tabs == "February 2024": 
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)
    
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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
                    <div class="vertical-rectangle-cc-feb" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                        Contestables
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
            </div>
            """,
            unsafe_allow_html=True
        )

# March 2024
elif tabs == "March 2024": 
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
        .vertical-rectangle-residential-mar {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 2px solid #ccc;
            font-weight: bold;
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# April 2024
elif tabs == "April 2024": 
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;
            height: 300px;
            background-color: white;
            border: 1px solid transparent;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# May 2024
elif tabs == "May 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# June 2024
elif tabs == "June 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# July 2024
elif tabs == "July 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# August 2024
# with tab8:
elif tabs == "August 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# September 2024
# with tab9:
elif tabs == "September 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# October 2024
elif tabs == "October 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# November 2024
elif tabs == "November 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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
            width: 165px;  /* Set the width of the rectangle */
            height: 300px; /* Set the height of the rectangle */
            background-color: white; /* Make the rectangle invisible */
            border: 1px solid transparent; /* Optional: Add a border (invisible here) */
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            width: 165px;
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
            </div>
            """,
            unsafe_allow_html=True
        )

# December 2024
elif tabs == "December 2024":
    # Create the rectangles
    col1, col2, col3, col4 = st.columns(4)

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