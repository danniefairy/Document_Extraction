from sentence_transformers import SentenceTransformer

model = SentenceTransformer('bert-base-nli-mean-tokens')
documents = """The president of the State University of New York at Oneonta has resigned, as the school grapples with hundreds of reported Covid-19 cases within the university since the beginning of the semester.

In a statement announcing the new interim president on Thursday, State University of New York Chancellor Jim Malatras said that Dr. Barbara Jean Morris had "transitioned from her position as president" and that she wanted to "pursue other opportunities."
A spokesperson for the university told CNN that Morris resigned.
Colleges knew the risks but they reopened anyway. Here&#39;s how they got it all wrong
Colleges knew the risks but they reopened anyway. Here's how they got it all wrong
SUNY Oneonta has reported 712 student cases of Covid-19 since residence halls opened on August 17.
That's more than half the total number of reported cases from campus testing across the entire SUNY system. There have been 1,167 positive cases reported from 61 different campuses.
The rising number of virus cases prompted SUNY Oneonta to switch from in-person learning to an entirely online format in late August.
ADVERTISING

Ads by Teads
Jim Urso, a spokesman for SUNY, commented on the timing of Morris' resignation.
"The Covid spike uptick was at the beginning of September. I just want to clarify her resignation did not come in the middle of that surge," Urso told CNN.
"She did not resign in the midst of this crisis. We're conducting a review on what happened. It's not like she resigned in the middle of the night while students were testing positive by the dozens."
University didn't test students on arrival
The resignation of the sitting president of SUNY Oneonta comes after the university decided not to test students or quarantine them on arrival.
Soon after, the University saw an uptick in positive results. By the time leadership tried to take punitive measures against students for disobeying social distancing orders, the virus had spread.
"We have acknowledged there were several issues with Oneonta's response to the implementation of their reopening plan in the fall," Urso told CNN. "Our chancellor's acknowledged that. It's public record at this point."
The psychology behind why some college students break Covid-19 rules
The psychology behind why some college students break Covid-19 rules
Dennis Craig, the former interim president of SUNY Purchase, which only reported three infections since the start of the semester, will serve as acting president of the university.
A search for someone to fill the role permanently is expected to begin soon.
Eryn Kenney, a junior with a dual major in Adolescent Education and French at SUNY Oneonta who lives off campus, wishes the university had done more to curtail the spread of Covid-19 on campus.
Other state schools in NY tested for Covid-19
"I believe President Morris should have handled COVID much better," Kenney told CNN Friday. "Most SUNY schools required testing before the semester started. My sister goes to SUNY Plattsburgh, and testing was required."
Kenney also said that "there could have also been more restrictions on social distancing," adding that she wished the administration had forced students living on campus to quarantine when they arrived like some other universities did.
But she also acknowledged the role students played in the spread getting out of control.
"I do believe that it is PARTLY [the student body's] fault," she said. "I believe that much of the spreading could have been prevented if the students hadn't partied or hadn't gone anywhere without masks on.\""""

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(documents)
sentence_embeddings = model.encode(sentences, 512)

import numpy as np
from sklearn.cluster import KMeans

labels = KMeans(n_clusters=len(sentences)//5).fit_predict(np.array(sentence_embeddings))
label_line = {}
for i in range(len(labels)):
    if labels[i] not in label_line:
        label_line[labels[i]] = [i]
    else:
        label_line[labels[i]] += [i]
n_lines = []
for label in label_line:
    if len(label_line[label])==1:
        n_lines += label_line[label]
    else:
        n_lines += [label_line[label][0], label_line[label][-1]]
for sentence in [sentences[i] for i in sorted(n_lines)]:
    print(sentence)
