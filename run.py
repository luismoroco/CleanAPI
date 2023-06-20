from application import createApp 
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path='.flaskenv')

app = createApp()

if __name__ == '__main__':
    app.run(debug=bool(os.getenv('DEBUG')), 
            port=int(os.getenv('PORT')))