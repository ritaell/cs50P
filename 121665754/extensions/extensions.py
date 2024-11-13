file = input("File name:").lower().strip().rstrip()

if "." in file:

    if file.rfind("gif") != -1:
      print("image/gif")

    elif file.rfind("png") != -1:
      print("image/png")

    elif file.rfind("jpg") != -1:
      print("image/jpeg")

    elif file.rfind("jpeg") != -1:
      print("image/jpeg")

    elif file.rfind("pdf") != -1:
      print("application/pdf")

    elif file.rfind("zip") != -1:
      print("application/zip")

    elif file.rfind("txt") != -1:
      print("text/plain")

    else:
      print("application/octet-stream")

else:
  print("application/octet-stream")



