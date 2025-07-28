# 이미지 리사이즈 설정 파일
input_dir = 'input_images'  # 원본 이미지 디렉토리
output_dir = 'output_resized_images'  # 리사이즈된 이미지 저장 디렉토리
target_filesize = 1048576  # 목표 파일 크기 (byte), 예: 1MB
max_size = (4096, 4096)  # 최대 이미지 크기 (가로, 세로)
min_quality = 20  # 최소 허용 품질
# 파일명 패턴 예시: input_images/abc.jpg -> output_resized_images/abc.jpg
