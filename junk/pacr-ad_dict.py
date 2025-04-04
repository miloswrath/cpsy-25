import os
import json

def count_t1w_files(base_path):
    subject_dict = {}
    print(f"Base path: {base_path}")
    for subject in os.listdir(base_path):
        subject_path = os.path.join(base_path, subject)
        # Check if the subject path is a directory and matches the expected subject format
        if os.path.isdir(subject_path) and subject.startswith('sub-'):
            print(f"Checking subject: {subject}, Path: {subject_path}")
            session_counts = {'ses-pre': 0, 'ses-post': 0}
            for session in ['ses-pre', 'ses-post']:
                session_path = os.path.join(subject_path, session, 'anat')
                print(f"Checking session: {session}, Path: {session_path}")
                if os.path.isdir(session_path):
                    for item in os.listdir(session_path):
                        item_path = os.path.join(session_path, item)
                        print(f"Checking item: {item}, Path: {item_path}")
                        if item.endswith('T1w.nii') or item.endswith('T1w.nii.gz'):
                            session_counts[session] += 1
                            print(f"Found T1w file: {item}")
            print(f"Found {session_counts['ses-pre']} T1w files for ses-pre and {session_counts['ses-post']} T1w files for ses-post for subject {subject}")
            subject_dict[subject] = session_counts
        else:
            print(f"Skipping {subject_path}, not a directory or not a subject folder")
    return subject_dict

# Use raw string to avoid escaping backslashes
base_path = r"\\itf-rs-store24.hpc.uiowa.edu\vosslabhpc\Projects\PACR-AD\Imaging\BIDS"
subject_dict = count_t1w_files(base_path)

# Correct the output file path
output_file_path = r"res/pac-radt1_dict.json"
with open(output_file_path, "w") as f:
    json.dump(subject_dict, f, indent=4)

print(subject_dict)