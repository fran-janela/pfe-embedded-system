import urequests as request

class SendModule():
    def __init__(self, server_url):
        self.server_url = server_url

    def send_data(self, data):
        try:
            response = request.post(self.server_url, json=data, headers = {'Content-type': 'application/json'})
            return response
        except OSError as e:
            # Check if the OSError has the specific error code ECONNABORTED (103)
            if e.args[0] == 103:
                print("Caught ECONNABORTED error. Handle it appropriately.")
                return {"error": "ECONNABORTED"}
            else:
                # Handle other OSError cases
                print(f"Caught OSError: {e}")
                return {"error": "OSError"}
        except Exception as e:
            # Handle other exceptions
            print(f"Caught exception: {e}")
            return {"error": "Exception"}