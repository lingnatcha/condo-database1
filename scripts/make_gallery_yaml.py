import os, sys

if len(sys.argv) < 2:
    print("Usage: python make_gallery_yaml.py <PROPERTY_ID>")
    sys.exit(1)

prop_id = sys.argv[1]
base_dir = f"images/upload/listings/{prop_id}"
public_base = f"/{base_dir}"

# นามสกุลรูปที่ยอมรับ
exts = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

try:
    files = sorted(f for f in os.listdir(base_dir)
                   if os.path.splitext(f.lower())[1] in exts)
except FileNotFoundError:
    print(f"Folder not found: {base_dir}")
    sys.exit(1)

print("images:")
for f in files:
    print(f"  - image: {public_base}/{f}")
    # ถ้าอยากเติม caption/alt อัตโนมัติจากชื่อไฟล์ ให้ uncomment 2 บรรทัดล่าง
    # name = os.path.splitext(f)[0].replace('-', ' ').replace('_', ' ').title()
    # print(f"    caption: \"{name}\"")
