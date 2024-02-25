from server import createApp
import init_db
from dotenv import load_dotenv

load_dotenv()
init_db.dbInit()

app = createApp()

if __name__ == '__main__':
    app.run(debug=True)