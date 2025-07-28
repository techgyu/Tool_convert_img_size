# 파일 크기(바이트) 이하로 이미지 저장 (비율 유지, JPEG 품질 조정)
import os
import io

def resize_to_target_filesize(input_path, output_path, target_filesize, max_size=(4096,4096), min_quality=20):
    """
    input_path: 원본 이미지 경로
    output_path: 저장할 이미지 경로
    target_filesize: 목표 파일 크기 (byte)
    max_size: 최대 이미지 크기 (가로, 세로)
    min_quality: 최소 허용 품질
    """
    with Image.open(input_path) as img:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        low = min_quality
        high = 95
        best_quality = low
        best_data = None
        while low <= high:
            mid = (low + high) // 2
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=mid)
            size = buffer.tell()
            if size <= target_filesize:
                best_quality = mid
                best_data = buffer.getvalue()
                low = mid + 1  # 더 높은 품질 시도
            else:
                high = mid - 1  # 더 낮은 품질 시도
        if best_data:
            with open(output_path, 'wb') as f:
                f.write(best_data)
            return True
        # 최소 품질에도 파일 크기가 크면 마지막 결과 저장
        img.save(output_path, format='JPEG', quality=min_quality)
        return False
from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img.thumbnail(size, Image.Resampling.LANCZOS)  # 비율 유지하며 최대 size로 축소
        img.save(output_path)

# settings.py에서 설정값 import
import settings
import glob
import os

# input_dir의 모든 jpg, jpeg, png 파일 변환
os.makedirs(settings.output_dir, exist_ok=True)
img_exts = ('*.jpg', '*.jpeg', '*.png')
input_files = []
for ext in img_exts:
    input_files.extend(glob.glob(os.path.join(settings.input_dir, ext)))

for input_path in input_files:
    filename = os.path.basename(input_path)
    output_path = os.path.join(settings.output_dir, filename)
    print(f"Resizing {filename} ...")
    resize_to_target_filesize(
        input_path,
        output_path,
        settings.target_filesize,
        max_size=settings.max_size,
        min_quality=settings.min_quality
    )
    print(f"Saved: {output_path}")