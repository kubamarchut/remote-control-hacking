from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileCreated(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_created(self, event):
        print("on_created", event.src_path)
        print(event.src_path.strip())
        if((event.src_path).strip() == ".\test.csv"):
            print("Execute your logic here!")

event_handler = NewFileCreated()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()


while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()