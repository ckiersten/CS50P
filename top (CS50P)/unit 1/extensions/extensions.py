def main():
    text = input("File name: ")
    text = text.strip().lower()
    if text.endswith(".gif"):
        print("image/gif")
    elif text.endswith(".png"):
        print("image/png")
    elif text.endswith(".jpg") or text.endswith(".jpeg"):
        print("image/jpeg")
    elif text.endswith(".pdf"):
        print("application/pdf")
    elif text.endswith(".zip"):
        print("application/zip")
    elif text.endswith(".txt"):
        print("text/plain")
    else: print("application/octet-stream")

main()
