import streamlit as st
import PyPDF2

# PDF에서 텍스트 추출 함수
@st.cache_data
def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

# 🎯 페이지 타이틀
st.title("📘 교원의 학생생활지도 방식 FAQ")

# PDF 업로드
uploaded_file = st.file_uploader("📄 PDF 파일을 업로드하세요", type="pdf")

# 라디오 버튼으로 유형 선택
options = ["조언", "상담", "주의", "훈육", "훈계", "보상"]
selected_option = st.radio("🔍 검색할 유형을 선택하세요", options)

# PDF가 업로드되었을 경우 처리
if uploaded_file:
    pdf_text = extract_pdf_text(uploaded_file)

    # 검색 버튼
    if st.button("검색"):
        sentences = [s.strip() for s in pdf_text.split('.') if selected_option in s]
        
        if sentences:
            st.markdown(f"### ✅ [{selected_option}] 관련 내용:")
            for s in sentences[:5]:
                st.markdown(f"- {s}.")
        else:
            st.warning("❗ 관련 내용을 찾을 수 없습니다.")
else:
    st.info("좌측 사이드바에서 PDF 파일을 업로드해주세요.")
    


