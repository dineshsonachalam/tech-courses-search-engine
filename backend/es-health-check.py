import requests
import time

if __name__ == "__main__":
    url = "http://elasticsearch:9200/_cluster/health"
    print("URL: ", url)
    while(True):
        try:
            print("Sleeping for 20 seconds before starting ES health check")
            time.sleep(20)
            response = requests.request("GET", url, headers={}, data={})
            if(response.status_code==200):
                response = response.json()
                status = response["status"]
                if(status != "red"):
                    print("💪 ES is {} and healthy".format(status))
                    break
                else:
                    print("🤒 ES is {} and not healthy".format(status))
        except Exception as e:
            print("❌ Exception: ",e)