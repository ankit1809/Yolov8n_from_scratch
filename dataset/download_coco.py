import os
import zipfile
import urllib.request
 
def download_coco128(save_path="dataset"):
    url = "https://ultralytics.com/assets/coco128.zip"
    zip_path = os.path.join(save_path, "coco128.zip")
 
    os.makedirs(save_path, exist_ok=True)
 
    print("📥 Downloading COCO128 dataset...")
    urllib.request.urlretrieve(url, zip_path)
 
    print("📦 Extracting...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(save_path)
 
    os.remove(zip_path)
    print("✅ COCO128 dataset ready at:", os.path.join(save_path, "coco128"))
 
if __name__ == "__main__":
    download_coco128()