from pyngrok import ngrok
import os

# Set your ngrok authtoken (get it from ngrok.com)
ngrok.set_auth_token("2wSjoRelIkRZoe8nGrmjRTdH77j_3cTKUvBwH8xxJQaQEki4N")

# Start ngrok tunnel to Jenkins on port 9090
http_tunnel = ngrok.connect(9090)
print(f"Jenkins is now accessible at: {http_tunnel.public_url}")

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Shutting down ngrok tunnel...")
    ngrok.kill() 