from flask import Flask, request, jsonify
import random  # Mock optimization logic
import pika
import redis

# Initialize Flask app
app = Flask(__name__)

# Connect to Redis Cache
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# Endpoint for optimization
@app.route('/optimize', methods=['POST'])
def optimize():
    port_data = request.json
    # Mock Optimization Logic
    optimized_schedule = {"berths": random.randint(1, 5), "efficiency": random.random()}

    # Cache the result for future requests
    cache.set('optimized_schedule', str(optimized_schedule))

    # Send optimization task to the message queue
    send_to_queue("Optimization task")

    return jsonify(optimized_schedule)

# Function to send message to RabbitMQ (Message Queue)
def send_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='optimization_queue')
    channel.basic_publish(exchange='', routing_key='optimization_queue', body=message)
    connection.close()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
