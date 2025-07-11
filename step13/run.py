# step12/run.py

from step13 import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # أو "127.0.0.1" إذا أردت تشغيله محليًا فقط
        port=40513,       # يمكنك تغييره حسب ما يناسبك
        debug=True        # اجعلها False في الإنتاج
    )
