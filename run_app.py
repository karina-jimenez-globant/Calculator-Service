import os
from api.hugo_api import app

if __name__ == '__main__':
    app.logger.info("Running application ...")
    app.debug = True
    host = os.environ.get('HOST', 'localhost')
    port = int(os.environ.get('PORT', 8080))

    app.run(host=host, port=port)

#  removed debug as true for production