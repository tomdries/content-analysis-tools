import docx
import pandas as pd
import regex as re
import utils

class Content:
    def __init__(self, content):
        
        ## load source data, via docx or string
        try: # this only works if content is path to docx file
            doc = docx.Document(content)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
            fullText = '\n'.join(fullText)
            self.text = fullText
        except: # else, the content must just be a string we use directly
            self.text = content
            
            
        ## Search tags and create df
    
        pattern = r'(#[\w|\-]+)(\.[\w|\-|.]+)?({[^}]+})?' # https://regex101.com/r/WvrPav/3
        search_result = re.findall(pattern, self.text)

        df = pd.DataFrame(search_result, columns=['stem', 'suffixes (original)', 'comments']) #put in dataframe

        # find participant number 
        ix_0 = [m.start(0) for m in re.finditer(pattern, self.text)] # search for starting index of each tag in string
        p_list = []
        pattern = r'(?r)P(\d+):' # pattern that matches last mentioned P number, (e.g. P34:). 
        for ix in ix_0:
            p_list.append(int(re.search(pattern, self.text[:ix])[1]))

        df['participant'] = p_list

        # split suffixes
        df['suffixes'] = df['suffixes (original)'].apply(lambda x: x.split('.')[1:])

        self.data = df[['stem', 'suffixes', 'comments', 'participant']]

        
    def count_stems(self):
        df = self.data
        stem_count = df['stem'].value_counts()
        
        first_occurence = df.groupby('stem')['participant'].min()

        stem_count_unique = df.groupby('stem')['participant'].nunique()

        stem_df = pd.DataFrame([stem_count, stem_count_unique, first_occurence]).transpose()
        stem_df.columns = ['stem count', 'stem count unique', 'first occurence']
        
        return stem_df
    
    
    def count_suffixes(self, tag_stem, avoid_double_counting=True):
        df_selected = self.data[self.data.stem==tag_stem]
        participants = df_selected.participant.unique()
        suffixes_mentioned = []
        for p in participants:
            suffixes = utils.flatten(list(df_selected.loc[df_selected.participant==p,'suffixes']))
            if avoid_double_counting:
                suffixes = list(set(suffixes)) # remove repeated mentions (1 vote per participant)
            suffixes_mentioned.append((suffixes))

        suffixes_mentioned = utils.flatten(suffixes_mentioned)
        suffixes_mentioned = [x for x in suffixes_mentioned if len(x)>0] #remove empty tags
        suffixes_mentioned = utils.value_counts(suffixes_mentioned)
        return suffixes_mentioned
            
            


        
        
        

    



        