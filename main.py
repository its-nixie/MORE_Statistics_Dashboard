# Necessary imports
import streamlit as st

st.set_page_config(page_title="Statistics Dashboard", page_icon="more_power_logo.png")

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

	.stTabs [data-baseweb="tab-list"] {
		gap: 13px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #000000;
		border-radius: 4px 4px 0px 0px;
		gap: 5px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
        color: #6A7FDB;
        font-weight: bold;
	}

    /* Change text color when tab is hovered */
    .stTabs [data-baseweb="tab"]:hover {
        color: #6A7FDB;  /* Change this to your desired color */
    }
    
</style>""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["01/2024", "02/2024", "03/2024", "04/2024", "05/2024", "06/2024", "07/2024", "08/2024", "09/2024", "10/2024", "11/2024", "12/2024"])

# January 2024
with tab1:

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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: white !important;;
            padding: 10px;
            border: 1px solid #ccc;
            font-weight: bold;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (32,109,152)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (13,817,384)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (17,182,011)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (11,245,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,360,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (16,882,500)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (18,628,682)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (133,622)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .vertical-rectangle-col3 {{
            width: 100px;
            height: 70px;
            background-color: #B56F76;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .vertical-rectangle-col3-v2 {{
            width: 100px;
            height: 70px;
            background-color: #84B067;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .vertical-rectangle-col3:hover {{
            background-color: #B56F76;
            color: #000;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
        }}
        .vertical-rectangle-col3-v2:hover {{
            background-color: #84B067;
            color: #000;
            transform: scale(1.05);
            transition: background-color 0.3s, transform 0.3s;
        }}
        .tooltip-col3-first {{
            display: block;
            background-color: #B56F76;
            color: #fff;
            text-align: left;
            border-radius: 5px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            left: 110%; /* Position the tooltip to the right of the rectangle */
            top: 50%;
            transform: translateY(-50%);
            margin-left: 10px; /* Add space between the rectangle and the tooltip */
            opacity: 1;
            width: 200px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-size: 10px;
        }}

        .tooltip-col3-second {{
            display: block;
            background-color: #84B067;
            color: #fff;
            text-align: left;
            border-radius: 5px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            left: 110%; /* Position the tooltip to the right of the rectangle */
            top: 50%;
            transform: translateY(-50%);
            margin-left: 10px; /* Add space between the rectangle and the tooltip */
            opacity: 1;
            width: 200px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-size: 10px;
        }}
    
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 48,462,295 
        </div>
        <div class="vertical-rectangle-col3" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado -  464,921<br>SM City - 2,381,612<br>Golden Portals -  634,825<br>QHP -  395,239<br>Mary Mart -  275,059<br>HEVA -  414,681<br>Marriott -  419,552<br>Festive Walk Mall -  655,735<br>Smart Communications -  326,431<br>HEVA ICC -  125,321<br>KAREILA -  214,966<br>One Fintech -  298,937<br>Seda Hotel -  119,976<br>Innove Communications -  179,489<br>Adauge (The Shops) -  85,622</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (7.21%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (1.28%)<br>DSL_Feeder (5.93%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.65%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# February 2024
with tab2:
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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (30,039,371)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (12,737,984)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (16,203,712)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (14,151,400)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,372,300)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (17,790,400)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (11,293,125)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (138,552)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 49,036,876  
        </div>
        <div class="vertical-rectangle-col3" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 412,418<br>SM City - 2,133,582<br>Golden Portals - 517,279<br>QHP - 373,970<br>Mary Mart - 242,663<br>HEVA - 372,596<br>Marriott - 283,046<br>Festive Walk Mall - 624,995<br>Smart Communications - 316,744<br>HEVA ICC - 116,031<br>KAREILA - 200,944<br>One Fintech - 410,240<br>Seda Hotel - 110,157<br>Innove Communications - 174,634<br>Adauge (The Shops) - 84,544</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (6.14%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (1.37%)<br>DSL_Feeder (4.76%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.46%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# March 2024
with tab3:
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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (30,315,442)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (13,023,080)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (16,096,277)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (13,535,500)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,579,400)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (17,698,200)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (11,735,138)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (165,551)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .vertical-rectangle-col3-march {{
            width: 100px;
            height: 70px;
            background-color: #B56F76;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 90px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 53,006,149 
        </div>
        <div class="vertical-rectangle-col3-march" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 419,025<br>SM City - 2,133,598<br>Golden Portals - 682,832<br>QHP - 377,284<br>Mary Mart - 237,082<br>HEVA - 401,585<br>Marriott - 448,332<br>Festive Walk Mall - 634,036<br>Smart Communications - 333,804<br>HEVA ICC - 132,857<br>KAREILA - 208,988<br>One Fintech - 288,040<br>Seda Hotel - 114,442<br>Innove Communications - 185,419<br>Adauge (The Shops) - 102,167<br>Sunnyfield - 187,073</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (1.93%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (1.34%)<br>DSL_Feeder (0.58%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.50%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# April 2024
with tab4:
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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (32,290,271)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (12,939,584)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (15,262,642)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (12,962,200)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,022,100)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (16,540,600)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (15,461,966)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (210,662)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 59,991,576 
        </div>
        <div class="vertical-rectangle-col3-march" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 404,103<br>SM City - 2,050,316<br>Golden Portals - 611,192<br>QHP - 360,829<br>Mary Mart - 224,742<br>HEVA - 362,058<br>Marriott - 396,130<br>Festive Walk Mall - 594,367<br>Smart Communications - 314,155<br>HEVA ICC - 110,785<br>KAREILA - 210,198<br>One Fintech - 289,569<br>Seda Hotel - 107,910<br>Innove Communications - 175,184<br>Adauge (The Shops) - 106,909<br>Sunnyfield - 187,186</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (6.12%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (1.49%)<br>DSL_Feeder (4.63%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.44%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# May 2024
with tab5:
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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (39,465,072)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (13,741,924)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (18,246,965)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (14,230,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,695,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (17,975,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (22,299,874)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (195,731)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .vertical-rectangle-col3-may {{
            width: 100px;
            height: 70px;
            background-color: #B56F76;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 98px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 63,552,930 
        </div>
        <div class="vertical-rectangle-col3-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 451,882<br>SM City - 2,166,781<br>Golden Portals - 595,754<br>QHP - 404,974<br>Mary Mart - 248,199<br>HEVA - 363,478<br>Marriott - 440,699<br>Festive Walk Mall - 660,892<br>Smart Communications - 337,731<br>HEVA ICC - 113,843<br>KAREILA - 220,966<br>One Fintech - 358,314<br>Seda Hotel - 119,053<br>Innove Communications - 191,918<br>Adauge (The Shops) - 116,183<br>Sunnyfield - 218,283<br>Two Fintech - 245,138</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (6.92%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (1.11%)<br>DSL_Feeder (5.81%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.70%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# June 2024
with tab6:
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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (41,305,036)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (15,483,608)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (19,838,057)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (14,200,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,692,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (17,825,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (27,109,551)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (161,508)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 56,319,151 
        </div>
        <div class="vertical-rectangle-col3-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 498,748<br>SM City - 2,354,727<br>Golden Portals - 551,244<br>QHP - 425,955<br>Mary Mart - 278,924<br>HEVA - 394,472<br>Marriott - 469,620<br>Festive Walk Mall - 718,441<br>Smart Communications - 327,853<br>HEVA ICC - 126,367<br>KAREILA - 225,506<br>One Fintech - 392,809<br>Seda Hotel - 121,354<br>Innove Communications - 188,774<br>Adauge (The Shops) - 121,735<br>Sunnyfield - 224,792<br>Two Fintech - 378,828</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (6.00%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (1.01%)<br>DSL_Feeder (4.98%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.73%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# July 2024
with tab7:
    # Create the rectangles
    col1, col2, col3, col4, col5, col6 = st.columns(6)

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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (36,302,166)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (14,100,097)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (17,651,831)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (14,500,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,678,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (18,125,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (18,008,199)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (142,344)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 53,631,867 
        </div>
        <div class="vertical-rectangle-col3-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 487,208<br>SM City - 2,402,620<br>Golden Portals - 566,921<br>QHP - 435,601<br>Mary Mart - 283,328<br>HEVA - 404,338<br>Marriott - 438,771<br>Festive Walk Mall - 692,681<br>Smart Communications - 324,408<br>HEVA ICC - 181,363<br>KAREILA - 230,556<br>One Fintech - 339,034<br>Seda Hotel - 117,790<br>Innove Communications - 189,532<br>Adauge (The Shops) - 112,040<br>Sunnyfield - 203,348<br>Two Fintech - 333,356</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (4.16%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (0.88%)<br>DSL_Feeder (3.28%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.69%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    # Number of Customers (Residential)
    with col6:
        st.markdown("‎ ")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Number of Residential Connections (91,418)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# August 2024
with tab8:
    # Create the rectangles
    col1, col2, col3, col4, col5, col6 = st.columns(6)

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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (34,147,315)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (13,171,900)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (16,389,707)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (13,990,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (10,002,500)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (17,487,500)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (14,709,732)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (141,998)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 56,902,886 
        </div>
        <div class="vertical-rectangle-col3-may" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 462,079<br>SM City - 2,353,111<br>Golden Portals - 521,017<br>QHP - 403,050<br>Mary Mart - 269,805<br>HEVA - 401,757<br>Marriott - 430,391<br>Festive Walk Mall - 731,992<br>Smart Communications - 324,970<br>HEVA ICC - 156,644<br>KAREILA - 222,950<br>One Fintech - 326,749<br>Seda Hotel - 105,723<br>Innove Communications - 184,324<br>Adauge (The Shops) - 109,197<br>Sunnyfield - 194,022<br>Two Fintech - 321,409</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (6.52%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (2.63%)<br>DSL_Feeder (3.89%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.74%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    # Number of Customers (Residential)
    with col6:
        st.markdown("‎ ")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Number of Residential Connections (91,645)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# September 2024
with tab9:
    # Create the rectangles
    col1, col2, col3, col4, col5, col6 = st.columns(6)

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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (36,781,635)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (14,577,080)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (17,926,645)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (13,450,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,674,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (17,275,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (20,904,582)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (173,035)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .vertical-rectangle-col3-sept {{
            width: 100px;
            height: 70px;
            background-color: #B56F76;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 107px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 54,557,518 
        </div>
        <div class="vertical-rectangle-col3-sept" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 499,415<br>SM City - 2,514,803<br>Golden Portals - 595,414<br>QHP - 417,255<br>Mary Mart - 283,283<br>HEVA - 412,157<br>Marriott - 418,028<br>Festive Walk Mall - 699,974<br>Smart Communications - 344,200<br>HEVA ICC - 139,041<br>KAREILA - 221,593<br>One Fintech - 347,894<br>Seda Hotel - 115,010<br>Innove Communications - 193,378<br>Adauge (The Shops) - 116,084<br>Sunnyfield - 217,471<br>Two Fintech - 346,897<br>Festive Walk 2 - 99,881</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (5.30%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (0.90%)<br>DSL_Feeder (4.40%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.67%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    # Number of Customers (Residential)
    with col6:
        st.markdown("‎ ")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Number of Residential Connections (92,100)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# October 2024
with tab10:
    # Create the rectangles
    col1, col2, col3, col4, col5, col6 = st.columns(6)

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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (35,423,892)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (13,681,823)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (16,898,261)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (13,300,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,673,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (16,325,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (18,747,975)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (159,735)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 54,894,755   
        </div>
        <div class="vertical-rectangle-col3-sept" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 495,935<br>SM City - 2,447,375<br>Golden Portals - 572,551<br>QHP - 409,942<br>Mary Mart - 278,523<br>HEVA - 407,636<br>Marriott - 393,030<br>Festive Walk Mall - 648,333<br>Smart Communications - 344,777<br>HEVA ICC - 141,546<br>KAREILA - 230,704<br>One Fintech - 344,818<br>Seda Hotel - 122,471<br>Innove Communications - 190,941<br>Adauge (The Shops) - 108,446<br>Sunnyfield - 212,502<br>Two Fintech - 337,632<br>Festive Walk 2 - 270,841</div>
        </div>
        <div class="vertical-rectangle-col3-v2" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Per Cycle SL, % (5.50%)
            <div class="tooltip-col3-second">DSL_ST+SS, % (0.57%)<br>DSL_Feeder (4.94%)</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=4').then(() => window.location.reload())">
            Actual Total SL (5.65%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    # Number of Customers (Residential)
    with col6:
        st.markdown("‎ ")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Number of Residential Connections (92,467)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# November 2024
with tab11:
    # Create the rectangles
    col1, col2, col3, col4, col5, col6 = st.columns(6)

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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (35,213,673)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (14,381,906)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (16,647,499)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (12,100,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,360,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
                    SCPC (15,100,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (21,860,612)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (173,309)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Captive: 55,379,891 
        </div>
        <div class="vertical-rectangle-col3" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-col3-first">SM Delgado - 460,159<br>SM City - 2,370,681<br>Golden Portals - 583,385<br>QHP - 406,496<br>Mary Mart - 252,063<br>HEVA - 392,500<br>Marriott - 430,235<br>Festive Walk Mall - 651,642<br>Smart Communications - 340,873<br>HEVA ICC - 139,782<br>KAREILA - 221,555<br>One Fintech - 346,065<br>Seda Hotel - 122,340<br>Innove Communications - 183,604<br>Adauge (The Shops) - 108,707<br>Sunnyfield - 214,031<br>Two Fintech - 332,917<br>Festive Walk 2 - 265,430</div>
        </div>
        <div class="vertical-rectangle-other" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            Actual Total SL (-3.09%)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
    # Number of Customers (Residential)
    with col6:
        st.markdown("‎ ")
        st.markdown(
            f"""
            <div class="rectangle-container">
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    Number of Residential Connections (93,292)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# December 2024
with tab12:
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
        .vertical-rectangle {
            background-color: #708090; /* Example color */
            color: #F5F5F5 !important;;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100px;
            height: 70px;
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
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            ILOMORE01-PN1MORE04 (35,206,677)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
            SBAMORE02-ILOMORE01 (14,584,192)
        </div>
        <div class="vertical-rectangle" onclick="fetch('/?rect=3').then(() => window.location.reload())">
            SBAMORE03 (17,414,030)
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
                <div class="vertical-rectangle" onclick="fetch('/?rect=1').then(() => window.location.reload())">
                    KSPC (12,720,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    EDC (9,674,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=2').then(() => window.location.reload())">
                    PEDC (5,795,000)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=4').then(() => window.location.reload())">
                    WESM (31,087,378)
                </div>
                <div class="vertical-rectangle" onclick="fetch('/?rect=5').then(() => window.location.reload())">
                    NM (187,070)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Column 3
    with col3:
        st.markdown("‎ ")
        st.markdown(
    f"""
    <style>
        .rectangle-container-col3 {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 20px;
        }}
        .vertical-rectangle-other {{
            width: 100px;
            height: 70px;
            background-color: #708090;
            color: #F5F5F5 !important;;
            border: 1px solid #ccc;
            font-weight: bold;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 12px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            position: relative;
            margin-bottom: 80px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(17, 16, 16, 0.2);
        }}
        .tooltip-dec {{
            display: block;
            background-color: #B56F76;
            color: #fff;
            text-align: left;
            border-radius: 5px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            left: 110%; /* Position the tooltip to the right of the rectangle */
            top: 170%;
            transform: translateY(-50%);
            margin-left: 10px; /* Add space between the rectangle and the tooltip */
            opacity: 1;
            width: 200px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-size: 10px;
        }}
    </style>
    <div class="rectangle-container">
        <div class="vertical-rectangle-col3" onclick="fetch('/?rect=1').then(() => window.location.reload())">
            Contestables
            <div class="tooltip-dec">SM Delgado - 467,927<br>SM City - 2,395,474<br>Golden Portals - 597,285<br>QHP - 416,100<br>Mary Mart - 248,980<br>HEVA - 389,432<br>Marriott - 436,659<br>Festive Walk Mall - 667,290<br>Smart Communications - 350,653<br>HEVA ICC - 131,164<br>KAREILA - 225,575<br>One Fintech - 358,438<br>Seda Hotel - 119,322<br>Innove Communications - 190,648<br>Adauge (The Shops) - 109,907<br>Sunnyfield - 219,858<br>Two Fintech - 341,476<br>Festive Walk 2 - 262,334</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)