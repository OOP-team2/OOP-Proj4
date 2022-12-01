## 2022-2 OOP 팀1 4번째 프로젝트입니다.
---
콘솔로 섯다 게임을 만듭니다.
파이썬으로 프로그래밍 후 윈도우즈 OS(x64) 실행 파일로 컴파일합니다.

모델 레이어와 서비스 레이어를 분리했습니다.
- 모델 레이어: 플레이어나 카드 등 기본적인 엔티티를 반영하는 클래스를 포함합니다.
- 서비스 레이어: 모델을 가지고 로직을 실햏하는 클래스를 포함합니다.

### 실행 방법
1. 먼저 가상 환경을 활성화해야합니다.
    - [여기](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)를 참고해서 __.venv/bin/__ 폴더 안에 _activate_ 라는 파일을 실행하면 됩니다.
2. 그 다음 __main.py__ 를 실행하면 메인 함수가 실행됩니다.
3. 할 일이 다 끝나면 __deactivate__ 를 입력해서 가상환경을 비활성화합니다.

### 참고자료
게임을 만들기 위한 참고자료
- [도트 아트 만들기](https://snskeyboard.com/dotart/)  
- [섯다 게임 방법](http://gostop.hangame.com/gameGuide/gssudda/guide_gssudda01_01.html)
- [C++ 섯다 프로그램](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=shenote&logNo=220453482685)

컴파일을 위한 참고자료
- [py2exe](https://www.py2exe.org/)