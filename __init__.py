from mycroft import MycroftSkill, intent_file_handler


class PlayAmazonMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.amazon.play.intent')
    def handle_music_amazon_play(self, message):
        self.speak_dialog('music.amazon.play')


def create_skill():
    return PlayAmazonMusic()

