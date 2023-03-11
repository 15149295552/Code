import base64

# test_str = "abcdef"

img_file = "d:\\tmp2\\t1.jpg"
with open(img_file, "rb") as f:
    img_data = f.read()


base64_str = base64.b64encode(img_data)
print("base64_str:", base64_str)

# decode_str =base64.b64decode(base64_str)
# print("decode_str:", decode_str)

