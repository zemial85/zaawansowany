class CustomException(Exception):
    pass

try:
    raise CustomException("ojojojojoj")
except CustomException:
    print("jhkgk")