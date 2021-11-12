import zmq
import threading
import time

global alive

class SatControl:
    def __init__(self, name):
        # Init ZMQ socket
        self.sock = zmq.Context().socket(zmq.REP)
        self.sock.bind("tcp://0.0.0.0:9000")

        self.name = name

        self.alive = True

    def start(self):

        # Create the comms thread
        self.thread = threading.Thread(target= self.comms_thread, args = ())
        self.thread.setDaemon(True)

        # Start the comms thread
        self.thread.start()

        # Loop until the user presses Ctrl+C
        # TODO: Add a way to remotely stop all threads, daemon somewhat fixes this
        while True:
            time.sleep(1)

        thread.join()

    def comms_thread(self):
        while True:

            # Register a poller to revice messages
            poller = zmq.Poller()
            poller.register(self.sock, zmq.POLLIN)

            events = poller.poll(timeout = 2000)

            if(len(events) > 0):
                # Decode received message
                message = events[0][0].recv().decode("utf-8")

                # Split into command and args
                split_message = message.split(" ")

                print(split_message)

                response = "default"
                
                # Switch based on command
                if split_message[0] == "HB":
                    response = self.receive_heartbeat(split_message[1])
                elif split_message[0] == "INIT":
                    response = self.receive_INIT(split_message[1])
                elif split_message[0] == "DRIVE":
                    response = self.receive_DRIVE(split_message[1:])
                
                # Send a reply
                self.sock.send_string(response)
            else:
                print("No message received, resetting")

                # Reset connection info
                self.reset()
            
    def receive_heartbeat(self, message):
        print("Received heartbeat: " + message)

        return self.name

    def receive_INIT(self, message):
        print("Received INIT: " + message)

        return "ACK " + str(self.name)

    def receive_DRIVE(self, message):
        print("Received DRIVE: ")
        print(message)

        return "ACK " + str(self.name)

    def reset(self):
        pass