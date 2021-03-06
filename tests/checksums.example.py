"""
Copy this file and rename it checksums.py

Update this Python data structure with the expected checksums
for the output directories you want to test.

Absolute paths are required.

Leave checksums blank for first run and compare_output.py will generate them for
you to enter here.

See compare_output.py for more information.

"""

#Files that can change
non_deterministic_file_name_endings = [
    'matchMismatch.csv',
    'hmmprob.RData',
]

paths_w_checksums = (
    ('/home/pinerog/msg_work/MSG_toy.run6.misc/hmm_data','c4746dfcbeba033fd60a9de4ca66c268'),
    ('/home/pinerog/msg_work/MSG_toy.run6.misc/hmm_fit','227e5a8f60ecac63bb0a2e905e8c914a'),
    ('/home/pinerog/msg_work/MSG_toy.run6.misc/hmm_fit_images','235d7884d88ddd242b26fb188ae5a473'),
)
