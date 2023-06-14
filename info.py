import streamlit as st
import pandas as pd
import pip
#vs코드 내에선 실행을 위해 pip install streamlit 이 선행되어야한다.
#vs코드 내의 시험 구동은 streamlit run info.py 사용
# github등을 이용한 외부 연결시 외부링크 사용가능

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
install('openpyxl') #execl파일을 읽기 위해 pip 를 실행하는 코드
install('streamlit')

view = [100.150,50]#웹 초기 크기 설정
st.title('슈키백과') #제목

st.text('슈니들을 위한 정보제공서비스') # 작은 글씨

#st.header('이 영역은 헤더 영역')  # 제목같은 큰 글씨
#st.subheader('이 영역은 subheader영역')

def main() :
        col = st.columns((1,2,3,4,5))[4]  #버튼이 소실 되는 문제를 해결하기 위한 초기화 버튼 위치조정
        clicked = col.button("초기화")
      # adjust to taste, possibly using floats
        st.markdown("----", unsafe_allow_html=True)#선을 그어 구분

        if st.button('편의시설') :
            df = pd.read_excel('편의시설 영업시간.xlsx')
            st.table(df)
        elif st.button('도서관') :
            df = pd.read_excel('도서관.xlsx')
            st.table(df)

if __name__ == "__main__" :
    main()
