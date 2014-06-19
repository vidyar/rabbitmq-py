import pika

class Rabbit():
    message = ""

    def sendMessage(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print " [x] Sent 'Hello World!'"
        connection.close()

    def readMessage(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        print ' [*] Waiting for messages. To exit press CTRL+C'
        def callback(ch, method, properties, body):
            message = body
            print " [x] Received %r" % (body,)
        channel.basic_consume(callback, queue='hello', no_ack=True)
        channel.start_consuming()
        return message

if __name__ == "__main__":
    rabbit = Rabbit()
    rabbit.sendMessage()
    print(rabbit.readMessage())
