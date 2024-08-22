# 5jeong-llm-bot
LLM chat Bot to use CrewAI

## 1. 프로젝트 세팅

- VSC
- GitHub 연동

## 2. 프로젝트 구성
- 가상환경을 설정 => Docker Container 개념( 공간을 분리해서 따로 관리)
- python 3.8 열심히 개발 -> 근데 우리가 배포할 서버가 3.3 버전의 파이썬이면
  - 3.8 함수를 썼다면 3.3에는 없는 함수 -> 오류 -> 배포하고나서 알게됨
  - 로컬에서 작업하는 환경과 호스트 서버에서 작업하는 환경을 일치시켜 주기 위함
  - Docker(가상 머신) 활용 // 지금은 venv 모듈을 사용해서 환경 설정을 해보자!



> python3.10 -m venv .venv 


project based learning

> .venv/Scripts/activate

## 3. 프로젝트

### 3-1. Ollma 모델

(1). ollama 다운로드

(2). ollama를 통해서 llm 다운로드

> ollama pull phi3:3.8b

> ollama run phi3:3.8b

(3). CrewAI 설치
> pip install crewai crewai-tools
> pip install -U langchain-ollama
### 3.2 Flask 사용해서 기본적인 챗봇만들기
