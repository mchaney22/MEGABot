from pyanswers import PyAnswers
import time



# Template superclass for GPT effects
class SimpleEffect(object):
    def __init__(self):
        self.pa = PyAnswers()
        self.examples = []
        self.examples_context = ""
        self.documents = []
        self.file_id = ""

    def query(self, question):
        pass
    
    def query_from_documents(self, question):
        answer = self.pa.query_examples(self.examples_context, self.examples, self.documents, question)
        return answer['answers'][0]

    def query_from_file(self, question):
        answer = self.pa.query_file(self.file_id, question)
        return answer['answers'][0]

    def documents_from_jsonl(self, jsonl_name):
        self.documents = self.pa.file_mgmt.documents_from_jsonl(jsonl_name)

    def require_file(self, file_name):
        self.file_id = self.pa.file_mgmt.get_file_id(file_name)
        if self.file_id == "":
            print("File not found: " + file_name)
            # upload the file
            self.file_id = self.pa.file_mgmt.upload_jsonl(file_name)
        # check if the file is processed
        # wait for the file to be processed
        while(self.pa.file_mgmt.file_status(self.file_id) != "processed"):
            print("File not processed yet: " + self.file_id)
            time.sleep(1)
        print("File processed: " + self.file_id)