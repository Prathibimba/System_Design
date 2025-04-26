import pika

def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    # Process optimization logic here
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='optimization_queue')
channel.basic_consume(queue='optimization_queue', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
