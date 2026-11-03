# GitHub에 수동으로 올리기

이 폴더 자체가 저장소의 최상위입니다. GitHub에서 새 **Public** 저장소를 만들고, README·.gitignore·라이선스 자동 생성은 선택하지 않아 빈 저장소로 둡니다. 이미 파일이 있는 저장소라면 기존 이력과 합치는 방법이 달라집니다.

터미널에서 다음을 순서대로 실행하세요. 첫 블록의 경로는 실제 폴더 경로로, 두 번째 블록의 `YOUR_GITHUB_USERNAME`과 `open-RPGFXS`는 실제 GitHub 사용자명과 저장소 이름으로 바꾸세요.

```sh
cd /path/to/OPEN-RPGFXS
python3 tools/validate.py
git init -b main
git add .
git status
git commit -m "Publish OPEN-RPGFXS under CC0"
```

```sh
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/open-RPGFXS.git
git push -u origin main
```

`git status`에서 LICENSE, README, sample과 에셋 폴더가 추가되는지 확인하세요. `.gitignore`는 macOS의 `.DS_Store`와 Python 캐시를 제외합니다. HTTPS 로그인 과정에서 인증을 요청하면 GitHub의 인증 절차를 따르세요. Git이 작성자 정보를 요구하면 자신의 `user.name`과 `user.email`을 설정한 후 커밋을 다시 실행하면 됩니다.

푸시 후 저장소 첫 화면에서 README의 GIF 5개, 각 MP4 링크, CC0 LICENSE와 개별 PNG·WAV 링크를 확인하세요. MP4는 GitHub 화면에서 열리지 않는 환경이라면 내려받아 재생할 수 있습니다. 이 저장소에는 전체 에셋이 들어 있으므로 별도 Release를 만들 필요는 없습니다.
