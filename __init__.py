from mycroft import MycroftSkill, intent_file_handler


class GoodBye(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bye.good.intent')
    def handle_bye_good(self, message):
        self.speak_dialog('bye.good')


def create_skill():
    return GoodBye()

