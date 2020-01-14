import pika

uesrname='uesrname'#修改用户名
password='password'#修改密码
host='host'#修改链接地址
queue='queue'#修改消息队列
virtual_host='virtual_host'#修改环境

credentials = pika.PlainCredentials(uesrname, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host, port=5672, virtual_host=virtual_host, credentials=credentials))
channel = connection.channel()


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())


# 告诉rabbitmq，用callback来接收消息
channel.basic_consume(queue, callback)
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
