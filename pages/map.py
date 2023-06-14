import streamlit as st
import pip


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
install('streamlit-folium') #pip install streamlit-folium 으로 대체가능
install('follium')

from streamlit_folium import st_folium
import folium

view = [100.150,50]
st.title('슈키백과')

st.text('슈니들을 위한 정보제공서비스') # 작은 글씨

st.markdown("----", unsafe_allow_html=True)

loca = ['편의점','입구']
choice = st.sidebar.selectbox('location', loca)

if choice == loca[0] :
    center = [37.628894, 127.090414]
    m=folium.Map(location = center, zoom_start = 18)
    folium.Marker(location =[37.626363,127.092861], popup ="50주년CU").add_to(m)
    folium.Marker(location =[37.627693,127.092310], popup ="인사관 GS25").add_to(m)
    folium.Marker(location =[37.62871,127.0903745], popup ="누리관매점").add_to(m)
    folium.Marker(location =[37.6289458, 127.0888736], popup ="샬롬 세븐일레븐").add_to(m)
    st_data = st_folium(m, width =800)

elif choice == loca[1] :
    center = [37.628894, 127.090414]
    m=folium.Map(location = center, zoom_start = 21)
    folium.Marker(location =[37.628349,127.090865], popup ="도서관2층입구").add_to(m)
    folium.Marker(location =[37.628295,127.091418], popup ="도서관1층입구").add_to(m)
    folium.Marker(location =[37.628437,127.090479], popup ="누리관지하입구").add_to(m)
    folium.Marker(location =[37.628722,127.090139], popup ="누리관1층입구").add_to(m)
    folium.Marker(location =[37.625933,127.093238], popup ="50주년입구 1").add_to(m)
    folium.Marker(location =[37.626616,127.093101], popup ="50주년 입구 2").add_to(m)
    folium.Marker(location =[37.627699,127.092305], popup ="인사관입구 1").add_to(m)
    folium.Marker(location =[37.628428,127.092319], popup ="인사관입구 2").add_to(m)
    folium.Marker(location =[37.628024,127.092474], popup ="인사관입구 3").add_to(m)
    folium.Marker(location =[37.628890,127.088454], popup ="샬롬 입구 1").add_to(m)
    folium.Marker(location =[37.628838,127.088926], popup ="샬롬 입구 2").add_to(m)
    st_data = st_folium(m, width =800)

