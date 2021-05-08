from waitress import serve

import server1
serve(server1.app, host='localhost', port=8000)
