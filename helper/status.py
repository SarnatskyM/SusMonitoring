from config.config import BACK_HOST
import requests

#some function for status requests

#/api/metrics
def getStatus():
    try:
        response = requests.get(BACK_HOST + "/api/metrics")
        return response.json()
    except Exception:
        return 500


#/api/recovery/terminate/:pid
def disconnectCon(pid):
    try:
        response = requests.get(BACK_HOST + f"/api/recovery/terminate/{pid}")
        return response.json()
    except Exception:
        return 500


#/api/recovery/terminate/vacuum?table_name=&type=
def getVacuum(table_name, type):
    try:
        response = requests.get(BACK_HOST + f"/api/recovery/vacuum?table_name={table_name}&type={type}")
        if response.status_code == 200:
            return 200
        else:
            return 401
    except Exception:
        return 500

def getShutdown():
    try:
        response = requests.get(BACK_HOST + "/api/recovery/shutdown")
        if response.status_code == 200:
            return 200
        else:
            return 401
    except Exception:
        return 500


def main():
    getStatus()
    getVacuum()

if __name__ == "__main__":
    main()