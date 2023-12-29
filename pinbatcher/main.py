from pinbatcher.src.infoinputapp import InfoInputApp


def run():
    app = InfoInputApp()
    title, description, link = app.run()
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Link: {link}")
