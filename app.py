import a2s
from flask import Flask, request, jsonify
app = Flask(__name__)

servers = [
		'45.235.99.158:27019', '45.235.99.158:27018', '45.235.99.158:27020', '45.235.99.158:27021', 
		'45.235.99.158:27022', '45.235.99.158:27024', '45.235.99.158:27025', '45.235.99.158:27026', 
		'45.235.99.158:27015', '45.235.99.158:27023', '45.235.99.158:27016', '45.235.99.158:27017',  
	]

@app.route('/', methods=['GET'])
def respond():
  informacion = []
  for server in servers:
    ip = server.split(":", 1)
    address = (ip[0], int(ip[1]))
    try:
      info = a2s.info(address)
      serverinfo = {
        "ip": server.replace('45.235.99.158', 'cs.cscagames.com.ar'),
        "name": info.server_name,
        "map": info.map_name,
        "max_players": info.max_players,
        "player_count": info.player_count,
      }
      informacion.append(serverinfo)
    except:
      pass
  return jsonify(informacion)
  

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)