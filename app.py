import a2s
from flask import Flask, request, jsonify
app = Flask(__name__)

servidores = [
  '45.235.98.244:27030', '45.235.98.252:27015', '45.235.98.222:27015', '45.235.99.150:27015', '45.235.99.134:27015', 
  '45.235.98.244:27030', '45.235.98.252:27015', '45.235.98.222:27015', '45.235.99.150:27015', '45.235.99.134:27015', 
  '45.235.98.244:27030', '45.235.98.252:27015',
]

@app.route('/', methods=['GET'])
def respond():
  informacion = []
  for server in servidores:
    ip = server.split(":", 1)
    address = (ip[0], int(ip[1]))
    try:
      info = a2s.info(address)
      serverinfo = {
        "ip": server,
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
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)