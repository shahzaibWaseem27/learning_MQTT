from simple import MQTTClient

def getMQTTClient(client_id, server, port, user, password, keepalive, ssl, ssl_params):
    
    client = MQTTClient(
    
        client_id = client_id,
        server = server,
        port = port,
        user = user,
        password = password,
        keepalive = keepalive,
        ssl = ssl,
        ssl_params = { 'server_hostname': ssl_params }
        
    )
    
    client.connect()
    
    return client


def handleSubscribe(topic, client):
    # Recieves data from the broker
    client.subscribe(topic)
    print("Subscribe Done")


def handleReceivingMessage(topic):
    # Perform desired actions based on the subscribed topic and response
    print(f"Received message on topic: {topic}\n")





