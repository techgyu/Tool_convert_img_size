# Tool_convert_img_size

이미지 파일을 지정한 최대 용량(예: 1MB) 이하로, 비율을 유지하며 자동으로 리사이즈 및 압축해주는 Python 도구입니다.

## 주요 기능
- input_images 폴더의 모든 이미지를 output_resized_images 폴더로 일괄 변환
- 이미지 비율 유지
- JPEG 압축 품질을 자동 조정해 목표 파일 크기(예: 1MB)에 최대한 가깝게 저장
- 최대 해상도 제한 가능
- 설정 파일(settings.py)로 간편하게 옵션 변경

## 설치 방법
```bash
pip install -r requirements.txt
```

## 사용법
1. `input_images` 폴더에 변환할 이미지를 넣으세요 (jpg, jpeg, png 지원)
2. `settings.py`에서 옵션(목표 용량, 최대 해상도 등) 필요시 수정
3. 아래 명령어로 실행
```bash
python main.py
```
4. 변환된 이미지는 `output_resized_images` 폴더에 저장됩니다

## settings.py 예시
```python
input_dir = 'input_images'  # 원본 이미지 디렉토리
output_dir = 'output_resized_images'  # 리사이즈된 이미지 저장 디렉토리
target_filesize = 1048576  # 목표 파일 크기 (byte), 예: 1MB
max_size = (4096, 4096)  # 최대 이미지 크기 (가로, 세로)
min_quality = 20  # 최소 허용 품질
```

## 디렉토리 구조 예시
```
Tool_convert_img_size/
├── input_images/
│   └── sample.jpg
├── output_resized_images/
├── main.py
├── settings.py
├── requirements.txt
└── README.md
```

## 참고
- PNG 등 비손실 포맷도 JPEG로 저장됩니다 (용량 제한 목적)
- 원본 파일은 변경되지 않습니다

---
문의 및 개선 제안은 언제든 환영합니다!