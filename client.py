import time
import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for n in range(10):
	# print(f'sending request {request}')
	socket.send(f'set a={n}'.encode())
	# time.sleep(1)
	message = socket.recv()
	print(message)

	socket.send('get a'.encode())
	message = socket.recv()
	print(message)

