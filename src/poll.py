import datetime
import json

class poll_base():
    def __init__(self, poll_id, question):
        self.id = poll_id
        self.question = question
        self.opt_votes = dict()
        self.voters = dict()

    def _add_option(self, option):
        self.opt_votes.update({option: 0})

    def _vote(self, option, voter_id):
        self.voters[voter_id] = option
        # TODO does that actually work? Try in juypter-notebook or something
        if not voter_id in voters:
            self.opt_votes[option] = self.opt_votes[option] + 1

    def write_to_file(self):
        file_path = 'data/' + str(self.id) + '.json'
        with open(file_path, 'w') as poll_file:
            json.dump(self.__dict__, poll_file, ensure_ascii=False)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as poll_file:
            poll_json = json.load(poll_file)
            self.id = poll_json['id']
            self.question = poll_json['question']
            self.opt_votes = poll_json['options']
            self.voters = poll_json['voters']

class poll_yn(poll_base):
    def __init__(self, poll_id, question, bot_ref):
        super().__init__(poll_id, question)
        self.bot = bot_ref
        self._add_option('Yes')
        self._add_option('No')

    # TODO
    # vote function
    # plot function

class poll_opt(poll_base):
    def __init__(self, poll_id, question, bot_ref):
        super().__init__(poll_id, question)
        self.bot = bot_ref
        self.opt_descr = dict()

    # TODO
    # add options function
    # vote function
    # plot function
