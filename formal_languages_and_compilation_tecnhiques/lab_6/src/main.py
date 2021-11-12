from application import Application


if __name__ == '__main__':
    try:
        application = Application()
        application.run()
    except Exception as e:
        print(f"Error: {e}")



