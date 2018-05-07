import nltk;
import shlex;


class Comment():
    
    def __init__(self):
        self.original_id = '';
        self.original_comment_text = '';

        self.expected_toxic = False;
        self.expected_severe_toxic = False;
        self.expected_obscene = False;
        self.expected_threat = False;
        self.expected_insult = False;
        self.expected_identity_hate = False;

        self.resolved_toxic = False;
        self.resolved_severe_toxic = False;
        self.resolved_obscene = False;
        self.resolved_threat = False;
        self.resolved_insult = False;
        self.resolved_identity_hate = False;

        self.analyzed_toxic = False;
        self.analyzed_severe_toxic = False;
        self.analyzed_obscene = False;
        self.analyzed_threat = False;
        self.analyzed_insult = False;
        self.analyze_identity_hate = False;
        
        self.nltk_words = [];
        self.shlex_words = [];
        self.split_words = [];

    
    def set_original(self,
                 comment_id,
                 comment_text,
                 toxic,
                 severe_toxic,
                 obscene,
                 threat,
                 insult,
                 identity_hate):
        self.original_id = comment_id;
        self.original_comment_text = comment_text;
        self.expected_toxic = toxic;
        self.expected_severe_toxic = severe_toxic;
        self.expected_obscene = obscene;
        self.expected_threat = threat;
        self.expected_insult = insult;
        self.expected_identity_hate = identity_hate;
        self.nltk_words = nltk.word_tokenize(comment_text);
        self.shlex_words = shlex.split(comment_text);
        self.split_words = comment_text.split();
        
        
    def analyze_comment_text(self):
        
        return;
        
            
    def get_analyzed(self):
        self.analyzed_toxic = (self.original_toxic != self.resolved_toxic);
        self.analyzed_severe_toxic = (self.original_severe_toxic != self.analyzed_severe_toxic);
        self.analyzed_obscene = (self.original_obscene != self.resolved_obscene);
        self.analyzed_threat = (self.original_threat != self.resolved_threat);
        self.analyzed_insult = (self.original_insult != self.resolved_insult);
        self.analyzed_identity_hate = (self.original_identity_hate != self.resolved_identity_hate);                