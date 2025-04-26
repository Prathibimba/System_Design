import pika

def send_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='optimization_queue')
    channel.basic_publish(exchange='', routing_key='optimization_queue', body=message)
    connection.close()

if __name__ == "__main__":
    send_to_queue("Start optimization task")
