from market import app
import os
#Checks if the run.py file has executed directly and not imported
#docker run -p 5001:5001 -e DEBUG=1 flask_app_dev
#docker run -p 5001:5001 -e DEBUG=1 <Image_name>


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001, debug=os.environ.get('DEBUG') == '0')