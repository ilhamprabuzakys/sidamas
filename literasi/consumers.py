from channels.consumer import SyncConsumer


class literasiConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass