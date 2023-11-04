from config.config import BACK_HOST
import requests

#some function for status requests
def getStatus():
    try:
        response = requests.get(BACK_HOST + "/api/metrics")
        return response.json()
    except Exception:
        return 500


def disconnectCon(pid):
    try:
        response = requests.get(BACK_HOST + f"/api/recovery/terminate/{pid}")
        return response.json()
    except Exception:
        return 500


def main():
    getStatus()


if __name__ == "__main__":
    main()