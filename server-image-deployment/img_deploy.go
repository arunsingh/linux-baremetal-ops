package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

// ServerManager manages server deployments and cleanup
type ServerManager struct {
	ApiURL string
	ApiKey string
}

// MonitorDeployment checks the status of a server deployment
func (manager *ServerManager) MonitorDeployment(serverID string) (bool, error) {
	client := &http.Client{}
	req, err := http.NewRequest("GET", manager.ApiURL+"/deployments/"+serverID, nil)
	if err != nil {
		return false, err
	}
	req.Header.Set("Authorization", "Bearer "+manager.ApiKey)
	resp, err := client.Do(req)
	if err != nil {
		return false, err
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return false, err
	}
	fmt.Println("Deployment Status:", string(body))
	return resp.StatusCode == 200, nil
}

func main() {
	manager := ServerManager{
		ApiURL: "http://example.com/api",
		ApiKey: os.Getenv("API_KEY"),
	}
	success, err := manager.MonitorDeployment("server123")
	if err != nil {
		fmt.Println("Error monitoring deployment:", err)
		return
	}
	if success {
		fmt.Println("Deployment successful.")
	} else {
		fmt.Println("Deployment in progress or failed.")
	}
}
